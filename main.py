from tkinter import Tk, Frame, NSEW, FALSE
from tkinter import ttk
from tkinter.ttk import Style
from PIL import ImageTk, Image

# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # Cinza
co3 = "#00a095"  # Verde
co4 = "#403d3d"  # Letra
co6 = "#038cfc"  # Azul
co7 = "#ef5350"  # Vermelha
co8 = "#263238"  # Verde escuro
co9 = "#e9edf5"  # Verde claro

# JANELA
janela = Tk()
janela.title("DREEWS instituição de ensino")
janela.geometry('1024x768')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# FRAMES
frame_logo = Frame(janela, width=850, height=52, bg=co3)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

# SEPARADOR 1
ttk.Separator(janela, orient='horizontal').grid(row=1, column=0, sticky='ew', ipadx=0)

frame_dados = Frame(janela, width=850, height=65, bg=co1)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

# SEPARADOR 2
ttk.Separator(janela, orient='horizontal').grid(row=3, column=0, sticky='ew', ipadx=0)

frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg=co1)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)

#COLUNA
janela.grid_columnconfigure(0, weight=1)

janela.mainloop()
