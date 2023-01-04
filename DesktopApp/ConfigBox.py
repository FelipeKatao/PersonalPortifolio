
# import tkinter module
from tkinter import * 
from tkinter import messagebox
import fnmatch
import xml.etree.cElementTree as XML
from Configurates import Config

def ConfigOpt(master):
    # Configurações padrões da Pagina
    newData = Toplevel(master)
    newData.grab_set()
    newData.iconbitmap("2115955.ico")
    newData.title("Configuracao...")
    newData.geometry("400x200")
    newData.resizable(FALSE,FALSE)
    configTheme = Config()
    configTheme.ReadThemesInSystem()
    Opt = []
    for values in configTheme.ThemeClass:
        Opt.append(values)

    #Conteudo da Pagina
    frame_page = Frame(newData)
    frame_page.configure(height=150,background="#6c1e7b")

    Bt_create = Button(newData)
    Bt_create.configure(text="Salvar configurações",relief="flat",background="#e0aaea", highlightthickness = 0, bd = 0)
    Bt_create.bind("<Button>",lambda e: Saveoptions(newData,clicked.get()))

    label_col = Label(frame_page)
    label_col.configure(text="Nome da sua coleção ",background="#6c1e7b",foreground="#ffffff")

    nome_Col_txt = Entry(frame_page)
    nome_Col_txt.configure(width=30)

    label_tema_txt = Label(frame_page,text="Tema da sua coleção",background="#6c1e7b",foreground="#ffffff")
    tema_col = Entry(frame_page,width=30)

    label_col.pack()
    frame_page.pack(fill="x")


    clicked= StringVar()
    clicked.set( "HelloFire" )
    #Create an instance of Menu in the frame
    main_menu = OptionMenu(frame_page, clicked, *Opt)
    main_menu.pack()

   
    nome_Col_txt.pack()
    label_tema_txt.pack()
    tema_col.pack()

    Bt_create.pack(side="left",ipadx=4,ipady=4,padx=2)
    #Fim do conteudo da Pagina
    newData.destroy

    #Renderizar a pagina

    newData.configure(bg="#6c1e7b")
    mainloop()

    pass

def Saveoptions(page,configuretheme):
    configTheme = Config()
    print(configuretheme)
    configTheme.ModifyTheme(configuretheme)
    page.destroy()
    pass