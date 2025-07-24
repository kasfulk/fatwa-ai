from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from modules.translator import translate_to_arabic
from modules.chunker_with_metadata import split_and_tag
from modules.reference_highlighter import highlight_references
from modules.metadata_parser import parse_title_and_chapter
import os

app = FastAPI()

@app.post("/translate")
async def translate_fatwa(request: Request):
    try:
        data = await request.json()
        text = data.get("text", "")

        if not text:
            return JSONResponse(
                status_code=400,
                content={"error": "No text provided for translation."}
            )

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
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"An error occurred: {str(e)}"}
        )

@app.get("/")
async def root():
    return {"message": "Hello World"}

# create API yang bisa mengupload file .epub dengan proteksi extension
@app.post("/upload")
async def upload_epub(request: Request):
    try:
        data = await request.json()
        file = data.get("file", None)

        if not file:
            return JSONResponse(
                status_code=400,
                content={"error": "No file provided for upload."}
            )

        # check if file is .epub
        if not file.endswith(".epub"):
            return JSONResponse(
                status_code=400,
                content={"error": "Invalid file type. Please upload a .epub file."}
            ) 
        
        # save file to ./data directory
        os.makedirs("./data", exist_ok=True)
        with open("./data/epub_file.epub", "wb") as f:
            f.write(file)

        return JSONResponse(
            status_code=200,
            content={"message": "File uploaded successfully."}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"An error occurred: {str(e)}"}
        )