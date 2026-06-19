<div align="center">

# Web Clipboard (Server)

**Seamless Cross-Device Clipboard Synchronization**

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/xjyzs/Clipboard_Android?color=orange)](https://github.com/xjyzs/Clipboard/releases)

[简体中文](README.md) · [Report Bug](https://github.com/xjyzs/Clipboard_Server/issues) · [Request Feature](https://github.com/xjyzs/Clipboard_Server/issues)

---

</div>

## ✨ Why Choose Web Clipboard?

Copy on your phone, paste on your PC. Copy on your computer, paste on your tablet. **Zero friction, instant synchronization.**

Web Clipboard is a **free and open-source** tool designed to automatically sync your clipboard contents across your devices and the web browser in real-time.

## 🚀 Key Features

| Feature | Description |
|------|------|
| **Automatic Sync** | Copy on any device, and it is instantly available across all other connected devices. |
| **Web Compatibility** | Built on the Socket.IO protocol, making it easy to integrate with browsers, desktop clients, and other platforms. |

## Client Downloads
[Android(Only the auto upload feature needs Root)](https://github.com/xjyzs/Clipboard_Android)

## 📦 How It Works

```
┌──────────────┐     Socket.IO       ┌──────────────┐
│    Client    │ ◄─────────────────► │    Server    │
│              │                     │   (Python)   │
└──────┬───────┘                     └──────────────┘
       │
Clipboard Detection                  
```

## 📲 Installation Guide

### Prerequisites

- A server or computer capable of running Python 3.

### Steps to Run
#### 1. Create a Virtual Environment (Optional)
```Shell
python3 -m venv .venv
source .venv/bin/activate
```
#### 2. Install Dependencies
```Shell
pip install -r requirements.txt
```
#### 3. Start the Server
```Shell
python clipboard.py
```
The server will be running at: `http://<YOUR_IP_ADDRESS>:11451`

### Script Variants
- `clipboard.py` (Default route is `/`)
- `clipboardWithRouteCb.py` (Default route is `/cb`)



## 🤝 Contributing

Contributions are highly welcome! Here is how you can help:

- 🐛 Report bugs by opening an [Issue](https://github.com/xjyzs/Clipboard_Server/issues)
- 💡 Propose new features or enhancements
- 🔧 Submit Pull Requests to improve the codebase

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

**If you find this project helpful, please give it a ⭐ to support our work!**

Made with ❤️ by [xjyzs](https://github.com/xjyzs)

</div>