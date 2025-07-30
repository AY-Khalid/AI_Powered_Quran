from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torch
import torchaudio
from pydub import AudioSegment
import os
import uuid

# Load Whisper model once
processor = WhisperProcessor.from_pretrained("openai/whisper-large-v3")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v3")
model.config.forced_decoder_ids = None  # Avoid forced decoding

def transcribe(audio_path):
    converted_path = None

    try:
        # Create a unique filename
        converted_path = f"{audio_path}_converted_{uuid.uuid4().hex}.wav"
        print(f"[INFO] Converting audio: {audio_path} → {converted_path}")

        # Convert to WAV with 16kHz mono
        audio = AudioSegment.from_file(audio_path)  # autodetects format
        audio = audio.set_frame_rate(16000).set_channels(1)
        audio.export(converted_path, format="wav")

        # Load with torchaudio
        waveform, sample_rate = torchaudio.load(converted_path)
        if waveform.numel() == 0:
            raise ValueError("Audio file is empty or corrupted.")

        input_audio = waveform.squeeze().numpy()

        # Run Whisper
        inputs = processor(input_audio, sampling_rate=16000, return_tensors="pt")
        with torch.no_grad():
            prediction = model.generate(inputs["input_features"])

        transcript = processor.batch_decode(prediction, skip_special_tokens=True)[0]
        print(f"[INFO] Transcription result: {transcript}")

        return transcript

    except Exception as e:
        print(f"[ERROR] Transcription failed: {e}")
        raise e

    finally:
        if converted_path and os.path.exists(converted_path):
            os.remove(converted_path)
            print(f"[CLEANUP] Deleted temp file: {converted_path}")
