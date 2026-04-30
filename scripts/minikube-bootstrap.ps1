# Minikube bootstrap script for ACEest Fitness

param(
    [string]$ImageName = 'aceest-fitness:latest',
    [string]$Namespace = 'aceest-fitness'
)

Write-Output "Starting Minikube..."
minikube start | Write-Output

Write-Output "Enabling ingress add-on..."
minikube addons enable ingress | Write-Output

Write-Output "Loading Docker image into Minikube: $ImageName"
minikube image load $ImageName | Write-Output

Write-Output "Creating namespace if needed: $Namespace"
kubectl create namespace $Namespace --dry-run=client -o yaml | kubectl apply -f -

Write-Output "Applying Kubernetes manifests"
kubectl apply -n $Namespace -f k8s/service.yaml
kubectl apply -n $Namespace -f k8s/deployment.yaml

Write-Output "Deployment completed."
Write-Output "Run 'kubectl get pods -n $Namespace' to verify."