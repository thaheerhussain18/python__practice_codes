from pytube import Playlist

p = Playlist('https://www.youtube.com/watch?v=bm0OyhwFDuY&list=PLsyeobzWxl7pe_IiTfNyr55kwJPWbgxB5')
for video in p.videos:
    video.streams.first().download()
