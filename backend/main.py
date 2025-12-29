from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from moviepy.editor import VideoFileClip
import shutil
import os

app = FastAPI()

# Allow the frontend to talk to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
EXPORT_DIR = "exports"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(EXPORT_DIR, exist_ok=True)

@app.post("/process")
async def process_video(
    file: UploadFile = File(...), 
    start: float = Form(...), 
    end: float = Form(...)
):
    input_path = os.path.join(UPLOAD_DIR, file.filename)
    output_path = os.path.join(EXPORT_DIR, f"trimmed_{file.filename}")

    # Save the uploaded file
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # MoviePy Logic
    with VideoFileClip(input_path) as video:
        # Basic bounds checking
        clip_end = min(end, video.duration)
        new_video = video.subclip(start, clip_end)
        new_video.write_videofile(output_path, codec="libx264")

    return {"message": "Success", "file": output_path}