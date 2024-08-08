IDE
Als IDE heb ik VS Code gebruikt. De reden hiervoor is dat ik de extensie-integratie erg fijn vind werken en al bekend ben met de IDE door school. Ook heb ik toegang tot Git Bash in VS Code, wat in mijn mening het beste werkt.

VM-omgeving  
Als VM-omgeving heb ik Docker gebruikt.

Efficiëntie: Docker is erg efficiënt omdat het weinig systeembronnen vraagt en over het algemeen snel werkt.
Voorkennis: Ik heb voor verschillende projecten Docker gebruikt, hierdoor had ik al wat voorkennis over hoe Docker werkt.
Extensies: In Docker bestaan er extensies die een image kunnen scannen op zwakke plekken. Voor een eerder project heb ik Snyk gebruikt, in dit geval heb ik dat ook gedaan.
MiniKube
Als MiniKube-omgeving heb ik ook Docker gebruikt. Tijdens het lezen van de MiniKube-documentatie las ik dat Docker ook gebruikt kan worden voor het draaien van een MiniKube-container. Aangezien ik het VM-gedeelte van de opdracht ook in Docker heb gedaan, leek het me een goed plan om dit deel ook in Docker te maken. Voor dit onderdeel is het me niet gelukt om op mijn Windows-pc MiniKube aan de praat te krijgen, maar op mijn MacBook is het wel gelukt. De reden hiervoor weet ik helaas niet.

Gebruikte resources
Ik heb de documentatie gebruikt die op de MiniKube-site staat. Ook heb ik een YouTube-video gebruikt waarin de maker stap voor stap uitlegt hoe hij zijn eigen applicatie laat draaien via MiniKube. Link naar video.

Kwetsbaarheden
Nadat ik de complete SRE-omgeving werkend had gekregen, kon ik met Snyk een scan uitvoeren. Hieruit kwam één kritische fout.

Deze fout geeft aan dat in de library ‘zlib’ een integer overflow zit. Wanneer de maximale waarde binnen het systeem wordt bereikt en er een +1 wordt gegeven, kan het zijn dat de integer naar de laagst mogelijke waarde gaat. Voorbeeld: bij een 8-bit systeem kan de integer gaan van -128 tot +127. Wanneer er een 1 wordt opgeteld bij die 127, zal het systeem weer terugspringen naar -128. Vandaar wordt het ook een wraparound genoemd.

Ik heb verder in de Python-code gezocht naar zwakke plekken of slecht geschreven code. Ik heb niets aangepast, maar wel commentaar geplaatst op de plekken waar de code verbeterd kon worden. Zo stond de secret key gewoon in plaintext in de code, werden alle gebruikers opgehaald bij een poging tot inloggen en werden alle wachtwoorden in plaintext vergeleken met elkaar.
