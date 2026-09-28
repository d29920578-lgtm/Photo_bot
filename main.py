import os
from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import replicate
import requests

app = FastAPI()

# Разрешаем сайту подключаться к бэкенду
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Токены (замените на свои)
os.environ["REPLICATE_API_TOKEN"] = "ВАШ_ТОКЕН_REPLICATE"

@app.get("/")
def home():
    return {"status": "Сервер обработки фото запущен!"}

@app.post("/process-photo")
async def process_photo(image: UploadFile, task: str = Form(...)):
    try:
        image_bytes = await image.read()
        
        # Модель для удаления фона (по умолчанию)
        model_id = "replicate/background-removal:76326e6d1c16838a16073703d15911cc64860d54020a66d0c29b76c8c4a4970c"
        
        # Отправка в ИИ
        output_url = replicate.run(model_id, input={"image": image_bytes})
        
        # Ссылка на оплату (заглушка, сюда привязывается ваша платежка)
        payment_url = "https://your-payment-gateway.com"

        return {
            "success": True,
            "preview_url": output_url,
            "payment_url": payment_url
        }
    except Exception as e:
        return {"success": False, "error": str(e)}
