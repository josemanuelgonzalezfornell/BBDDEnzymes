from tkinter import messagebox
from Funciones_BBDD_Enzymes import *
from tkinter import *
import sqlite3

# funciones interruptor
datagivens = 0  # nos determina que campo se ha rellenado


def openCreateWindow(root):

    while True:
        try:
            createwindow = Toplevel(root)
            textframe = Frame(createwindow)
            textframe.pack()
            bottomframe = Frame(createwindow)
            bottomframe.pack()

            # Función para borrar campos
            def EraseData():
                name.set("")
                microrganism.set("")
                type.set("")
                vector.set("")
                ph.set("")
                activity.set("")
                substrate.set("")
                adjustmenttype.set("")
                intraextracellular.set(intraextracellularoptions[0])
                soluble.set(solubleoptions[0])
                protocolpurification.set("")
                protocolreplegament.set("")
                aa.set("")
                mw.set("")
                temperatureexpression.set("")
                temperatureactivity.set("")
                pi.set("")
                iptg.set("")
                coefficient.set("")
                timeexpression.set("")
                km.set("")
                kmunit.set("")
                kmerror.set("")
                kcat.set("")
                kcatunit.set("")
                kcaterror.set("")
                kmkcat.set("")
                kmkcatunit.set("")
                kmkcaterror.set("")
                seqdnatext.delete("1.0", END)
                seqaatext.delete("1.0", END)
                commentstext.delete("1.0", END)

            # Títulos
            unittitlecreatewindow = Label(
                textframe, text="Unidad", font=("bold"))
            unittitlecreatewindow.grid(row=0, column=15)
            unittitlecreatewindow.config(font="Verdana 12 bold")
            errortitlecreatewindow = Label(
                textframe, text="Error estándar", font=("bold"))
            errortitlecreatewindow.grid(row=0, column=16)
            errortitlecreatewindow.config(font="Verdana 12 bold")

            # Etiqueta y cuadro texto ID
            newid = str(obtainNewID())
            idlabel = Label(textframe, text="ID")
            idlabel.grid(row=1, column=0, sticky=W)
            idtext = Label(textframe, text=newid)
            idtext.grid(row=1, column=1)

            # Etiqueta y cuadro texto Nombre
            name = StringVar()
            namelabel = Label(textframe, text="Nombre enzima")
            namelabel.grid(row=2, column=0, sticky=W)
            nametext = Entry(textframe, textvariable=name)
            nametext.grid(row=2, column=1)

            # Etiqueta y cuadro texto Microorganismo de procedencia
            microrganism = StringVar()
            microrganismlabel = Label(
                textframe, text="Microorganismo de procedencia")
            microrganismlabel.grid(row=3, column=0, sticky=W)
            microrganismtext = Entry(textframe, textvariable=microrganism)
            microrganismtext.grid(row=3, column=1)

            # Etiqueta y cuadro texto Type
            type = StringVar()
            typelabel = Label(textframe, text="Tipo de enzima")
            typelabel.grid(row=4, column=0, sticky=W)
            typetext = Entry(textframe, textvariable=type)
            typetext.grid(row=4, column=1)

            # Etiqueta y cuadro texto Vector
            vector = StringVar()
            vectorlabel = Label(textframe, text="Vector")
            vectorlabel.grid(row=5, column=0, sticky=W)
            vectortext = Entry(textframe, textvariable=vector)
            vectortext.grid(row=5, column=1)

            # Etiqueta y cuadro texto pH
            ph = StringVar()
            phlabel = Label(textframe, text="pH óptimo de actividad")
            phlabel.grid(row=6, column=0, sticky=W)
            phtext = Entry(textframe, textvariable=ph)
            phtext.grid(row=6, column=1)

            # Etiqueta y cuadro texto Activity
            activity = StringVar()
            activitylabel = Label(
                textframe, text="Tipo de actividad de la enzima")
            activitylabel.grid(row=7, column=0, sticky=W)
            activitytext = Entry(textframe, textvariable=activity)
            activitytext.grid(row=7, column=1)

            # Etiqueta y cuadro texto Substrate
            substrate = StringVar()
            substratelabel = Label(
                textframe, text="Sustrato específico sobre el que actúa")
            substratelabel.grid(row=8, column=0, sticky=W)
            substratetext = Entry(textframe, textvariable=substrate)
            substratetext.grid(row=8, column=1)

            # Etiqueta y cuadro texto Tipo ajuste
            adjustmenttype = StringVar()
            adjustmenttypelabel = Label(textframe, text="Tipo de ajuste")
            adjustmenttypelabel.grid(row=9, column=0, sticky=W)
            adjustmenttypetext = Entry(textframe, textvariable=adjustmenttype)
            adjustmenttypetext.grid(row=9, column=1)

            # Etiqueta y cuadro texto Intra o extracelular
            intraextracellular = StringVar()
            intraextracellularoptions = ["", "Intracelular", "Extracelular"]
            intraextracellular.set(intraextracellularoptions[0])
            intraextracellularlabel = Label(
                textframe, text="Localización en el cultivo")
            intraextracellularlabel.grid(row=10, column=0, sticky=W)
            intraextracellulartext = OptionMenu(
                textframe, intraextracellular, *intraextracellularoptions)
            intraextracellulartext.grid(row=10, column=1)

            # Etiqueta y cuadro texto Soluble Cuerpos
            soluble = StringVar()
            solubleoptions = ["", "Soluble", "Cuerpos"]
            soluble.set(solubleoptions[0])
            solublelabel = Label(textframe, text="Estado de la proteína")
            solublelabel.grid(row=11, column=0, sticky=W)
            solubletext = OptionMenu(textframe, soluble, *solubleoptions)
            solubletext.grid(row=11, column=1)

            # Etiqueta y cuadro texto Protocolo purificación
            protocolpurification = StringVar()
            protocolpurificationlabel = Label(
                textframe, text="Protocolo purificación")
            protocolpurificationlabel.grid(row=12, column=0, sticky=W)
            protocolpurificationtext = Entry(
                textframe, textvariable=protocolpurification)
            protocolpurificationtext.grid(row=12, column=1)

            # Etiqueta y cuadro texto Protocolo purificación
            protocolreplegament = StringVar()
            protocolreplegamentlabel = Label(
                textframe, text="Protocolo repliegue")
            protocolreplegamentlabel.grid(row=13, column=0, sticky=W)
            protocolreplegamenttext = Entry(
                textframe, textvariable=protocolreplegament)
            protocolreplegamenttext.grid(row=13, column=1)

            # Etiquetas y cuadro texto Tamaño
            aa = StringVar()
            aalabel = Label(textframe, text="Tamaño", padx=10)
            aalabel.grid(row=1, column=4, sticky=W)
            aatext = Entry(textframe, textvariable=aa)
            aatext.grid(row=1, column=5, columnspan=10)
            aalabel = Label(textframe, text="aa")
            aalabel.grid(row=1, column=15)

            # Etiquetas y cuadro texto Peso Molecular
            mw = StringVar()
            mwlabel = Label(textframe, text="Peso Molecular", padx=10)
            mwlabel.grid(row=2, column=4, sticky=W)
            mwtext = Entry(textframe, textvariable=mw)
            mwtext.grid(row=2, column=5, columnspan=10)
            mwunitlabel = Label(textframe, text="kDa")
            mwunitlabel.grid(row=2, column=15)

            # Etiquetas y cuadro texto Temperatura expresión
            temperatureexpression = StringVar()
            temperatureexpressionlabel = Label(
                textframe, text="Temperatura óptima de expresión", padx=10)
            temperatureexpressionlabel.grid(row=3, column=4, sticky=W)
            temperatureexpressiontext = Entry(
                textframe, textvariable=temperatureexpression)
            temperatureexpressiontext.grid(row=3, column=5, columnspan=10)
            temperatureexpressionunitlabel = Label(textframe, text="°C")
            temperatureexpressionunitlabel.grid(row=3, column=15)

            # Etiquetas y cuadro texto Temperatura actividad
            temperatureactivity = StringVar()
            temperatureactivitylabel = Label(
                textframe, text="Temperatura óptima de actividad", padx=10)
            temperatureactivitylabel.grid(row=4, column=4, sticky=W)
            temperatureactivitytext = Entry(
                textframe, textvariable=temperatureactivity)
            temperatureactivitytext.grid(row=4, column=5, columnspan=10)
            temperatureactivityunitlabel = Label(textframe, text="°C")
            temperatureactivityunitlabel.grid(row=4, column=15)

            # Etiquetas y cuadro texto Punto Isoelectrico
            pi = StringVar()
            pilabel = Label(textframe, text="Punto isoelectrico", padx=10)
            pilabel.grid(row=5, column=4, sticky=W)
            pitext = Entry(textframe, textvariable=pi)
            pitext.grid(row=5, column=5, columnspan=10)
            piunitlabel = Label(textframe, text="pH")
            piunitlabel.grid(row=5, column=15)

            # Etiquetas y cuadro texto Concentración IPTG
            iptg = StringVar()
            iptglabel = Label(
                textframe, text="Concentración final IPTG", padx=10)
            iptglabel.grid(row=6, column=4, sticky=W)
            iptgtext = Entry(textframe, textvariable=iptg)
            iptgtext.grid(row=6, column=5, columnspan=10)
            iptgunitlabel = Label(textframe, text="mM")
            iptgunitlabel.grid(row=6, column=15)

            # Etiquetas y cuadro texto Coefficient
            coefficient = StringVar()
            coefficientlabel = Label(
                textframe, text="Coeficiente de extinción molar", padx=10)
            coefficientlabel.grid(row=7, column=4, sticky=W)
            coefficienttext = Entry(textframe, textvariable=coefficient)
            coefficienttext.grid(row=7, column=5, columnspan=10)
            coefficientunitlabel = Label(textframe, text="L/(mol*cm)")
            coefficientunitlabel.grid(row=7, column=15)

            # Etiquetas y cuadro texto Tiempo de expresión
            timeexpression = StringVar()
            timeexpressionlabel = Label(
                textframe, text="Tiempo óptimo de expresión", padx=10)
            timeexpressionlabel.grid(row=8, column=4, sticky=W)
            timeexpressiontext = Entry(textframe, textvariable=timeexpression)
            timeexpressiontext.grid(row=8, column=5, columnspan=10)
            timeexpressionunitlabel = Label(textframe, text="h")
            timeexpressionunitlabel.grid(row=8, column=15)

            # Etiquetas y cuadro texto Km
            km = StringVar()
            kmunit = StringVar()
            kmerror = StringVar()
            kmlabel = Label(textframe, text="Km", padx=10)
            kmlabel.grid(row=9, column=4, sticky=W)
            kmtext = Entry(textframe, textvariable=km)
            kmtext.grid(row=9, column=5, columnspan=10)
            kmunittext = Entry(textframe, textvariable=kmunit, width=7)
            kmunittext.grid(row=9, column=15)
            kmerrortext = Entry(textframe, textvariable=kmerror, width=7)
            kmerrortext.grid(row=9, column=16)

            # Etiquetas y cuadro texto Kcat
            kcat = StringVar()
            kcatunit = StringVar()
            kcaterror = StringVar()
            kcatlabel = Label(textframe, text="Kcat", padx=10)
            kcatlabel.grid(row=10, column=4, sticky=W)
            kcattext = Entry(textframe, textvariable=kcat)
            kcattext.grid(row=10, column=5, columnspan=10)
            kcatunittext = Entry(textframe, textvariable=kcatunit, width=7)
            kcatunittext.grid(row=10, column=15)
            kcaterrortext = Entry(textframe, textvariable=kcaterror, width=7)
            kcaterrortext.grid(row=10, column=16)

            # Etiquetas y cuadro texto Km/Kcat
            kmkcat = StringVar()
            kmkcatunit = StringVar()
            kmkcaterror = StringVar()
            kmkcatlabel = Label(textframe, text="Km/Kcat", padx=10)
            kmkcatlabel.grid(row=11, column=4, sticky=W)
            kmkcattext = Entry(textframe, textvariable=kmkcat)
            kmkcattext.grid(row=11, column=5, columnspan=10)
            kmkcatnittext = Entry(textframe, textvariable=kmkcatunit, width=7)
            kmkcatnittext.grid(row=11, column=15)
            kmkcaterrortext = Entry(
                textframe, textvariable=kmkcaterror, width=7)
            kmkcaterrortext.grid(row=11, column=16)

            # Etiqueta y cuadro de texto Secuencia DNA
            seqdnalabel = Label(textframe, text="Secuencia DNA", padx=10)
            seqdnalabel.grid(row=12, column=4, sticky=W)
            seqdnatext = Text(textframe, width=26, height=8)
            seqdnatext.grid(row=12, column=5, sticky=W, columnspan=9)
            scrollseqdna = Scrollbar(textframe, command=seqdnatext.yview)
            scrollseqdna.grid(row=12, column=14, sticky=NSEW)
            seqdnatext.config(yscrollcommand=scrollseqdna.set)

            # Etiqueta y cuadro de texto Secuencia AA
            seqaalabel = Label(
                textframe, text="Secuencia aminoácidos", padx=10)
            seqaalabel.grid(row=13, column=4, sticky=W)
            seqaatext = Text(textframe, width=26, height=8)
            seqaatext.grid(row=13, column=5, sticky=W, columnspan=9)
            scrollseqaa = Scrollbar(textframe, command=seqaatext.yview)
            scrollseqaa.grid(row=13, column=14, sticky=NSEW)
            seqaatext.config(yscrollcommand=scrollseqaa.set)

            # Etiqueta y cuadro de texto Comentarios
            commentslabel = Label(textframe, text="Comentarios", padx=10)
            commentslabel.grid(row=14, column=4, sticky=W, rowspan=2)
            commentstext = Text(textframe, width=26, height=8)
            commentstext.grid(row=14, column=5, sticky=W,
                              columnspan=9, rowspan=2)
            scrollcomments = Scrollbar(textframe, command=commentstext.yview)
            scrollcomments.grid(row=14, column=14, sticky=NSEW, rowspan=2)
            commentstext.config(yscrollcommand=scrollcomments.set)

            # Botón Crear instancia
            createbutton = Button(bottomframe, text="Crear", width=15, command=lambda: CreateData(name.get(), microrganism.get(), type.get(), vector.get(), ph.get(), activity.get(), substrate.get(), adjustmenttype.get(), intraextracellular.get(), soluble.get(), protocolpurification.get(), protocolreplegament.get(), aa.get(), mw.get(), temperatureexpression.get(
            ), temperatureactivity.get(), pi.get(), iptg.get(), coefficient.get(), timeexpression.get(), km.get(), kmunit.get(), kmerror.get(), kcat.get(), kcatunit.get(), kcaterror.get(), kmkcat.get(), kmkcatunit.get(), kmkcaterror.get(), seqdnatext.get(1.0, END).rstrip("\n"), seqaatext.get(1.0, END).rstrip("\n"), commentstext.get("1.0", END).rstrip("\n"), idtext))
            createbutton.grid(row=0, column=0, padx=2)

            # Botón borrar campos
            erasecampbutton = Button(
                bottomframe, text="Borrar campos", width=15, command=lambda: EraseData())
            erasecampbutton.grid(row=0, column=1, padx=2)

            """Menubar of root"""
            Menubar = Menu(createwindow)
            createwindow.config(menu=Menubar, width=300, height=300)

            # BBDD Menu
            BBDDMenu = Menu(Menubar, tearoff=0)
            Menubar.add_cascade(label="BBDD", menu=BBDDMenu)
            BBDDMenu.add_command(label="Salir", command=lambda: CloseApp(root))

            # Action Menu
            actionmenu = Menu(Menubar, tearoff=0)
            Menubar.add_cascade(label="Action", menu=actionmenu)
            actionmenu.add_command(label="Crear", command=lambda: CreateData(name.get(), microrganism.get(), type.get(), vector.get(), ph.get(), activity.get(), substrate.get(), adjustmenttype.get(), intraextracellular.get(), soluble.get(), protocolpurification.get(), protocolreplegament.get(), aa.get(), mw.get(), temperatureexpression.get(
            ), temperatureactivity.get(), pi.get(), iptg.get(), coefficient.get(), timeexpression.get(), km.get(), kmunit.get(), kmerror.get(), kcat.get(), kcatunit.get(), kcaterror.get(), kmkcat.get(), kmkcatunit.get(), kmkcaterror.get(), seqdnatext.get(1.0, END).rstrip("\n"), seqaatext.get(1.0, END).rstrip("\n"), commentstext.get("1.0", END).rstrip("\n"), idtext))
            actionmenu.add_command(label="Borrar campos",
                                   command=lambda: EraseData())

            createwindow.mainloop()
            break

        except sqlite3.OperationalError:
            createwindow.destroy()
            messagebox.showerror("ERROR", "Cree primero la BBDD")
            break
