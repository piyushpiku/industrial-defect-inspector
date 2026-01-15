import io
import os
from fastapi import FastAPI, File, UploadFile, HTTPException, Security, status
from fastapi.security import APIKeyHeader
from PIL import Image
from ultralytics import YOLO

API_KEY = os.getenv("API_KEY", "donaldson-secret-key-123") 
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == API_KEY:
        return api_key_header
    raise HTTPException(status_code=403, detail="Invalid API Key")

app = FastAPI(title="Industrial Defect Inspector")

print("🚀 Loading YOLO Model...")
model = YOLO("best.pt") 

@app.post("/predict")
async def predict(file: UploadFile = File(...), api_key: str = Security(get_api_key)):
    try:
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))
    except:
        raise HTTPException(status_code=400, detail="Invalid image")

    results = model.predict(image, conf=0.25)
    
    detections = []
    decision = "PASS"
    for box in results[0].boxes:
        decision = "REJECT" 
        name = results[0].names[int(box.cls[0])]
        detections.append({"type": name, "confidence": float(box.conf[0])})

    return {"decision": decision, "detections": detections}
