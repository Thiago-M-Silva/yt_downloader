from youtube_dl import *
from tkinter import *

link = ['https://www.youtube.com/watch?v=YU4ggIvW-P4']

ydl = YoutubeDL

ydl.download(link)
print('teste')