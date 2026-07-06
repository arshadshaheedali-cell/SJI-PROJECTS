# #Made by Arshad Ali








import time
import webbrowser

import threading
import importlib
import subprocess
import sys
#Ensure all packages installed
REQUIRED_PACKAGES = ["requests", "flask"]


def ensure_dependencies():
    for package in REQUIRED_PACKAGES:
        try:
            
            importlib.import_module(package)
        except ImportError:
            print(f"[SETUP] Installing missing dependency: {package} ...")
            try:
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "install", package]
                )
                print(f"[SETUP] Successfully installed {package}.")
            except subprocess.CalledProcessError as e:
                print(f"[ERROR] Failed to install {package}: {e}")
                sys.exit(1)



ensure_dependencies()

import requests
from flask import Flask, request, render_template_string




# #=== hCaptcha keys ===
HCAPTCHA_SITE_KEY = '10000000-ffff-ffff-ffff-000000000001'  # Replace with your public site key
HCAPTCHA_SECRET = '0x0000000000000000000000000000000000000000'  # Replace with your secret key
















app = Flask(__name__)
captcha_verified = False
captcha_event = threading.Event()
















def verify_hcaptcha(response_token: str) -> bool:
   """Verify hCaptcha token with hCaptcha API"""
   data = {
       "secret": HCAPTCHA_SECRET,
       "response": response_token
   }
   try:
       response = requests.post("https://hcaptcha.com/siteverify", data=data, timeout=5)
       return response.json().get("success", False)
   except requests.RequestException:
       return False
























@app.route('/')
def captcha_form():
   """Render CAPTCHA verification form"""
   html = f'''
   <!DOCTYPE html>
   <html>
   <head>
       <title>hCaptcha Verification</title>
       <style>
           body {{
               font-family: Arial, sans-serif;
               display: flex;
               flex-direction: column;
               align-items: center;
               justify-content: center;
               height: 100vh;
               background-color: #f4f4f9;
               margin: 0;
           }}
           .container {{
               background: white;
               padding: 30px;
               border-radius: 8px;
               box-shadow: 0 4px 8px rgba(0,0,0,0.1);
               text-align: center;
           }}
           h1 {{ color: #333; font-size: 1.5rem; margin-bottom: 20px; }}
           button {{
               margin-top: 15px;
               padding: 10px 20px;
               background-color: #003366;
               color: white;
               border: none;
               border-radius: 4px;
               cursor: pointer;
               font-size: 1rem;
           }}
           button:hover {{ background-color: #002244; }}
       </style>
   </head>
   <body>
       <div class="container">
           <h1>Complete CAPTCHA Verification</h1>
           <form action="/verify" method="POST">
               <div class="h-captcha" data-sitekey="{HCAPTCHA_SITE_KEY}"></div>
               <br>
               <button type="submit">Verify</button>
           </form>
       </div>
       <script src="https://js.hcaptcha.com/1/api.js" async defer></script>
   </body>
   </html>
   '''
   return render_template_string(html)
















@app.route('/verify', methods=['POST'])
def verify():
   """Handle CAPTCHA verification"""
   global captcha_verified
   token = request.form.get('h-captcha-response')








   if token and verify_hcaptcha(token):
       captcha_verified = True
       captcha_event.set()
       return """<h3>[SUCCESS] Verification successful! You may now return to the console application.</h3>"""
   return "<h3>[ERROR] Verification failed. Please refresh the browser window to try again.</h3>"
















def run_flask_app():
   """Run Flask app in separate thread"""
   app.run(port=5000, use_reloader=False)
























flask_thread = threading.Thread(target=run_flask_app)
flask_thread.daemon = True
flask_thread.start()
















time.sleep(1)
























print("[INFO] Opening CAPTCHA verification in browser...")
webbrowser.open("http://127.0.0.1:5000")
print("[INFO] Please complete the CAPTCHA validation loop in your browser window.")
















captcha_event.wait(timeout=120)








if not captcha_verified:
   print("[STATUS] CAPTCHA verification failed or timed out.")
   exit()
















print("\n[STATUS] Access Granted. Proceeding with core terminal payload logic...")
# #=== CORE APPLICATION HERE ===
