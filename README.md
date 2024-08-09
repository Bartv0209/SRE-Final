Docker VM omgeving: docker pull bvink0209/sre  
Docker Minikube omgeving: docker pull bvink0209/kicbase

MiniKube omgeving: 
 
minikube start --driver=docker  
kubectl apply -f deployment.yaml  
minikube service sre-chall-service
