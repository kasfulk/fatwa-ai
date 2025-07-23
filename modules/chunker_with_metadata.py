import re
from typing import List

def split_and_tag(docs: List[str], chunk_size=400) -> List[dict]:
    chunks = []
    for doc in docs:
        metadata = {}
        judul = re.search(r'Judul\s*:\s*(.*)', doc)
        bab = re.search(r'Bab\s*:\s*(.*)', doc)
        metadata["judul"] = judul.group(1).strip() if judul else None
        metadata["bab"] = bab.group(1).strip() if bab else None

        paragraphs = [p.strip() for p in doc.split("\n") if p.strip()]
        current_chunk, current_len = [], 0
        for p in paragraphs:
            if current_len + len(p) > chunk_size:
                if current_chunk:
                    chunks.append({
                        "text": " ".join(current_chunk),
                        "judul": metadata["judul"],
                        "bab": metadata["bab"]
                    })
                    current_chunk, current_len = [], 0
            current_chunk.append(p)
            current_len += len(p)
        if current_chunk:
            chunks.append({
                "text": " ".join(current_chunk),
                "judul": metadata["judul"],
                "bab": metadata["bab"]
            })
    return chunks
