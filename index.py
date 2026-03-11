from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Siggy | Ritual AI Expert</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body { background: #0f0f1a; color: white; font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
                .card { background: #1a1a2e; padding: 35px; border-radius: 30px; text-align: center; border: 2px solid #f39c12; width: 380px; box-shadow: 0 20px 50px rgba(0,0,0,0.7); position: relative; }
                .siggy-img { width: 130px; height: 130px; border-radius: 50%; border: 4px solid #f39c12; margin-bottom: 20px; object-fit: cover; box-shadow: 0 0 25px rgba(243, 156, 18, 0.5); }
                h2 { color: #f39c12; margin: 0; letter-spacing: 3px; font-size: 1.8rem; font-weight: 800; }
                p.tagline { color: #888; font-size: 0.8rem; margin: 5px 0 25px 0; text-transform: uppercase; letter-spacing: 1px; }
                input { width: 100%; padding: 15px; margin-bottom: 12px; border-radius: 12px; border: 1px solid #333; background: #0b0b16; color: white; box-sizing: border-box; outline: none; font-size: 1rem; transition: 0.3s; }
                input:focus { border-color: #f39c12; box-shadow: 0 0 15px rgba(243, 156, 18, 0.2); }
                button { width: 100%; padding: 15px; background: #f39c12; color: white; border: none; border-radius: 12px; cursor: pointer; font-weight: bold; text-transform: uppercase; transition: 0.3s; font-size: 1rem; }
                button:hover { background: #e67e22; transform: translateY(-2px); box-shadow: 0 8px 20px rgba(230,126,34,0.4); }
                #res { margin-top: 25px; font-size: 0.9rem; color: #eee; text-align: left; background: rgba(0,0,0,0.4); padding: 20px; border-radius: 18px; border-left: 5px solid #f39c12; line-height: 1.6; max-height: 250px; overflow-y: auto; }
                a { color: #f39c12; text-decoration: none; font-weight: bold; border-bottom: 1px solid rgba(243, 156, 18, 0.3); }
                a:hover { color: #fff; border-bottom: 1px solid #fff; }
                ::-webkit-scrollbar { width: 6px; }
                ::-webkit-scrollbar-thumb { background: #333; border-radius: 10px; }
            </style>
        </head>
        <body>
            <div class="card">
                <img src="https://raw.githubusercontent.com/aska0x/siggy-teacher-bot/main/siggy-kucing.png" class="siggy-img" alt="Siggy">
                <h2>SIGGY</h2>
                <p class="tagline">Sovereign AI Navigator</p>
                <input type="text" id="in" placeholder="Ask about Ritual AI, Student...">
                <button onclick="
