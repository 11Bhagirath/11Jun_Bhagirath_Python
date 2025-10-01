from pytubefix import YouTube

url = "https://youtu.be/k1PISUqfkVA?si=xwdfc5xbb2gdnARD"

# Progress callback
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f"\rDownloading... {percentage_of_completion:.2f}%", end="")

# Create YouTube object with callback
yt = YouTube(url, on_progress_callback=on_progress)

# Get highest resolution video-only stream
video_stream = yt.streams.filter(adaptive=True, only_video=True, file_extension="mp4") \
    .order_by("resolution") \
    .desc() \
    .first()

# Download the stream
print("Starting download...")
video_stream.download()
print("\nDownload completed ✅")
