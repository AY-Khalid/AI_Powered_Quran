from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
import uuid
from app.model import transcribe
from app.matcher import match as match_quran_verse

app = FastAPI()

# Add CORS middleware for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    # Save incoming file
    temp_path = f"./temp_{uuid.uuid4().hex}.webm"
    with open(temp_path, "wb") as f:
        f.write(await file.read())
    print(f"[INFO] Audio file saved as: {temp_path}")

    try:
        # Transcribe
        transcript = transcribe(temp_path)
        print(f"[INFO] Transcription result: {transcript}")

        # Match to Quran
        match_result = match_quran_verse(transcript)

        return {
            "transcript": transcript,
            "match": match_result
        }

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
            print(f"[CLEANUP] Deleted temp file: {temp_path}")
