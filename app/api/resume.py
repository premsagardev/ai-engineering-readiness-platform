import shutil
from fastapi import APIRouter, HTTPException, UploadFile, File, status
from pathlib import Path
from services.pdf_parser import extract_text_from_pdf
from utils.text_cleaner import clean_text
from services.section_extractor import sections
up_load_dir = Path("uploads")
up_load_dir.mkdir(exist_ok = True)

router = APIRouter()

@router.post("/resume/upload")
async def upload_resume(file: UploadFile = File(...)):
    #check for pdf's only
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Only PDF files are allowed"
            )
    file_location = up_load_dir / file.filename
    try:
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail= "There was Error Uploading file {e}"
            )
    finally:
        await file.close()
    # upload only
    # return {
    #     "message" : f"The file {file.filename} was Successfully uploaded",
    #     "location" : str(file_location)
    # }
    # parse and return
    raw_text = extract_text_from_pdf(str(file_location))
    sections = sections(raw_text)
    
    return {
        "message" : f"The file {file.filename} was Successfully uploaded",
        "location" : str(file_location),
        "content" : sections
    }