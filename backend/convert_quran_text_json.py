import json

verses = []

with open("quran_text.txt", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("|")
        if len(parts) == 3:
            surah = int(parts[0])
            ayah = int(parts[1])
            text = parts[2]
            verses.append({"surah": surah, "ayah": ayah, "text": text})

with open("quran.json", "w", encoding="utf-8") as out:
    json.dump(verses, out, ensure_ascii=False, indent=2)
