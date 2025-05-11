import yt_dlp

# Get the URL input from the user
music_url = input("Enter the YouTube URL:\n")

# yt-dlp options for downloading and converting audio
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'song.%(ext)s',  # The output template for the file
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',  # Convert the file to MP3
        'preferredquality': '320',  # Set the quality to 320 kbps
    }],
}

# Use yt_dlp to download and convert the audio
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    try:
        # Extract info and download the audio
        info = ydl.extract_info(music_url, download=True)
        print(f"Downloaded: {info['title']} as MP3")
    except Exception as e:
        print(f"Error during download: {e}")