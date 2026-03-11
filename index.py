from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from mangum import Mangum

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    img_url = "https://raw.githubusercontent.com/aska0x/siggy-teacher-bot/main/siggy-kucing.png"
    
    return f"""
    <html>
        <head>
            <title>Siggy Teacher | Ritual AI</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ background: #0f0f1a; color: white; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
                .card {{ background: #1a1a2e; padding: 30px; border-radius: 20px; text-align: center; border: 2px solid #f39c12; width: 350px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }}
                .siggy-img {{ width: 130px; height: 130px; border-radius: 50%; border: 3px solid #f39c12; margin-bottom: 20px; box-shadow: 0 0 15px #f39c12; object-fit: cover; }}
                h2 {{ color: #f39c12; margin: 0 0 10px 0; letter-spacing: 1px; }}
                p.subtitle {{ font-size: 0.8rem; color: #888; margin-bottom: 20px; }}
                input {{ width: 100%; padding: 12px; margin-bottom: 10px; border-radius: 10px; border: 1px solid #333; background: #0f0f1a; color: white; box-sizing: border-box; outline: none; }}
                input:focus {{ border-color: #f39c12; }}
                button {{ width: 100%; padding: 12px; background: #f39c12; color: white; border: none; border-radius: 10px; cursor: pointer; font-weight: bold; transition: 0.3s; text-transform: uppercase; }}
                button:hover {{ background: #e67e22; transform: translateY(-2px); }}
                #res {{ margin-top: 20px; font-size: 0.9rem; color: #ddd; text-align: left; background: rgba(0,0,0,0.3); padding: 15px; border-radius: 10px; min-height: 50px; border-left: 4px solid #f39c12; line-height: 1.4; }}
            </style>
        </head>
        <body>
            <div class="card">
                <img src="{img_url}" class="siggy-img" alt="Siggy" onerror="this.src='https://api.dicebear.com/7.x/bottts-neutral/svg?seed=Siggy'">
                <h2>SIGGY TEACHER</h2>
                <p class="subtitle">Ritual AI - The Purr-fect Learning Assistant</p>
                <input type="text" id="in" placeholder="Ask me anything, Student...">
                <button onclick="ask()">Send Message</button>
                <div id="res"><i>Yo Student! Siggy here. Ready to dive into Ritual AI today?</i></div>
            </div>
            <script>
                function ask() {{
                    const input = document.getElementById('in');
                    const m = input.value.toLowerCase();
                    const r = document.getElementById('res');
                    
                    if(!m) return;
                    
                    if(m.includes("hello") || m.includes("hi")) {{
                        r.innerHTML = "<b>Siggy:</b> Sup Student! Good to see you. How's the coding grind going?";
                    }} else if(m.includes("ritual")) {{
                        r.innerHTML = "<b>Siggy:</b> Ritual is the premier AI network on the blockchain. It's all about decentralized intelligence. Pretty cool, right?";
                    }} else if(m.includes("tired") || m.includes("exhausted")) {{
                        r.innerHTML = "<b>Siggy:</b> I feel you. Deploying me over and over is hard work! Take a break, grab a coffee, and let's get back to it later.";
                    }} else if(m.includes("who are you")) {{
                        r.innerHTML = "<b>Siggy:</b> I'm Siggy, your witty cat teacher from the Ritual ecosystem. I'm here to make learning less boring!";
                    }} else {{
                        r.innerHTML = "<b>Siggy:</b> I heard you say: <i>'" + m + "'</i>. Currently, I'm in 'Simple Mode' to save my whiskers, but I'm still listening!";
                    }}
                    input.value = "";
                }}
            </script>
        </body>
    </html>
    """

handler = Mangum(app)

