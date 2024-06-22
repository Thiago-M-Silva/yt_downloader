from tkinter import Tk, Label, Entry, Button

# Função para exibir o texto inserido no campo de texto
def exibir_texto():
    texto_inserido = campo_texto.get()
    print(f"Texto inserido: {texto_inserido}")

# Cria a janela
janela = Tk()
janela.title("Minha Janela")
janela.geometry("500x500")  # Define o tamanho da janela

# Centraliza a janela na tela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
pos_x = (largura_tela - 500) // 2
pos_y = (altura_tela - 500) // 2
janela.geometry(f"+{pos_x}+{pos_y}")

# Calcula a largura do campo de texto (3/4 da largura da janela)
largura_campo = (500 * 3) // 4

# Cria um campo de texto
campo_texto = Entry(janela, width=largura_campo)
campo_texto.pack()

# Cria um botão para exibir o texto
botao_exibir = Button(janela, text="Exibir Texto", command=exibir_texto)
botao_exibir.pack()

# Exibe a janela
janela.mainloop()
