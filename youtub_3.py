from pytube import Playlist

link = input('Enter Youtube Playlist:-')

yt_pla = Playlist(link)

for video in yt_pla.videos:
    video.streams.get_highest_resolution().download("G:\html")
    print("video  Dow:",video.title)

print("All video downled")




