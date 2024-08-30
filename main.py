from tkinter import Tk, Frame, NSEW, FALSE, Label, LEFT, NW, RAISED, Button, RIDGE
from tkinter import ttk
from tkinter.ttk import Style
from PIL import Image, ImageTk
from logo_loader import load_logos

co0 = "#2e2d2b"
co1 = "#feffff"
co2 = "#e5e5e5"
co3 = "#00a095"
co4 = "#403d3d"
co6 = "#038cfc"
co7 = "#ef5350"
co8 = "#263238"
co9 = "#e9edf5"

janela = Tk()
janela.title("DREEWS")
janela.geometry('1024x768')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

frame_logo = Frame(janela, width=850, height=52, bg=co3)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient='horizontal').grid(row=1, column=0, sticky='ew', ipadx=0)

frame_dados = Frame(janela, width=850, height=65, bg=co1)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient='horizontal').grid(row=3, column=0, sticky='ew', ipadx=0)

frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg=co1)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)

logos = load_logos()

def cadastrar():
    print("Cadastrar Alunos")
    clear_frames()

def adicionar():
    print("Cursos e Turmas")
    clear_frames()

def salvar():
    print("Salvar")
    clear_frames()

def clear_frames():
    for widget in frame_detalhes.winfo_children():
        widget.destroy()
    for widget in frame_tabela.winfo_children():
        widget.destroy()

def control(action):
    if action == "cadastrar":
        cadastrar()
    elif action == "adicionar":
        adicionar()
    elif action == "salvar":
        salvar()

button_cadastro = Button(
    frame_dados,
    image=logos["adicionar"],
    text="Cadastro",
    width=100,
    compound=LEFT,
    overrelief=RIDGE,
    font=("Ivy 9"),
    bg=co1,
    fg=co0,
    command=lambda: control("cadastrar")
)
button_cadastro.grid(row=0, column=0, padx=10, pady=5, sticky='w')

button_adicionar = Button(
    frame_dados,
    image=logos["cadastrar"],  
    text="Adicionar",
    width=100,
    compound=LEFT,
    overrelief=RIDGE,
    font=("Ivy 9"),
    bg=co1,
    fg=co0,
    command=lambda: control("adicionar")
)
button_adicionar.grid(row=0, column=1, padx=10, pady=5, sticky='w')

button_salvar = Button(
    frame_dados,
    image=logos["save"],
    text="Salvar",
    width=100,
    compound=LEFT,
    overrelief=RIDGE,
    font=("Ivy 9"),
    bg=co1,
    fg=co0,
    command=lambda: control("salvar")
)
button_salvar.grid(row=0, column=2, padx=10, pady=5, sticky='w')

janela.grid_columnconfigure(0, weight=1)

janela.mainloop()
