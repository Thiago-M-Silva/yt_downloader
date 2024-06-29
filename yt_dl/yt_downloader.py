from youtube_dl import YoutubeDL
from tkinter import *

class yt_downloader:
    
    def baixa_vid(Link, qualidade):
        ydl_opts = {
            'format': qualidade  # Exemplo: 'best', 'worst', 'bestaudio', 'bestvideo', etc.
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([Link])

# Exemplo de uso:
# yt_downloader.baixa_vid('URL_DO_VIDEO', 'best')