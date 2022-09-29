from tkinter import *
from tkinter import ttk
from Funciones_BBDD_Enzymes import *

def openSearchWindow(root):
	searchwindow=Toplevel(root)
	root.eval(f'tk::PlaceWindow {str(searchwindow)} center') #Center the window on the screen when the program is initializated
	searchwindow.resizable(False,False)
	textframe=Frame(searchwindow)
	textframe.pack()
	tableframe=Frame(searchwindow)
	tableframe.pack()
	bottomframe=Frame(searchwindow)
	bottomframe.pack()

#Función para borrar campos
	def EraseData():
		id.set("")
		name.set("")
		type.set("")
		ph.set("")
		coefficient.set("")
		activity.set("")
		substrate.set("")

	#Etiqueta y cuadro texto ID
	id=StringVar()
	idlabel=Label(textframe, text="ID")
	idlabel.grid(row=0, column=0, sticky=W)
	idtext=Entry(textframe, textvariable=id)
	idtext.grid(row=0, column=1, columnspan=2)

	#Etiqueta y cuadro texto Nombre
	name=StringVar()
	namelabel=Label(textframe, text="Nombre enzima")
	namelabel.grid(row=1, column=0, sticky=W)
	nametext=Entry(textframe, textvariable=name)
	nametext.grid(row=1, column=1, columnspan=2)

	#Etiqueta y cuadro texto Type
	type=StringVar()
	typelabel=Label(textframe, text="Tipo de enzima")
	typelabel.grid(row=2, column=0, sticky=W)
	typetext=Entry(textframe, textvariable=type)
	typetext.grid(row=2, column=1, columnspan=2)

	#Etiqueta y cuadro texto pH
	ph=StringVar()
	phlabel=Label(textframe, text="pH óptimo de actividad")
	phlabel.grid(row=3, column=0, sticky=W)
	phtext=Entry(textframe, textvariable=ph)
	phtext.grid(row=3, column=1, columnspan=2)

	#Etiqueta y cuadro texto Coefficient
	coefficient=StringVar()
	coefficientlabel=Label(textframe, text="Coeficiente de extinción molar")
	coefficientlabel.grid(row=4, column=0, sticky=W)
	coefficienttext=Entry(textframe, textvariable=coefficient)
	coefficienttext.grid(row=4, column=1, columnspan=2)

	#Etiqueta y cuadro texto Activity
	activity=StringVar()
	activitylabel=Label(textframe, text="Tipo de actividad de la enzima")
	activitylabel.grid(row=5, column=0, sticky=W)
	activitytext=Entry(textframe, textvariable=activity)
	activitytext.grid(row=5, column=1, columnspan=2)

	#Etiqueta y cuadro texto Substrate
	substrate=StringVar()
	substratelabel=Label(textframe, text="Sustrato específico sobre el que actua")
	substratelabel.grid(row=6, column=0, sticky=W)
	substratetext=Entry(textframe, textvariable=substrate)
	substratetext.grid(row=6, column=1, columnspan=2)

	#Botones Acción
		#Botón Buscar
	searchbutton=Button(bottomframe, text="Buscar", width=15)
	searchbutton.grid(row=0, column=0, padx=2)

		#Botón Mdificar
	modifybutton=Button(bottomframe, text="Modificar", width=15)
	modifybutton.grid(row=0, column=1, padx=2)

		#Botón borrar campos
	readbutton=Button(bottomframe, text="Borrar campos", width=15, command=lambda:EraseData())
	readbutton.grid(row=0, column=2, padx=2)

		#Botón borrar instancia
	deletebutton=Button(bottomframe, text="Eliminar", width=15)
	deletebutton.grid(row=0, column=3, padx=2)

	"""Menubar of root"""
	Menubar=Menu(searchwindow)
	searchwindow.config(menu=Menubar, width=300, height=300)

		#BBDD Menu
	BBDDMenu=Menu(Menubar, tearoff=0)
	Menubar.add_cascade(label="BBDD", menu=BBDDMenu)
	BBDDMenu.add_command(label="Salir", command=lambda:CloseApp(root))

		#Action Menu
	actionmenu=Menu(Menubar, tearoff=0)
	Menubar.add_cascade(label="Action", menu=actionmenu)
	actionmenu.add_command(label="Buscar")
	actionmenu.add_command(label="Modificar")
	actionmenu.add_command(label="Borrar campos", command=lambda:EraseData())
	actionmenu.add_command(label="Borrar")


	searchwindow.mainloop()
