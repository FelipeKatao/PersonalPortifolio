# import tkinter module
from tkinter import * 
from tkinter.ttk import *
from tkhtmlview import HTMLLabel
from CreateNewData import NewData
from ReadData import ReadDataBase
from Configurates import Config
import RenderWidgets

# Configurações padrões da Pagina
master = Tk()
master.iconbitmap("2115955.ico")
master.geometry("240x100")
master.state('zoomed')
master.title("Mynotes")

conf = Config()
conf.Readtheme()

#Estilos customizados para a pagina 
StylePageMenu = Style()
StylePageMenu.configure("A.TFrame",background = conf.ColorClass[0]["background"])

#Importação de informação


t = ReadDataBase.ReturnData()
r = RenderWidgets.RenderWidget()

ReadDataBase.ReadData()
#Conteudo da Pagina

menu_frame = Frame(master)
menu_frame.configure(height=5,style="A.TFrame")

Bt_newCol = Button(menu_frame)
Bt_updateCol = Button(menu_frame,text="Modificar coleção")
Bt_newCol.configure(text="Nova coleção")
Bt_newCol.bind("<Button>" ,lambda e: NewData(master))
tese = "abc"
master.bind('r', lambda event: r.UpdateItem(l1,tese,master))

l1 = HTMLLabel(master, html=""" 
<div style='background-color:"""+conf.ColorClass[0]["background"]+"""; font-family: 'Chivo Mono', monospace;'>
<h1 style='color:"""+conf.ColorClass[0]["color"]+""";'background-color:#6c1e7b; font-family: 'Open Sans', sans-serif;'>"""+t[1]+"""</h1>
<h2 style='color:"""+conf.ColorClass[0]["color"]+""";font-family: 'Chivo Mono', monospace;'>"""+t[0]+tese+"""</h2>
</div>
    """,font=("Calibri", 10))
menu_frame.pack(fill="x",pady=4)
Bt_newCol.pack(side="left")
Bt_updateCol.pack(side="left")
l1.configure(bg=conf.ColorClass[0]["background"])
l1.pack(fill="both", expand=True)

#Fim do conteudo da Pagina


#Renderizar a pagina

master.configure(bg=conf.ColorClass[0]["background"])
mainloop()

