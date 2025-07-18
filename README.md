<p align="center">
  <img src="https://raw.githubusercontent.com/YOUR_USERNAME/HCO-SMS-RAT/main/logo.png" width="200"/>
</p>

<h1 align="center">💌 HCO-SMS-RAT</h1>
<p align="center">
  Remotely access SMS from an Android device through a Termux-built RAT system.<br>
  <b>Educational Purpose Only</b> • <b>Hackers Colony Official</b>
</p>

---

### 🔰 Features

- Access victim SMS remotely
- Termux-based payload builder
- Flask server to collect data
- Works on Android 10–15
- Includes cloudflared integration
- Auto link generation
- Real-time logs

---

### ⚙️ Installation in Termux

```bash
pkg update && pkg upgrade -y
pkg install python git curl -y
pip install flask requests
git clone https://github.com/Hackerscolonyofficial/HCO-SMS-RAT.git
cd HCO-SMS-RAT
bash start.sh
```

> 🚨 This tool is for **educational** and **awareness** purposes only.

---

### 🚀 How to Use

1. Run `bash start.sh`
2. Payload APK will be generated and served
3. Install APK on target device
4. Wait for SMS logs to appear in Termux console

---

### ☁️ Optional: Cloudflare Tunneling

```bash
pkg install cloudflared -y
cloudflared tunnel --url http://localhost:5000
```

---

### ❌ Disclaimer

> This tool is made for **educational purposes only**. Any misuse of this tool for unauthorized access or hacking is strictly forbidden. The creator is not responsible for your actions.

---

### 🤝 Connect with Us

- 🌐 [Hackers Colony Website](https://hackerscolonyofficial.blogspot.com/?m=1)
- 📸 [Instagram](https://www.instagram.com/hackers_colony_official)
- 📘 [Facebook](https://www.facebook.com/share/1AY25it2Em/)
- ✈️ [Telegram](https://t.me/hackersColony)
- 💬 [Discord](https://discord.gg/Xpq9nCGD)
- 📺 [YouTube](https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya)

---

### 👨‍💻 Code by Azhar

> 💬 _“Hacking isn’t just about code. It’s about mindset.”_ — Hackers Colony
