from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    img_url = "https://raw.githubusercontent.com/aska0x/siggy-teacher-bot/main/siggy_kucing.png"
    return f"""
    <html>
        <head>
            <title>Siggy Teacher | Ritual AI</title>
            <style>
                body {{ background: #0f0f1a; color: white; font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
                .card {{ background: #1a1a2e; padding: 30px; border-radius: 20px; text-align: center; border: 2px solid #f39c12; width: 350px; }}
                img {{ width: 150px; border-radius: 15px; margin-bottom: 15px; border: 2px solid #f39c12; }}
                button {{ width: 100%; padding: 10px; background: #f39c12; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; }}
            </style>
        </head>
        <body>
            <div class="card">
                <img src="{img_url}" onerror="this.src='https://placekitten.com/200/200'">
                <h2 style="color:#f39c12;">SIGGY TEACHER</h2>
                <p>Yo Student! Akhirnya aku bangun juga setelah error panjang!</p>
                <button onclick="alert('Siggy: Rehat dulu, coding emang berat!')">TEKAN AKU</button>
            </div>
        </body>
    </html>
    """
