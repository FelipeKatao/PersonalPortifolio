from tkinter import * 
from tkinter import messagebox
import xml.etree.cElementTree as XML

def UpdateCol(master):
 # Configurações padrões da Pagina
    newData = Toplevel(master)
    newData.grab_set()
    newData.iconbitmap("2115955.ico")
    newData.title("Nova coleção")
    newData.geometry("300x200")
    newData.resizable(FALSE,FALSE)

    #Conteudo da Pagina

    #Fim do conteudo da Pagina

    #Renderizar a pagina

    newData.configure(bg="#6c1e7b")
    mainloop()    
    pass
    