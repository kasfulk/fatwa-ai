# 🕌 Fatwa AI

Chatbot Fatwa adalah sistem berbasis Python yang memungkinkan Anda untuk:
- Mengelola teks kitab berbahasa Indonesia
- Mengekstrak metadata (judul & bab)
- Membagi teks menjadi paragraf
- Menyorot kutipan ayat dan hadits
- Menerjemahkan ke Bahasa Arab menggunakan [LibreTranslate](https://github.com/LibreTranslate/LibreTranslate) atau fallback ke Gemini

---

## 📂 Struktur Folder

```
chatbot-fatwa/
│
├── docker-compose.yml           # Menjalankan semua service
├── Dockerfile                   # Dockerfile untuk aplikasi utama
├── main.py                      # Entry point aplikasi
├── requirements.txt             # Daftar dependensi Python
├── README.md                    # Dokumentasi proyek
└── modules/                     # Modul-modul Python
    ├── translator.py
    ├── metadata_parser.py
    ├── reference_highlighter.py
    └── chunker_with_metadata.py
└── kitab/
    └── contoh.txt               # Tempat Anda menyimpan teks kitab
```

## 📦 Menambahkan Teks Kitab
Tempatkan file `.txt` Anda di dalam folder `kitab/`. File ini akan diproses dalam `main.py`.

## 🐳 docker-compose.yml
```yaml
version: '3.8'
services:
  app:
    build: .
    volumes:
      - .:/app
    ports:
      - "8501:8501"
    environment:
      - LIBRETRANSLATE_URL=http://translator:5000
      - GEMINI_API_KEY=YOUR_GEMINI_API_KEY(optional)
    depends_on:
      - translator

  translator:
    image: libretranslate/libretranslate
    ports:
      - "5000:5000"
    environment:
      - LT_LOCALES=id,en,ar
```

## 🐍 Dockerfile
```Dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

## 📜 requirements.txt
```
requests
dotenv
google-generativeai
langchain
```

## 🚀 Cara Menjalankan
```bash
docker-compose up --build
```

---

## 📥 Contoh Pemrosesan
```python
# main.py
from modules.translator import translate_to_arabic
from modules.metadata_parser import extract_metadata
from modules.reference_highlighter import highlight_references
from modules.chunker_with_metadata import split_and_tag

# Load file kitab
with open("kitab/contoh.txt", "r") as f:
    teks = f.read()

# Highlight referensi
highlighted = highlight_references(teks)

# Chunk + Metadata
chunks = split_and_tag([highlighted])

# Translate
for chunk in chunks:
    translated = translate_to_arabic(chunk["content"])
    print("====")
    print("ID:", chunk["content"])
    print("AR:", translated)
```