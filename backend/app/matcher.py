import json
from fuzzywuzzy import fuzz
import re

# Load Quran verses
with open("app/quran.json", "r", encoding="utf-8") as f:
    QURAN = json.load(f)

# Simple Arabic text normalizer
def normalize_arabic(text):
    text = re.sub(r"[ًٌٍَُِّْ]", "", text)  # Remove diacritics
    text = re.sub(r"[إأآا]", "ا", text)     # Normalize alef
    text = re.sub(r"ى", "ي", text)         # Normalize yaa
    text = re.sub(r"ؤ", "و", text)         # Normalize waw
    text = re.sub(r"ئ", "ي", text)         # Normalize yaa
    return text.strip()

def match(transcription):
    transcription = normalize_arabic(transcription)
    best_score = 0
    best_match = None

    for verse in QURAN:
        verse_text = normalize_arabic(verse["text"])
        score = fuzz.partial_ratio(verse_text, transcription)

        if score > best_score:
            best_score = score
            best_match = verse

    if best_score > 70 and best_match:
        return {
            "surah": best_match["surah"],
            "ayah": best_match["ayah"],
            "text": best_match["text"],
            "match_text": f"The verse you recited is Quran Chapter {best_match['surah']} verse {best_match['ayah']}."
        }
    else:
        return {
            "error": "No confident match",
            "match_text": "Sorry, we couldn't confidently identify the verse."
        }
