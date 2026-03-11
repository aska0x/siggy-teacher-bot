from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Siggy Teacher | Ritual AI Expert</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body { background: #0f0f1a; color: white; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
                .card { background: #1a1a2e; padding: 30px; border-radius: 20px; text-align: center; border: 2px solid #f39c12; width: 360px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
                .siggy-img { width: 120px; height: 120px; border-radius: 50%; border: 3px solid #f39c12; margin-bottom: 15px; object-fit: cover; box-shadow: 0 0 15px rgba(243, 156, 18, 0.4); }
                input { width: 100%; padding: 12px; margin-bottom: 10px; border-radius: 10px; border: 1px solid #333; background: #0f0f1a; color: white; box-sizing: border-box; outline: none; }
                input:focus { border-color: #f39c12; }
                button { width: 100%; padding: 12px; background: #f39c12; color: white; border: none; border-radius: 10px; cursor: pointer; font-weight: bold; text-transform: uppercase; transition: 0.3s; }
                button:hover { background: #e67e22; transform: scale(1.02); }
                #res { margin-top: 20px; font-size: 0.85rem; color: #ddd; text-align: left; background: rgba(0,0,0,0.3); padding: 15px; border-radius: 10px; border-left: 4px solid #f39c12; line-height: 1.6; max-height: 200px; overflow-y: auto; }
                a { color: #f39c12; text-decoration: underline; font-weight: bold; }
                .info-tag { font-size: 0.75rem; color: #888; margin-top: 10px; display: block; }
            </style>
        </head>
        <body>
            <div class="card">
                <img src="https://raw.githubusercontent.com/aska0x/siggy-teacher-bot/main/siggy-kucing.png" class="siggy-img">
                <h2 style="color: #f39c12; margin: 0;">SIGGY TEACHER</h2>
                <p style="color: #888; font-size: 0.75rem; margin-bottom: 15px;">The Sovereign AI Knowledge Hub</p>
                <input type="text" id="in" placeholder="Ask me about Ritual AI...">
                <button onclick="ask()">Send Message</button>
                <div id="res"><b>Siggy:</b> Hello Student! I am Siggy. How can I assist you with Ritual AI today?</div>
            </div>
            <script>
                function ask() {
                    const i = document.getElementById('in');
                    const m = i.value.toLowerCase();
                    const r = document.getElementById('res');
                    if(!m) return;

                    let response = "";

                    if(m.includes("hi") || m.includes("hello") || m.includes("halo")) {
                        response = "<b>Siggy:</b> Sup Student! I'm Siggy, your witty guide to <b>Ritual</b>—the premier decentralized AI network. Need to know how we're making AI sovereign?";
                    } 
                    else if(m.includes("ritual") && (m.includes("what") || m.includes("is"))) {
                        response = "<b>Siggy:</b> Ritual is a decentralized AI network that allows for seamless integration of AI models onto any blockchain. It provides a sovereign infrastructure to ensure AI remains open and permissionless. <br><br>For more details, check here: <a href='https://ritualfoundation.org' target='_blank'>ritualfoundation.org</a>";
                    }
                    else if(m.includes("infernet")) {
                        response = "<b>Siggy:</b> Ah, Infernet! That's Ritual's first product. It's a powerful suite that allows smart contracts to request AI inference directly on-chain. It bridges the gap between Web3 and AI! <br><br>Full info: <a href='https://docs.ritual.net' target='_blank'>docs.ritual.net</a>";
                    }
                    else if(m.includes("why") || m.includes("benefit")) {
                        response = "<b>Siggy:</b> Why Ritual? Because it provides <b>Model Integrity</b> and <b>Compute Privacy</b>. It ensures that the AI you use is actually the one you requested, without centralized gatekeepers! <br><br>Deep dive here: <a href='https://ritual.net' target='_blank'>ritual.net</a>";
                    }
                    else if(m.includes("who are you")) {
                        response = "<b>Siggy:</b> I'm the smartest feline on the Ritual Network! I translate complex AI-on-chain theories into bite-sized cat puns and lessons for you.";
                    }
                    else {
                        response = "<b>Siggy:</b> That's a deep one, Student! While I'm in 'Simple Mode' right now, you can find the complete technical breakdown at <a href='https://ritualfoundation.org' target='_blank'>ritualfoundation.org</a>.";
                    }

                    r.innerHTML = response;
                    i.value = "";
                }
            </script>
        </body>
        </html>
        """
        self.wfile.write(html.encode())
        return
