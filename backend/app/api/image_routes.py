import os
import uuid
from fastapi import APIRouter,UploadFile,File,HTTPException

router=APIRouter(
    prefix='/images',
    tags=['Satellite images']
)

UPLOAD_DIR='datasets/satellite_images'

os.makedirs(UPLOAD_DIR,exist_ok=True)

@router.post('/upload')
async def upload_satellite_image(file:UploadFile=File(...)):
    allowed_extensions={".tif", ".tiff", ".png", ".jpg", ".jpeg"}
    file_extension=os.path.splitext(file.filename)[1].lower
    if file_extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail='Unsupported file format.Upload TIFF,PNG or JPEG images.'
        )
    unique_filename=f"{uuid.uuid4()}{file_extension}"
    
    file_path=os.path.join(UPLOAD_DIR,unique_filename)
    try:
        with open(file_path,"wb") as buffer:
            while chunk := await file.read(1024*1024):
                buffer.write(chunk)
    except Exception:
        if os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(
            status_code=500,
            detail='Failed to save satellite image.'
        )
    finally:
        await file.close()
    return {
        "message": "Satellite image uploaded successfully",
        "filename": unique_filename,
        "file_path": file_path,
        "status": "success"
    }
    