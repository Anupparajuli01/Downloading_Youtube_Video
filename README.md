# Downloading_Youtube_Video
This python program is desined for macOS.
A simple Python script to download YouTube videos or audio (MP3) on macOS using Homebrew, a virtual environment, ffmpeg, and [yt-dlp] (https://github.com/yt-dlp/yt-dlp).

---

## Features

- Automatically checks for **Homebrew** and installs it if missing
- Creates and uses a Python virtual environment (`ytvenv`). It creates where the file is located. 
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
```
After that it asks if you want to download video or audio. 
Then it asks for the URL of the video. 
Happy Downloading

###  In Terminal (only for MacOS)
1. Installing HomeBrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
2. Installing yt-dlp
```bash
brew install yt-dlp
```
3. Installing ffmpeg (for mp3)
```bash
brew install ffmpeg
```
Now you are ready to download the youtube video/audio.
<br>

To download video copy and replace the URL in the code bellow. By default I have my favourite singer song there. 
```bash
yt-dlp -f "bestvideo[ext=mp4][vcodec^=avc]+bestaudio[ext=m4a]/mp4" \
-o ~/Downloads/"%(title)s.%(ext)s" \
"https://www.youtube.com/watch?v=AMRGmAh2NTk"
```
To download audio copy and replace the URL in the code bellow. By default I have my favourite singer song there.
```bash
yt-dlp -x --audio-format mp3 -o ~/Downloads/"%(title)s.%(ext)s" "https://www.youtube.com/watch?v=AMRGmAh2NTk"
```


