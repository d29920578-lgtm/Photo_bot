import os
from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# СЮДА ВСТАВЬТЕ ВАШ КЛЮЧ МЕЖДУ КАВЫЧКАМИ:
CLIPDROP_API_KEY = "01f5ab34e79205c79ab4ccde8080e2237d617119b26a030d92333b1527b2e420e6669f32a4204bb99f60ed1048e3ae6f"

@app.get("/")
def home():
    return {"status": "Сервер Clipdrop запущен!"}

@app.post("/process-photo")
async def process_photo(image: str = Form(...)):
    try:
        response = requests.post(
            'https://clipdrop-api.co',
            files={'image_file': requests.get(image).content},
            headers={'x-api-key': CLIPDROP_API_KEY}
        )
        
        if response.status_code == 200:
            return {"success": True, "preview_url": image}
        else:
            return {"success": False, "error": response.text}
    except Exception as e:
        return {"success": False, "error": str(e)}
