from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from mangum import Mangum

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    # Menggunakan link raw agar gambar pasti muncul
    img_url = "https://raw.githubusercontent.com/aska0x/siggy-teacher-bot/main/siggy_kucing.png"
    
    return f"""
    <html>
        <head>
            <title>Siggy Teacher | Offline Mode</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ background: #0f0f1a; color: white; font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
                .card {{ background: #1a1a2e; padding: 30px; border-radius: 20px; text-align: center; border: 2px solid #f39c12; width: 350px; box-shadow: 0 0 20px rgba(243, 156, 18, 0.2); }}
                .siggy-img {{ width: 150px; border-radius: 15px; border: 2px solid #f39c12; margin-bottom: 15px; }}
                input {{ width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 8px; border: none; background: #0f0f1a; color: white; box-sizing: border-box; }}
                button {{ width: 100%; padding: 10px; background: #f39c12; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; }}
                #res {{ margin-top: 15px; font-size: 0.9em; color: #bbb; min-height: 40px; }}
            </style>
        </head>
        <body>
            <div class="card">
                <img src="{img_url}" class="siggy-img" onerror="this.src='https://placekitten.com/200/200'">
                <h2 style="color:#f39c12; margin:0;">SIGGY TEACHER</h2>
                <p style="font-size: 0.7em; color: #888; margin-bottom: 20px;">Vercel Simple Deployment</p>
                <input type="text" id="in" placeholder="Ketik sesuatu...">
                <button onclick="ask()">CHAT</button>
                <div id="res">Yo Student! Aku Siggy. Capek ya coding terus? Rehat dulu sini!</div>
            </div>
            <script>
                function ask() {{
                    const m = document.getElementById('in').value.toLowerCase();
                    const r = document.getElementById('res');
                    
                    if(m.includes("halo") || m.includes("hi")) {{
                        r.innerText = "Siggy: Halo juga Student! Ada yang bisa kucing pintar ini bantu?";
                    }} else if(m.includes("ritual")) {{
                        r.innerText = "Siggy: Ritual itu AI keren di atas Blockchain. Masa gak tau sih?";
                    }} else if(m.includes("capek")) {{
                        r.innerText = "Siggy: Istirahat gih, minum kopi dulu. Nanti kita lanjut lagi!";
                    }} else {{
                        r.innerText = "Siggy: Wah, aku lagi mode hemat energi (Offline). Tapi aku tetep dengerin kok!";
                    }}
                    document.getElementById('in').value = "";
                }}
            </script>
        </body>
    </html>
    """

handler = Mangum(app)
