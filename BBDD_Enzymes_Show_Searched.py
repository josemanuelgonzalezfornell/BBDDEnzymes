from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


def showSearchedWindow(root, data):
    while True:
        try:
            searchedwindow = Toplevel(root)
            # Center the window on the screen when the program is initializated
            searchedwindow.geometry("2900x600")
            bbddframe = Frame(searchedwindow)
            bbddframe.pack()

            # Realizar tabla
            findbox = ttk.Treeview(bbddframe, column=("id", "name", "microrganism", "type", "vector", "pH", "activity", "substrate", "adjustmenttype", "intraextracellular", "soluble", "protocolpurification", "protocolreplegament", "aa", "mw", "temperatureexpression",
                                   "temperatureactivity", "pi", "iptg", "coefficient", "timeexpression", "km", "unitkm", "kmerror", "kcat", "unitkcat", "kcaterror", "kmkcat", "unitkmkcat", "kmkcaterror", "seqdna", "seqaa", "comments"), show='headings', height=50)
            scrollxfindbox = Scrollbar(
                bbddframe, orient="horizontal", command=findbox.xview)
            scrollxfindbox.pack(side='bottom', fill='x')
            findbox.config(xscrollcommand=scrollxfindbox.set)
            findbox.column("id", anchor=CENTER)
            findbox.heading("id", text="ID")
            findbox.column("name", anchor=CENTER)
            findbox.heading("name", text="Nombre enzima")
            findbox.column("microrganism", anchor=CENTER)
            findbox.heading(
                "microrganism", text="Microorganismo de procedencia")
            findbox.column("type", anchor=CENTER)
            findbox.heading("type", text="Tipo de enzima")
            findbox.column("vector", anchor=CENTER)
            findbox.heading("vector", text="Vector")
            findbox.column("pH", anchor=CENTER)
            findbox.heading("pH", text="pH óptimo de actividad")
            findbox.column("activity", anchor=CENTER)
            findbox.heading("activity", text="Tipo de actividad de la enzima")
            findbox.column("substrate", anchor=CENTER)
            findbox.heading(
                "substrate", text="Sustrato específico sobre el que actúa")
            findbox.column("adjustmenttype", anchor=CENTER)
            findbox.heading("adjustmenttype", text="Tipo de ajuste")
            findbox.column("intraextracellular", anchor=CENTER)
            findbox.heading("intraextracellular",
                            text="Localización en el cultivo")
            findbox.column("soluble", anchor=CENTER)
            findbox.heading("soluble", text="Estado de la proteína")
            findbox.column("protocolpurification", anchor=CENTER)
            findbox.heading("protocolpurification",
                            text="Protocolo purificación")
            findbox.column("protocolreplegament", anchor=CENTER)
            findbox.heading("protocolreplegament", text="Protocolo repliegue")
            findbox.column("aa", anchor=CENTER)
            findbox.heading("aa", text="Tamaño")
            findbox.column("mw", anchor=CENTER)
            findbox.heading("mw", text="Peso molecular")
            findbox.column("temperatureexpression", anchor=CENTER)
            findbox.heading("temperatureexpression",
                            text="Temperatura óptima de expresión (°C)")
            findbox.column("temperatureactivity", anchor=CENTER)
            findbox.heading("temperatureactivity",
                            text="Temperatura óptima de actividad (°C)")
            findbox.column("pi", anchor=CENTER)
            findbox.heading("pi", text="Punto isoeléctrico")
            findbox.column("iptg", anchor=CENTER)
            findbox.heading("iptg", text="Concentración final IPTG (mM)")
            findbox.column("coefficient", anchor=CENTER)
            findbox.heading(
                "coefficient", text="Coeficiente de extinción molar (L/(mol*cm))")
            findbox.column("timeexpression", anchor=CENTER)
            findbox.heading("timeexpression",
                            text="Tiempo óptimo de expresión (h)")
            findbox.column("km", anchor=CENTER)
            findbox.heading("km", text="Km")
            findbox.column("unitkm", anchor=CENTER)
            findbox.heading("unitkm", text="Unidad de la Km")
            findbox.column("kmerror", anchor=CENTER)
            findbox.heading("kmerror", text="Error estándar de la Km")
            findbox.column("kcat", anchor=CENTER)
            findbox.heading("kcat", text="Kcat")
            findbox.column("unitkcat", anchor=CENTER)
            findbox.heading("unitkcat", text="Unidad de la Kcat")
            findbox.column("kcaterror", anchor=CENTER)
            findbox.heading("kcaterror", text="Error estándar de la Kcat")
            findbox.column("kmkcat", anchor=CENTER)
            findbox.heading("kmkcat", text="Km/Kcat")
            findbox.column("unitkmkcat", anchor=CENTER)
            findbox.heading("unitkmkcat", text="Unidad de la Km/Kcat")
            findbox.column("kmkcaterror", anchor=CENTER)
            findbox.heading("kmkcaterror", text="Error estándar de la Km/Kcat")
            findbox.column("seqdna", anchor=CENTER)
            findbox.heading("seqdna", text="Secuencia DNA")
            findbox.column("seqaa", anchor=CENTER)
            findbox.heading("seqaa", text="Secuencia aminoácidos")
            findbox.column("comments", anchor=CENTER)
            findbox.heading("comments", text="Comentarios")

            for filas in data:
                findbox.insert('', 'end', values=(filas[0], filas[1], filas[2], filas[3], filas[4], filas[5], filas[6], filas[7], filas[8], filas[9], filas[10], filas[11], filas[12], filas[13], filas[14], filas[15],
                               filas[16], filas[17], filas[18], filas[19], filas[20], filas[21], filas[22], filas[23], filas[24], filas[25], filas[26], filas[27], filas[28], filas[29], filas[30], filas[31], filas[32]))

            findbox.pack()

            searchedwindow.mainloop()

        except sqlite3.OperationalError:
            searchedwindow.destroy()
            messagebox.showerror("ERROR", "Cree primero la BBDD")
            break
