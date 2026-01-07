# 📺 Python YouTube Downloader

A lightweight, terminal-based YouTube downloader built with Python and `yt-dlp`.

> **⚠️ Note:** This script is designed to run on **any operating system** (Linux, macOS, Windows) where Python is available. However, it has been **developed and tested specifically on NixOS**.

## 🚀 Features

- 🎥 **Video & Audio:** Download high-quality video (MP4) or extract audio (MP3).
- 📜 **Playlist Support:** Automatically detects and downloads full playlists.
- 🔐 **Premium/Members-Only:** Supports downloading members-only content via `cookies.txt`.
- 🛡️ **Smart Cookie Handling:** Asks before using cookies to protect your session data.
- ❄️ **Nix Flakes Support:** Ready-to-use development environment for Nix users.

---

## 🛠️ Prerequisites

To run this script, you strictly need **FFmpeg** installed on your system (required for merging video/audio and MP3 conversion).

Please install FFmpeg using your distribution's package manager:

**Debian / Ubuntu / Mint:**
```bash
sudo apt update && sudo apt install ffmpeg
```

**Arch Linux / Manjaro:**
```bash
sudo pacman -Syu ffmpeg
```

**Fedora:**
```bash
sudo dnf install ffmpeg
```

**macOS (Homebrew):**
```bash
brew install ffmpeg
```

---

## 📥 Installation & Usage

### Method 1: Standard (Universal)

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/fd0ra/VideoDownload.git](https://github.com/fd0ra/VideoDownload.git)
   cd VideoDownload
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script:**
   ```bash
   python main.py
   ```

### Method 2: Nix / NixOS (Recommended)

If you are using Nix, the flake will automatically handle Python, `yt-dlp`, and `ffmpeg` dependencies.

1. **Enter the environment:**
   ```bash
   nix develop
   ```

2. **Run the script:**
   ```bash
   python main.py
   ```

---

## 🍪 How to Download Members-Only Videos

To download Premium or Members-only content, the script needs your authentication cookies to verify your account.

1.  **Get a Cookie Export Tool:** Use a browser extension to export your cookies in **Netscape HTTP Cookie File** format.
    * **⚠️ CAUTION:** Be extremely careful when choosing a browser extension.
2.  **Log in:** Make sure you are logged into your YouTube Premium/Member account.
3.  **Save the file:** Export the cookies and save the file exactly as `cookies.txt` in the **project root directory**.
4.  **Run the script:** When asked *"Is this a Members Only video?"*, answer **Yes (e)**.

---

## 🚨 CRITICAL SECURITY WARNING & DISCLAIMER

**PLEASE READ CAREFULLY:**

1.  **Third-Party Extensions:** Browser extensions are third-party software. Some extensions may be malicious or designed to steal your data. **The author of this repository is NOT responsible for the browser extensions you choose to install.** You install and use them entirely at your own risk.

2.  **Data Security:** The `cookies.txt` file contains your active session data (passwords/login tokens). If this file falls into the wrong hands, your account can be compromised.
    * While this repository includes a `.gitignore` file to help prevent you from accidentally uploading your `cookies.txt` to GitHub, **it is ultimately your responsibility to keep your local files safe.**
    * The author accepts **no liability** for any account theft, data breach, or security compromise resulting from the use of third-party extensions or mishandling of sensitive files.

**By using this script and external tools, you acknowledge that you are solely responsible for your own system's security.**
