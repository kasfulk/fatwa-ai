import re

def highlight_references(text: str) -> str:
    text = re.sub(r'(Q\.S\.\s*[^.,\n]+)', r'<strong class="quran">\1</strong>', text)
    text = re.sub(r'(HR\.\s*[^.,\n]+)', r'<strong class="hadith">\1</strong>', text)
    text = re.sub(r'(\b[A-Za-z0-9]*\b[\u0600-\u06FF]{2,}[A-Za-z0-9]*\b)', r'<em class="arab">\1</em>', text)
    return text
