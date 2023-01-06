# import tkinter module
from tkinter import * 
from tkinter.ttk import *
from tkhtmlview import HTMLLabel
from CreateNewData import NewData
from ConfigBox import ConfigOpt
from ReadData import ReadDataBase
from Configurates import Config
import RenderWidgets
from PIL import Image
from PIL import ImageTk

# Configurações padrões da Pagina
master = Tk()
master.iconbitmap("2115955.ico")
master.geometry("240x100")
master.state('zoomed')
master.title("Mynotes")

conf = Config()
conf.Readtheme()
conf.ReadThemesInSystem()

#Estilos customizados para a pagina 
StylePageMenu = Style()
StylePageMenu.configure("A.TFrame",background = conf.ColorClass[0]["background"])
StylePageMenu.configure("B.TFrame",background=conf.ColorClass[0]["color"],foreground=conf.ColorClass[0]["color"])

#Importação de informação


t = ReadDataBase()
t = t.ReturnData()
print(t)
r = RenderWidgets.RenderWidget()

ReadDataBase.ReadData()
#Conteudo da Pagina

menu_frame = Frame(master)
menu_frame.configure(height=5,style="A.TFrame")

Bt_newCol = Button(menu_frame)
Bt_updateCol = Button(menu_frame,text="Modificar coleção")
Bt_newCol.configure(text="Nova coleção")
Bt_Config = Button(menu_frame,text="Configurações")
Bt_Config.bind("<Button>",lambda e:ConfigOpt(master))
Bt_newCol.bind("<Button>" ,lambda e: NewData(master))
tese = "abc"
master.bind('r', lambda event: r.UpdateItem(l1,tese,master))

#Adicionar tasks
TaskCreated =  ReadDataBase().GetTasks()
Tasks =""
for value in TaskCreated:
    Tasks += "<h4 style='color:"+conf.ColorClass[0]["color"]+";'>"+value+"</h4>"
    print(Tasks)
var1 = ""

l1 = HTMLLabel(master, html=""" 
<div style='background-color:"""+conf.ColorClass[0]["background"]+"""; font-family: 'Chivo Mono', monospace;'>
<h1 style='color:"""+conf.ColorClass[0]["color"]+""";'background-color:#6c1e7b; font-family: 'Open Sans', sans-serif;'>"""+t["titulo"]+"""</h1>
<h2 style='color:"""+conf.ColorClass[0]["color"]+""";font-family: 'Chivo Mono', monospace;'>"""+t["subtitulo"]+"""</h2>
"""+Tasks+"""
</div>
    """,font=("Calibri", 10))
photo = Image.open("./img/Check.png")
photo = photo.resize((40,40),Image.ANTIALIAS)
photoImg =  ImageTk.PhotoImage(photo)
# Teste para criação de Tasks Isoladas
c1 = Button(l1, text='Python',image=photoImg,compound = LEFT)

menu_frame.pack(fill="x",pady=4)
Bt_newCol.pack(side="left")
Bt_updateCol.pack(side="left")
Bt_Config.pack(side="left")
l1.configure(bg=conf.ColorClass[0]["background"])
l1.pack(fill="both", expand=True,padx=400,pady=50)
c1.pack(side="left")
#Fim do conteudo da Pagina


#Renderizar a pagina

master.configure(bg=conf.ColorClass[0]["background"])
mainloop()

