from tkinter import *
from BBDD_Enzymes_Create_Window import *
from Funciones_BBDD_Enzymes import *
from BBDD_Enzymes_Search_Window import *

"""Window of main menu"""


root=Tk()
root.resizable(False, False)
root.eval("tk::PlaceWindow . center") #Center the window on the screen when the program is initializated
root.title("BBDD")

"""Main menus and initial buttons"""

mainmenu=Frame(root)
mainmenu.pack()

conectinitialbutton=Button(mainmenu, text="Conectar", width=15, command=lambda:connectToBBDD())
conectinitialbutton.grid(column=0, row=0, pady=2)

createinitialbutton=Button(mainmenu, text="Crear", width=15, command=lambda:openCreateWindow(root))
createinitialbutton.grid(column=0, row=1, pady=2)

searchinitialbutton=Button(mainmenu, text="Buscar", width=15, command=lambda:openSearchWindow(root))
searchinitialbutton.grid(column=0, row=2, pady=2)

openbbddinitialbutton=Button(mainmenu, text="Abrir BBDD", width=15)
openbbddinitialbutton.grid(column=0, row=3, pady=2)

closebutton=Button(mainmenu, text="Cerrar", width=15, command=lambda:CloseApp(root))
closebutton.grid(column=0, row=4, pady=2)

"""Menubar of root"""
Menubar=Menu(root)
root.config(menu=Menubar, width=300, height=300)

	#BBDD Menu
BBDDMenu=Menu(Menubar, tearoff=0)
Menubar.add_cascade(label="BBDD", menu=BBDDMenu)
BBDDMenu.add_command(label="Conectar", command=lambda:connectToBBDD())
BBDDMenu.add_command(label="Salir", command=lambda:CloseApp(root))

	#Action Menu
actionmenu=Menu(Menubar, tearoff=0)
Menubar.add_cascade(label="Action", menu=actionmenu)
actionmenu.add_command(label="Crear", command=lambda:openCreateWindow(root))
actionmenu.add_command(label="Buscar")

	#View Menu
viewmenu=Menu(Menubar, tearoff=0)
Menubar.add_cascade(label="View", menu=viewmenu)
viewmenu.add_command(label="Ver BBDD")

mainloop()