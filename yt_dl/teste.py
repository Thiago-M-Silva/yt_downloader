from tkinter import *
from youtube_dl import YoutubeDL

class yt_downloader:

    @staticmethod
    def baixa_vid(Link, qualidade):
        ydl_opts = {
            'format': qualidade  # Exemplo: 'best', 'worst', 'bestaudio', 'bestvideo', etc.
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([Link])

class tela:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Baixador YT")
        self.janela.geometry("500x500")  # Define o tamanho da janela

        # Centraliza a janela na tela
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        pos_x = (largura_tela - 500) // 2
        pos_y = (altura_tela - 500) // 2
        self.janela.geometry(f"+{pos_x}+{pos_y}")

        # Cria um campo de texto
        self.campo_texto = Entry(self.janela, width=300)
        self.campo_texto.pack()

        # Lista de opções de qualidade
        self.opcoes_qualidade = ['best', 'worst', 'bestaudio', 'bestvideo']
        self.qualidade_selecionada = StringVar(self.janela)
        self.qualidade_selecionada.set(self.opcoes_qualidade[0])  # Define a qualidade padrão

        # Cria um menu de opções para seleção de qualidade
        self.menu_qualidade = OptionMenu(self.janela, self.qualidade_selecionada, *self.opcoes_qualidade)
        self.menu_qualidade.pack()

        # Cria um botão para baixar o vídeo
        self.botao_baixar = Button(self.janela, text="Baixar", command=self.baixar_video)
        self.botao_baixar.pack()

        # Exibe a janela
        self.janela.mainloop()

    def baixar_video(self):
        link = self.campo_texto.get()
        qualidade = self.qualidade_selecionada.get()
        yt_downloader.baixa_vid(link, qualidade)

# Cria e exibe a janela
tela()
