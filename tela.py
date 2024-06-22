from tkinter import Tk, Label, Entry, Button

class tela:
    # Cria a janela
    janela = Tk()
    janela.title("Bem Vindo!")

    # Cria um campo de texto
    campo_texto = Entry(janela)
    campo_texto.pack()

    # Cria um botão para exibir o texto
    botao_exibir = Button(janela, text="Exibir Texto", command=exibir_texto)
    botao_exibir.pack()

    # Função para exibir o texto inserido no campo de texto
    def exibir_texto():
        texto_inserido = campo_texto.get()
        print(f"Texto inserido: {texto_inserido}")

    # Exibe a janela
    janela.mainloop()