from fastapi import APIRouter, File, HTTPException, UploadFile
from app.services.image_service import save_satellite_image
router = APIRouter(prefix="/images", tags=["Satellite images"])


@router.post("/upload")
async def upload_satellite_image(file: UploadFile = File(...)):
    try:
        result = await save_satellite_image(file)

        return {
            "message": "Satellite image uploaded successfully",
            "status": "success",
            **result
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception:
        raise HTTPException(status_code=500, detail="Image upload failed.")
