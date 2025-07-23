from fastapi import FastAPI, Request
from modules.translator import translate_to_arabic
from modules.chunker_with_metadata import split_and_tag
from modules.reference_highlighter import highlight_references
from modules.metadata_parser import parse_title_and_chapter

app = FastAPI()

@app.post("/translate")
async def translate_fatwa(request: Request):
    data = await request.json()
    text = data.get("text", "")

    arabic = translate_to_arabic(text)
    highlighted = highlight_references(arabic)
    chunks = split_and_tag([text])
    metadata = parse_title_and_chapter(text)

    return {
        "original": text,
        "translated": arabic,
        "highlighted": highlighted,
        "chunks": chunks,
        "metadata": metadata
    }
