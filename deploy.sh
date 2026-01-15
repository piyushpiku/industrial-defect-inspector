
RG_NAME="IndustrialInspectorRG"
REGISTRY_NAME="defectregistry01"
IMAGE_NAME="defect-inspector:v1"
ACI_NAME="defect-api"
DNS_LABEL="industrial-defect-api"

export PATH="$PATH:/usr/local/bin:/opt/homebrew/bin:/Applications/Docker.app/Contents/Resources/bin"

echo "🚀 Logging into Azure..."
az login

echo "🏗️ Checking Infrastructure..."
az group create --name $RG_NAME --location eastus
az acr create --resource-group $RG_NAME --name $REGISTRY_NAME --sku Basic --admin-enabled true

echo "🔑 Logging into Registry..."
az acr login --name $REGISTRY_NAME

echo "📦 Building Docker Image..."
docker build --platform linux/amd64 -t $REGISTRY_NAME.azurecr.io/$IMAGE_NAME 
docker push $REGISTRY_NAME.azurecr.io/$IMAGE_NAME

echo "🔐 Fetching Registry Password..."
REGISTRY_PW=$(az acr credential show --name $REGISTRY_NAME --query "passwords[0].value" -o tsv)

echo "🌍 Deploying Serverless Container..."
az container create \
  --resource-group $RG_NAME \
  --name $ACI_NAME \
  --image $REGISTRY_NAME.azurecr.io/$IMAGE_NAME \
  --os-type Linux \
  --cpu 1 --memory 2 \
  --registry-login-server $REGISTRY_NAME.azurecr.io \
  --registry-username $REGISTRY_NAME \
  --registry-password $REGISTRY_PW \
  --dns-name-label $DNS_LABEL \
  --ports 80 \
  --environment-variables API_KEY="default-dev-key"

echo "✅ DEPLOYMENT COMPLETE!"
echo "👉 API Docs: http://$DNS_LABEL.eastus.azurecontainer.io/docs"
