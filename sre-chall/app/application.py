import sqlite3
import logging
from flask import Flask, session, redirect, url_for, request, render_template, abort
#from werkzeug.security import check_password_hash, generate_password_hash ---> deze import is voor een latere verbetering waarbij de wachtwoord hashes worden vergeleken ipv plaintext wachtwoorden


# de secret key is niet veilig. deze moet niet in de source code staan.
app = Flask(__name__)
app.secret_key = b"192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf"
app.logger.setLevel(logging.INFO)

# app = Flask(__name__)
# # app.secret_key = os.environ.get("SECRET_KEY", os.urandom(24))
# # app.logger.setLevel(logging.INFO)


def get_db_connection():
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row
    return connection


def is_authenticated():
    if "username" in session:
        return True
    return False

# de manier waarop users wordt opgehaald is erg inefficiënt.
#  met SELECT * FROM users haal je alle gebruikers op. dat is onnodig
# het is momenteel niet vatbaar voor sql injectie.
# als de query wordt aangepast naar 
# SELECT * FROM users WHERE username = '{username}' AND password = '{password}' loop je risico op sql injectie.
def authenticate(username, password):
    connection = get_db_connection()
    users = connection.execute("SELECT * FROM users").fetchall()
    connection.close()

    for user in users:
        if user["username"] == username and user["password"] == password:
            app.logger.info(f"the user '{username}' logged in successfully with password '{password}'")
            session["username"] = username
            return True

    app.logger.warning(f"the user '{ username }' failed to log in '{ password }'")
    abort(401)

# Verbeterde code:
#  1. Gebruik een parameterized query om alleen de gebruiker op te halen die overeenkomt met de opgegeven gebruikersnaam.
#  2. Gebruik 'check_password_hash' om het gehashte wachtwoord te vergelijken, wat veiliger is.

#  def authenticate(username, password):
#      connection = get_db_connection()
#      user = connection.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
#      connection.close()

#      if user and check_password_hash(user["password"], password):
#          app.logger.info(f"the user '{username}' logged in successfully")
#          session["username"] = username
#          return True

#      app.logger.warning(f"the user '{username}' failed to log in")
#      abort(401)
@app.route("/")
def index():
    return render_template("index.html", is_authenticated=is_authenticated())


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if authenticate(username, password):
            return redirect(url_for("index"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
