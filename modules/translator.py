import requests
import os

LIBRE_URL = os.getenv("LIBRETRANSLATE_URL", "http://localhost:5000")

def translate_to_arabic(text: str) -> str:
    try:
        res = requests.post(f"{LIBRE_URL}/translate", json={
            "q": text,
            "source": "id",
            "target": "ar",
            "format": "text"
        })
        if res.ok:
            return res.json()["translatedText"]
    except Exception:
        pass
    return "[GAGAL_TERJEMAH]"
