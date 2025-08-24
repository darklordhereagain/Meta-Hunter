# 🚀 Meta-Hunter

Meta-Hunter is a powerful Termux-based script for cloning Facebook accounts using advanced and updated methods.  
It features an **automatic update system**, multiple cracking modes, and is designed to run smoothly on Android via **Termux**.

> ⚠️ **For educational and research purposes only. Use responsibly.**

---

## 📱 Termux Installation Guide

### 🧰 Requirements

- ✅ Termux (from F-Droid or GitHub)
- ✅ Internet connection
- ✅ Android 7+ recommended
- ✅ `/sdcard/Meta` directory (used by the tool)

---

### ⚙️ Installation Steps

```bash
pkg update && pkg upgrade -y
pkg install python git -y
pkg install libandroid-support
rm -rf Meta-Hunter
git clone --depth=1 https://github.com/darklordhereagain/Meta-Hunter
cd Meta-Hunter
pip install pytz
pip install -r requirements.txt
termux-setup-storage
python Meta.py
