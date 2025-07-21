import os
import sys
import subprocess

VENV_DIR = os.path.join(os.path.dirname(__file__), "ytvenv")

def check_or_install_homebrew():
    print("Checking if Homebrew is installed...")
    try:
        subprocess.check_call(['which', 'brew'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Homebrew is installed.")
    except subprocess.CalledProcessError:
        print("Homebrew is not installed. Installing now...")
        try:
            subprocess.check_call(
                '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"',
                shell=True
            )
            print("Homebrew installed successfully!")
        except subprocess.CalledProcessError:
            print("Error: Failed to install Homebrew. Please install it manually and run this script again.")
            sys.exit(1)

def ensure_venv():
    if not os.path.exists(VENV_DIR):
        print("Creating virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", VENV_DIR])
    else:
        print("Virtual environment already exists.")

def install_yt_dlp():
    pip_exe = os.path.join(VENV_DIR, "bin", "pip")
    print("Installing/upgrading yt-dlp in venv...")
    subprocess.check_call([pip_exe, "install", "--upgrade", "yt-dlp"])

def check_or_install_ffmpeg():
    print("Checking if ffmpeg is installed...")
    try:
        subprocess.check_call(['which', 'ffmpeg'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("ffmpeg is installed.")
    except subprocess.CalledProcessError:
        print("ffmpeg is not installed. Installing via Homebrew...")
        try:
            subprocess.check_call(['brew', 'install', 'ffmpeg'])
            print("ffmpeg installed successfully!")
        except subprocess.CalledProcessError:
            print("Error: Failed to install ffmpeg. Please install it manually (brew install ffmpeg) and run this script again.")
            sys.exit(1)

def run_video_downloader(url):
    python_exe = os.path.join(VENV_DIR, "bin", "python")
    script_code = f"""
import yt_dlp
import os

url = {repr(url)}
download_dir = os.path.expanduser("~/Downloads")

ydl_opts = {{
    'format': 'bestvideo[ext=mp4][vcodec^=avc]+bestaudio[ext=m4a]/mp4',
    'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
    'noplaylist': True
}}

print(f"Downloading video from: {{url}}")
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
print("Video download complete!")
"""
    subprocess.check_call([python_exe, "-c", script_code])

def run_audio_downloader(url):
    python_exe = os.path.join(VENV_DIR, "bin", "python")
    script_code = f"""
import yt_dlp
import os

url = {repr(url)}
download_dir = os.path.expanduser("~/Downloads")

ydl_opts = {{
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
    'postprocessors': [{{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }}],
    'noplaylist': True
}}

print(f"Downloading MP3 audio from: {{url}}")
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
print("Audio download complete!")
"""
    subprocess.check_call([python_exe, "-c", script_code])

if __name__ == "__main__":
    check_or_install_homebrew()
    ensure_venv()
    install_yt_dlp()
    check_or_install_ffmpeg()

    while True:
        choice = input("Do you want to download v)ideo or a)udio (v/a)?: ").strip().lower()
        if choice in ('v', 'a'):
            break
        print(" Please enter 'v' for video or 'a' for audio.")

    if len(sys.argv) > 1:
        video_url = sys.argv[1]
    else:
        video_url = input("Enter the YouTube URL: ").strip()

    if choice == 'v':
        run_video_downloader(video_url)
    else:
        run_audio_downloader(video_url)
