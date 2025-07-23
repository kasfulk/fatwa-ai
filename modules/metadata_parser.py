import re

def parse_title_and_chapter(text: str) -> dict:
    title_match = re.search(r'^\s*(Judul\s*:\s*.+)', text, re.IGNORECASE | re.MULTILINE)
    chapter_match = re.search(r'^\s*(Bab\s*:\s*.+)', text, re.IGNORECASE | re.MULTILINE)
    return {
        "judul": title_match.group(1) if title_match else None,
        "bab": chapter_match.group(1) if chapter_match else None
    }
