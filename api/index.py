from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from groq import Groq
from mangum import Mangum

app = FastAPI()

# API KEY
MY_API_KEY = "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"
client = Groq(api_key=MY_API_KEY)

@app.get("/", response_class=HTMLResponse)
def home():
    # Link Gambar Langsung dari GitHub kamu
    img_url = "https://raw.githubusercontent.com/aska0x/siggy-teacher-bot/main/siggy_kucing.png"
    
    return f"""
    <html>
        <head>
            <title>Siggy Teacher | Ritual AI</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ background: #0f0f1a; color: white; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; overflow: hidden; }}
                .card {{ background: #1a1a2e; padding: 30px; border-radius: 25px; text-align: center; border: 2px solid #f39c12; width: 350px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }}
                .siggy-img {{ width: 150px; height: 150px; border-radius: 20px; border: 3px solid #f39c12; margin-bottom: 20px; object-fit: cover; box-shadow: 0 0 15px #f39c12; }}
                input {{ width: 100%; padding: 12px; margin-bottom: 15px; border-radius: 10px; border: 1px solid #333; background: #0f0f1a; color: white; box-sizing: border-box; }}
                button {{ width: 100%; padding: 12px; background: #f39c12; color: white; border: none; border-radius: 10px; cursor: pointer; font-weight: bold; transition: 0.3s; }}
                button:hover {{ background: #e67e22; transform: scale(1.02); }}
                #res {{ margin-top: 20px; font-size: 0.9em; color: #bbb; line-height: 1.5; text-align: left; max-height: 150px; overflow-y: auto; padding-right: 5px; }}
                .loader {{ display: none; color: #f39c12; font-style: italic; margin-top: 10px; }}
            </style>
        </head>
        <body>
            <div class="card">
                <img src="{img_url}" class="siggy-img" alt="Siggy Teacher" onerror="this.src='https://api.dicebear.com/7.x/bottts-neutral/svg?seed=Siggy'">
                <h2 style="color:#f39c12; margin:0 0 10px 0;">SIGGY TEACHER</h2>
                <p style="font-size: 0.8em; margin-bottom: 20px; color: #888;">Ritual AI - Learning is a Purr-ocess</p>
                <input type="text" id="in" placeholder="Tanya apa saja, Student...">
                <button onclick="ask()">KIRIM PESAN</button>
                <div id="loader" class="loader">Siggy lagi mikir... 🐾</div>
                <div id="res"><i>Yo Student! Ready to learn something today?</i></div>
            </div>
            <script>
                async function ask() {{
                    const m = document.getElementById('in').value;
                    const r = document.getElementById('res');
                    const l = document.getElementById('loader');
                    if(!m) return;
                    
                    l.style.display = "block";
                    r.style.display = "none";
                    
                    try {{
                        const res = await fetch('/api/chat?msg=' + encodeURIComponent(m));
                        const d = await res.json();
                        r.innerText = d.siggy || d.error;
                    }} catch (e) {{ 
                        r.innerText = "Error: Koneksi terputus!"; 
                    }} finally {{
                        l.style.display = "none";
                        r.style.display = "block";
                    }}
                }}
            </script>
        </body>
    </html>
    """

@app.get("/api/chat")
def chat(msg: str):
    try:
        completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are Siggy, a witty cat teacher. You are part of Ritual, the AI on-chain network. Call the user Student. Be brief, smart, and use cat puns occasionally."},
                {"role": "user", "content": msg}
            ],
            model="llama-3.3-70b-versatile"
        )
        return {"siggy": completion.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}

# Handler untuk Vercel
handler = Mangum(app)
