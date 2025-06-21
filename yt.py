import yt_dlp

url = input("Enter the YouTube video URL: ")

choice = input("Download as MP4 (video) or MP3 (audio)? Enter 'mp4' or 'mp3': ").strip().lower()

outtmpl = '%(title).80s.%(ext)s'

if choice == 'mp3':
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': outtmpl,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True,
        'quiet': False,
        'no_warnings': True,
    }
elif choice == 'mp4':
    ydl_opts = {
        'format': (
            'bestvideo[height<=720][vcodec^=avc1]+bestaudio[acodec^=mp4a]/'
            'bestvideo[height<=720]+bestaudio/'
            'best[height<=720][ext=mp4]/'
            'best'
        ),
        'merge_output_format': 'mp4',
        'outtmpl': outtmpl,
        'noplaylist': True,
        'quiet': False,
        'no_warnings': True,
    }
else:
    print("Invalid choice. Please enter 'mp4' or 'mp3'.")
    exit()

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"✅ Download as {choice.upper()} completed.")
except Exception as e:
    print(f"Download failed: {e}")
