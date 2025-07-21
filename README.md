# Downloading_Youtube_Video
This python program is desined for macOS.
A simple Python script to download YouTube videos or audio (MP3) on macOS using Homebrew, a virtual environment, ffmpeg, and [yt-dlp] (https://github.com/yt-dlp/yt-dlp).

---

## Features

- Automatically checks for **Homebrew** and installs it if missing
- Creates and uses a Python virtual environment (`venv`)
- Installs or upgrades `yt-dlp` inside the virtual environment
- Checks for `ffmpeg` and installs it via Homebrew if missing (required for audio extraction)
- Supports downloading video (MP4) or extracting audio as MP3
- Saves downloads to your `~/Downloads` folder

---

## Requirements

- macOS with Python 3.6 or higher installed (usually pre-installed)
- Internet connection for installing packages and downloading videos

---

## Setup and Usage

### 1. Clone or download this repository

```bash
git clone https://github.com/Anupparajuli01/Downloading_Youtube_Video.git
cd Downloading_Youtube_Video
python3 VideoAudioDownloaderFromYoutube.py


