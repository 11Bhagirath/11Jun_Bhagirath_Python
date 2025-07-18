from pytubefix import YouTube

url="https://youtu.be/gh8DuVpFeNE?si=2VaeySlngt2wW_1R"

YouTube(url).streams.first().download()