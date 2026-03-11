from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from groq import Groq
from mangum import Mangum

app = FastAPI()
handler = Mangum(app) # Handler harus di atas untuk Vercel

MY_API_KEY = "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"
client = Groq(api_key=MY_API_KEY)

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Siggy Teacher | Ritual AI</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body { background: #0f0f1a; color: #e0e0e0; font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
                .container { background: rgba(255,255,255,0.05); padding: 40px; border-radius: 20px; text-align: center; border: 1px solid #f39c12; width: 400px; }
                img { width: 150px; border-radius: 15px; border: 2px solid #f39c12; }
                input { width: 100%; padding: 10px; margin: 15px 0; border-radius: 5px; border: none; }
                button { width: 100%; padding: 10px; background: #f39c12; color: white; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; }
                #res { margin-top: 20px; font-size: 0.9em; color: #bbb; }
            </style>
        </head>
        <body>
            <div class="container">
                <img src="https://raw.githubusercontent.com/aska0x/siggy-teacher-bot/main/siggy_kucing.png" onerror="this.src='https://placekitten.com/200/200'">
                <h1>SIGGY TEACHER</h1>
                <input type="text" id="in" placeholder="Ask me something, Student...">
                <button onclick="ask()">SEND MESSAGE</button>
                <div id="res"><i>Yo Student! Ready to learn?</i></div>
            </div>
            <script>
                async function ask() {
                    const m = document.getElementById('in').value;
                    const r = document.getElementById('res');
                    if(!m) return;
                    r.innerText = "Siggy is thinking...";
                    try {
                        const res = await fetch('/api/chat?msg=' + encodeURIComponent(m));
                        const d = await res.json();
                        r.innerText = d.siggy || d.error;
                    } catch (e) { r.innerText = "Error: Connection lost!"; }
                }
            </script>
        </body>
    </html>
    """

@app.get("/api/chat")
def chat(msg: str):
    try:
        resp = client.chat.completions.create(
            messages=[{"role": "system", "content": "You are Siggy, a cat teacher. Call user Student. Be witty and brief."},
                      {"role": "user", "content": msg}],
            model="llama-3.3-70b-versatile"
        )
        return {"siggy": resp.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}
