from fastapi import APIRouter, HTTPException
from app.services.detection_service import run_detection

router = APIRouter(prefix="/detection", tags=["Anomaly Detection"])

@router.post("/run")
def detect_anomalies(image_path: str):
    try:
        return run_detection(image_path)

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Anomaly detection failed."
        )
