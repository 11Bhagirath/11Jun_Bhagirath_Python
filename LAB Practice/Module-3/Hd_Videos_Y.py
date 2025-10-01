from pytubefix import YouTube

url = "https://www.youtube.com/watch?v=bB7CrdjL4D0"
yt = YouTube(url)

# Get highest resolution video-only stream
video_stream = yt.streams.filter(adaptive=True, only_video=True, file_extension="mp4") \
    .order_by("resolution") \
    .desc() \
    .first()

# Download the stream
video_stream.download()
