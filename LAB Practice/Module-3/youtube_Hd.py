from pytubefix import YouTube

url = "https://youtu.be/gLUFh9nYmAw?si=AIsJTc4wOOHuWZlX"
yt = YouTube(url)

# Get highest resolution video-only stream
video_stream = yt.streams.filter(adaptive=True, type="video", file_extension="mp4").order_by("resolution").desc().first().download()