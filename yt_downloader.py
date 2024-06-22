from youtube_dl import * 
from tkinter import *

ydl = YoutubeDL

class yt_downloader:

    def baixa_vid(Link):
        ydl.download(Link)
