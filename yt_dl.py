import tkinter as tk
import customtkinter as ctk
from pytube import YouTube

def baixar():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        titulo.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Baixado!")
    except:
        finishLabel.configure(text="Erro ao baixar!")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    porcentagem = bytes_downloaded / total_size * 100
    per = str(int(porcentagem))
    progresso.configure(text = per +'%')
    progresso.updadte()

# configurações
ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme(Red)

# tela
app = ctk.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# elementos UI
titulo = ctk.CTkLabel(app, text="Insira o link do video a ser baixado:")
titulo.pack(padx=10, pady=10)

# entrada de link
url_var = tk.StringVar()
link = ctk.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# download finalizado
finishLabel = ctk.CTkLabel(app, text="")
finishLabel.pack()

# barra de progresso
progresso = ctk.CTkLabel(app, text="0%")
progresso.pack()

barra_progresso = ctk.CTkProgressBar(app, width=400)
barra_progresso.set(0)
barra_progresso.pack()

# botao de download
download = ctk.CTkButton(app, text="Baixar", command=baixar)
download.pack(padx=10, pady=10)

# execução do app
app.mainloop()