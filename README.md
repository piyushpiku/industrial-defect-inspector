# 🏭 Industrial Defect Inspector

An end-to-end **Computer Vision Microservice** designed for automated quality control in manufacturing environments. This system detects surface defects (dents, scratches, anomalies) on industrial components in real-time.

## 🚀 Key Features
* **YOLOv8 Custom Object Detection:** Trained on a dataset of industrial components to identify sub-millimeter defects with high precision.
* **Azure Cloud Deployment:** Fully containerized application running on **Azure Container Instances (ACI)**.
* **Serverless Architecture:** Utilizes **Azure Container Registry (ACR)** for secure image storage and rapid scaling.
* **FastAPI Integration:** Provides a high-performance REST API for integration with factory floor SCADA systems.
* **Dockerized:** Reproducible environment ensures consistent performance across development and production.

## 🛠️ Tech Stack
* **ML Core:** PyTorch, Ultralytics YOLOv8
* **Backend:** Python, FastAPI, Uvicorn
* **Cloud & DevOps:** Microsoft Azure (ACI, ACR), Docker, Bash Scripting
* **Tools:** OpenCV, NumPy

## 🏗️ Architecture
1.  **Input:** Image captured from assembly line camera.
2.  **Processing:** Image sent to Azure Cloud Endpoint via REST API.
3.  **Inference:** YOLOv8 model analyzes image for specific defect classes.
4.  **Output:** JSON response with bounding boxes, confidence scores, and pass/fail status.

## 📦 How to Run
This project is containerized for easy deployment.

### 1. Build the Docker Image
\`\`\`bash
docker build -t defect-inspector .
\`\`\`

### 2. Run Locally
\`\`\`bash
docker run -p 80:80 defect-inspector
\`\`\`

### 3. Access API Documentation
Visit \`http://localhost:80/docs\` to test the inference endpoints interactively.

---
*Created by [Your Name] - [Year]*
