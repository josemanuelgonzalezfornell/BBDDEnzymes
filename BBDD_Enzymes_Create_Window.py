from tkinter import scrolledtext
from Funciones_BBDD_Enzymes import *
from tkinter import *

#funciones interruptor
datagivens=0 #nos determina que campo se ha rellenado

def openCreateWindow(root):

	createwindow=Toplevel(root)
	root.eval(f'tk::PlaceWindow {str(createwindow)} center') #Center the window on the screen when the program is initializated
	createwindow.resizable(False,False)
	textframe=Frame(createwindow)
	textframe.pack()
	bottomframe=Frame(createwindow)
	bottomframe.pack()
	


	#Función para imprimir datos en la función read
	def PrintDataReadData():
		if id.get()!="":
			datagivens="id"
			data=ReadData(datagivens,str(id.get()))
		if name.get()!="":
			datagivens="name"
			data=ReadData(datagivens,name.get())
		if type.get()!="":
			datagivens="type"
			data=ReadData(datagivens,type.get())
		if ph.get()!="":
			datagivens="pH"
			data=ReadData(datagivens,str(ph.get()))
		if coefficient.get()!="":
			datagivens="coefficient"
			data=ReadData(datagivens,str(coefficient.get()))
		if activity.get()!="":
			datagivens="activity"
			data=ReadData(datagivens,activity.get())
		if substrate.get()!="":
			datagivens="substrate"
			data=ReadData(datagivens,substrate.get())
		if commentstext.get("1.0",END)!="\n":
			datagivens="comments"
			data=ReadData(datagivens,commentstext.get("1.0",END))
		id.set(data[0][0])
		name.set(data[0][1])
		type.set(data[0][2])
		ph.set(data[0][3])
		coefficient.set(data[0][4])
		activity.set(data[0][5])
		substrate.set(data[0][6])
		commentstext.insert(END, data[0][7].rstrip("\n"))

	#Función para borrar campos tras la función delete
	def EraseDataDeleteFunction():
		from tkinter import messagebox
		confirmation=DeleteData(id.get())
		if confirmation=="yes":
			id.set("")
			name.set("")
			type.set("")
			ph.set("")
			coefficient.set("")
			activity.set("")
			substrate.set("")
			commentstext.delete("1.0", END)

	#Función para borrar campos
	def EraseData():
		id.set("")
		name.set("")
		type.set("")
		ph.set("")
		coefficient.set("")
		activity.set("")
		substrate.set("")
		commentstext.delete("1.0", END)

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

	#Etiqueta y cuadro de texto Comentarios
	commentslabel=Label(textframe, text="Comentarios")
	commentslabel.grid(row=7, column=0, sticky=W)
	commentstext=Text(textframe, width=26, height=10)
	commentstext.grid(row=7, column=1, sticky=W, columnspan=10)
	scrollcomments=Scrollbar(textframe, command=commentstext.yview)
	scrollcomments.grid(row=7, column=5, sticky=NSEW)
	commentstext.config(yscrollcommand=scrollcomments.set)

	#Botón Crear instancia
	createbutton=Button(bottomframe, text="Crear", width=15, command=lambda:CreateData(name.get(),type.get(),ph.get(),coefficient.get(),activity.get(),substrate.get(), commentstext.get("1.0", END)))
	createbutton.grid(row=0, column=0, padx=2)

	#Botón borrar campos
	readbutton=Button(bottomframe, text="Borrar campos", width=15, command=lambda:EraseData())
	readbutton.grid(row=0, column=1, padx=2)

	"""Menubar of root"""
	Menubar=Menu(createwindow)
	createwindow.config(menu=Menubar, width=300, height=300)

		#BBDD Menu
	BBDDMenu=Menu(Menubar, tearoff=0)
	Menubar.add_cascade(label="BBDD", menu=BBDDMenu)
	BBDDMenu.add_command(label="Salir", command=lambda:CloseApp(root))

		#Action Menu
	actionmenu=Menu(Menubar, tearoff=0)
	Menubar.add_cascade(label="Action", menu=actionmenu)
	actionmenu.add_command(label="Crear", command=lambda:CreateData(name.get(),type.get(),ph.get(),coefficient.get(),activity.get(),substrate.get(), commentstext.get("1.0", END)))
	actionmenu.add_command(label="Borrar campos", command=lambda:EraseData())

	createwindow.mainloop()