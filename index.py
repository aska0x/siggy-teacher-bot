from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Pure HTML - No Python variables to break the code
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Siggy Teacher</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body { background: #0f0f1a; color: white; font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
                .card { background: #1a1a2e; padding: 30px; border-radius: 20px; text-align: center; border: 2px solid #f39c12; width: 320px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
                .siggy-img { width: 130px; height: 130px; border-radius: 50%; border: 3px solid #f39c12; margin-bottom: 20px; object-fit: cover; }
                input { width: 100%; padding: 12px; margin-bottom: 10px; border-radius: 10px; border: 1px solid #333; background: #0f0f1a; color: white; box-sizing: border-box; }
                button { width: 100%; padding: 12px; background: #f39c12; color: white; border: none; border-radius: 10px; cursor: pointer; font-weight: bold; width: 100%; }
                #res { margin-top: 20px; font-size: 0.9rem; color: #ddd; text-align: left; background: rgba(0,0,0,0.3); padding: 15px; border-radius: 10px; border-left: 4px solid #f39c12; }
            </style>
        </head>
        <body>
            <div class="card">
                <img src="https://raw.githubusercontent.com/aska0x/siggy-teacher-bot/main/siggy-kucing.png" class="siggy-img">
                <h2 style="color: #f39c12; margin: 0 0 15px 0;">SIGGY TEACHER</h2>
                <input type="text" id="in" placeholder="Ask me something...">
                <button onclick="ask()">SEND</button>
                <div id="res">Yo Student! Siggy is finally here. No more errors. What's up?</div>
            </div>
            <script>
                function ask() {
                    const i = document.getElementById('in');
                    const m = i.value.toLowerCase();
                    const r = document.getElementById('res');
                    if(!m) return;
                    if(m.includes("hi") || m.includes("hello")) {
                        r.innerHTML = "<b>Siggy:</b> Sup! Glad we finally fixed this!";
                    } else if(m.includes("ritual")) {
                        r.innerHTML = "<b>Siggy:</b> Ritual AI is the future, and you just built a piece of it!";
                    } else {
                        r.innerHTML = "<b>Siggy:</b> I hear you! We are officially live in English now.";
                    }
                    i.value = "";
                }
            </script>
        </body>
        </html>
        """
        self.wfile.write(html.encode())
        return
