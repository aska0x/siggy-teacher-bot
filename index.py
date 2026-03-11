from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from mangum import Mangum

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    # Kita tidak pakai f-string di sini supaya aman dari bentrok kurung kurawal CSS
    return """
    <html>
        <head>
            <title>Siggy Teacher | Ritual AI</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body { background: #0f0f1a; color: white; font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
                .card { background: #1a1a2e; padding: 30px; border-radius: 20px; text-align: center; border: 2px solid #f39c12; width: 350px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
                .siggy-img { width: 130px; height: 130px; border-radius: 50%; border: 3px solid #f39c12; margin-bottom: 20px; object-fit: cover; }
                h2 { color: #f39c12; margin: 0 0 10px 0; }
                input { width: 100%; padding: 12px; margin-bottom: 10px; border-radius: 10px; border: 1px solid #333; background: #0f0f1a; color: white; box-sizing: border-box; }
                button { width: 100%; padding: 12px; background: #f39c12; color: white; border: none; border-radius: 10px; cursor: pointer; font-weight: bold; }
                #res { margin-top: 20px; font-size: 0.9rem; color: #ddd; text-align: left; background: rgba(0,0,0,0.3); padding: 15px; border-radius: 10px; border-left: 4px solid #f39c12; }
            </style>
        </head>
        <body>
            <div class="card">
                <img src="https://raw.githubusercontent.com/aska0x/siggy-teacher-bot/main/siggy_kucing.png" class="siggy-img" onerror="this.src='https://api.dicebear.com/7.x/bottts-neutral/svg?seed=Siggy'">
                <h2>SIGGY TEACHER</h2>
                <input type="text" id="in" placeholder="Ask me anything, Student...">
                <button onclick="ask()">Send Message</button>
                <div id="res"><i>Yo Student! Siggy here. Ready to talk?</i></div>
            </div>
            <script>
                function ask() {
                    const input = document.getElementById('in');
                    const m = input.value.toLowerCase();
                    const r = document.getElementById('res');
                    if(!m) return;
                    
                    if(m.includes("hi") || m.includes("hello")) {
                        r.innerHTML = "<b>Siggy:</b> Sup Student! How's the grind going?";
                    } else if(m.includes("ritual")) {
                        r.innerHTML = "<b>Siggy:</b> Ritual is the premier AI network on-chain. Pretty cool, right?";
                    } else if(m.includes("who are you")) {
                        r.innerHTML = "<b>Siggy:</b> I'm Siggy, your witty cat teacher from the Ritual ecosystem!";
                    } else {
                        r.innerHTML = "<b>Siggy:</b> I heard you say: '" + m + "'. I'm still learning, but I'm listening!";
                    }
                    input.value = "";
                }
            </script>
        </body>
    </html>
    """

handler = Mangum(app)



