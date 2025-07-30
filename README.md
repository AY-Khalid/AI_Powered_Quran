# Quran Verse Recognition Web App

This is an AI-powered web application that allows users to **recite Quranic verses using a microphone**, and automatically identifies the verse using OpenAI's Whisper and fuzzy text matching.

## Features

- Record your voice directly in the browser  
- Transcribe speech using **Whisper (large-v3)** locally (no API key needed)  
- Match transcription to closest Quran verse using fuzzy logic  
- Display the matched Surah, Ayah, and original Arabic text  

---

## Tech Stack  

| Layer       | Tech                                 |  
|-------------|--------------------------------------|  
| Frontend    | React (mic recording + UI)           |  
| Backend     | FastAPI                              |  
| AI Model    | [Whisper](https://github.com/openai/whisper) via HuggingFace Transformers |  
| Audio       | `torchaudio`, `pydub`, `ffmpeg`      |  
| Matching    | `fuzzywuzzy` + Quran JSON file       |  

---

## How to Run Locally  

### 1. Clone the Repo  
  
```
git clone https://github.com/yourusername/quran-verse-recognition.git  
cd quran-verse-recognition
```

2. Install Backend Dependencies  
```
cd backend  
python -m venv venv  
source venv/bin/activate  # or venv\Scripts\activate on Windows  
pip install -r requirements.txt  
Make sure ffmpeg is installed and added to your system PATH.  
```
3. Run the FastAPI Server  
```
uvicorn app.main:app --reload --port 8000
``` 
4. Run the React Frontend  
```
cd frontend  
npm install  
npm start  
Your app will be available at http://localhost:3000  
```
Directory Structure  

```
├── backend/  
│   ├── app/  
│   │   ├── main.py          # FastAPI route handler  
│   │   ├── model.py         # Whisper transcription logic  
│   │   ├── matcher.py       # Fuzzy verse matcher  
│   │   └── quran.json       # Quran verses dataset  
├── frontend/  
│   ├── App.js               # Main React app  
│   ├── MicRecorder.js       # Microphone logic + fetch  
│   ├── App.css              # Optional styles
```
**Planned Improvements**  
We plan to add the following features in the future:  

- Tafsir (verse explanations) via AI or public APIs  

- Language detection and translation  

- Pronunciation scoring  

- Similarity heatmaps (e.g., matched words)  

- Feedback loop for user-corrected matches  

- Mobile responsiveness & offline support  

**AI Use Summary**  
This project uses:  
 
- OpenAI Whisper (large-v3) for automatic speech recognition  

- Fuzzy text matching to approximate verse identity  

__(Coming soon: LLMs for tafsir and feedback)__  

**Requirements**  
- Python 3.8+  

- Node.js (for React frontend)  

- FFmpeg (ffmpeg in PATH)  

- Whisper & HuggingFace Transformers  

- Torchaudio  

- Pydub  

- fuzzywuzzy  

__License__  
MIT License — free to use and modify on my permission **aniduyakbu@gmail.com**.  

__Contributing__  
PRs and suggestions are welcome! Please fork the repo and submit changes via pull request.  

## Author: Anidu Yakubu Khalid
