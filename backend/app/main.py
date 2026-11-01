from fastapi import FastAPI

app=FastAPI(title="Oil spill detection api",description="Satellite-based oil spill anomaly detection and vessel correlation system",version="1.0.0")

@app.get('/')
def home():
    return {
        "message": "Oil Spill Detection API is running",
        "project": "Oil Spill Detection System",
        "status": "success"
    }
 
@app.get('/health')   
def health_check():
    return {
        "message":"Backend is running successfully."
    }