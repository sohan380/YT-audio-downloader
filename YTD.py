# install pytube before running. Use - pip3 install pytube

from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)
yd = yt.streams.get_audio_only()

# For Video download use this
# yd = yt.streams.get_highest_resolution()

yd.download('/Users/sohan/Music/YT music')