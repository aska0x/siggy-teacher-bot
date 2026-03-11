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
    return """
    <html>
        <head>
            <title>Siggy Teacher | Ritual AI</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&display=swap" rel="stylesheet">
            <style>
                body { 
                    background: radial-gradient(circle, #1a1a2e 0%, #0f0f1a 100%); 
                    color: #e0e0e0; font-family: 'Space Grotesk', sans-serif; 
                    display: flex; justify-content: center; align-items: center; 
                    height: 100vh; margin: 0; overflow: hidden;
                }
                .container { 
                    background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px);
                    border-radius: 20px; border: 1px solid rgba(255,255,255,0.1);
                    padding: 40px; width: 90%; max-width: 450px; text-align: center;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                }
                .siggy-img { 
                    width: 180px; height: 180px; border-radius: 20px;
                    object-fit: cover; border: 2px solid #f39c12;
                    filter: drop-shadow(0 0 15px #f39c12); 
                    animation: float 3s ease-in-out infinite; 
                }
                @keyframes float { 0% { transform: translateY(0px); } 50% { transform: translateY(-10px); } 100% { transform: translateY(0px); } }
                h1 { color: #f39c12; margin: 15px 0 5px 0; letter-spacing: 2px; font-weight: 700; }
                .subtitle { font-size: 0.8em; opacity: 0.6; margin-bottom: 20px; letter-spacing: 1px; }
                input { 
                    width: 100%; padding: 12px; border-radius: 10px; border: none; 
                    background: #252545; color: white; margin-top: 10px; outline: none;
                    box-sizing: border-box;
                }
                button { 
                    width: 100%; padding: 12px; margin-top: 10px; border-radius: 10px; 
                    border: none; background: #f39c12; color: white; font-weight: bold; cursor: pointer;
                }
                #response { 
                    margin-top: 25px; min-height: 60px; font-size: 0.9em; 
                    line-height: 1.6; color: #bbb; border-top: 1px solid #333; padding-top: 15px; text-align: left;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <img src="https://raw.githubusercontent.com/aska0x/siggy-teacher-bot/main/siggy_kucing.png" class="siggy-img" onerror="this.src='https://api.dicebear.com/7.x/bottts-neutral/svg?seed=Siggy'">
                <h1>SIGGY TEACHER</h1>
                <div class="subtitle">YOUR CURIOUS COMPANION IN RITUAL</div>
                <input type="text" id="userInput" placeholder="Ask me something, Student...">
                <button onclick="askSiggy()">SEND MESSAGE</button>
                <div id="response"><i>Yo Student! Ready to learn about Ritual? Ask me anything!</i></div>
            </div>
            <script>
                async function askSiggy() {
                    const input = document.getElementById('userInput').value;
                    const resDiv = document.getElementById('response');
                    if(!input) return;
                    resDiv.innerHTML = "<i>Siggy is thinking...</i>";
                    try {
                        const response = await fetch('/api/chat?msg=' + encodeURIComponent(input));
                        const data = await response.json();
                        resDiv.innerText = data.siggy || data.error;
                    } catch (err) { resDiv.innerText = "Error: Brain fuzzy!"; }
                }
            </script>
        </body>
    </html>
    """

@app.get("/api/chat")
def chat(msg: str):
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are Siggy, a chill cat teacher in a suit. Call user Student. Ritual is Sovereign Layer for AI. Brief and witty."},
                {"role": "user", "content": msg}
            ],
            model="llama-3.3-70b-versatile"
        )
        return {"siggy": response.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}

handler = Mangum(app)