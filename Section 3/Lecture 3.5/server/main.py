from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse
import shutil
import os

app = FastAPI()

@app.post("/file")
def upload_file(file:UploadFile):
    try:
        with open(f"server/files/{file.filename}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return f"file uploaded as: {file.filename}"
    except:
        raise HTTPException(status_code=400, detail="File uploaded failed")
    
@app.get("/file/{filename}")
def download_file(filename:str):
    filepath = f"server/files/{filename}"
    if os.path.isfile(filepath):
        return FileResponse(filepath, filename=filename)
    else:
        raise HTTPException(status_code=404, detail="File not found")