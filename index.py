from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    # Ini link gambar kamu yang sudah benar
    img_url = "https://raw.githubusercontent.com/aska0x/siggy-teacher-bot/main/siggy_kucing.png"
    
    return f"""
    <html>
        <head>
            <title>Siggy Teacher | Live</title>
            <style>
                body {{ background: #0f0f1a; color: white; font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
                .card {{ background: #1a1a2e; padding: 30px; border-radius: 20px; text-align: center; border: 2px solid #f39c12; width: 350px; }}
                img {{ width: 180px; border-radius: 15px; margin-bottom: 15px; border: 2px solid #f39c12; }}
                h1 {{ color: #f39c12; margin: 0; }}
                p {{ color: #888; }}
            </style>
        </head>
        <body>
            <div class="card">
                <img src="{img_url}" onerror="this.src='https://placekitten.com/200/200'">
                <h1>SIGGY LIVE!</h1>
                <p>Status: Berhasil Deploy di Vercel</p>
                <hr style="border: 0.5px solid #333; margin: 20px 0;">
                <p style="color: #eee;">"Student, akhirnya kita berhasil tembus error!"</p>
            </div>
        </body>
    </html>
    """
