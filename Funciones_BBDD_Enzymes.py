from tkinter import *
from BBDD_Enzymes_Show_Searched import *
from tkinter import filedialog
from tkinter import messagebox
from os import remove
from io import *
import csv
from sqlite3 import *

# Crea un archivo de texto que almacena la ubicación de la base de datos a abrir


def saveBBDDLocation(location):
    bbddlocation = open("BBDDLocation.txt", 'w')
    bbddlocation.write(location)
    bbddlocation.close()

# Lee la información del archivo de texto donde se almacena la bbdd abierta y lo devuelve


def readBBDDLocation():
    bbddlocation = open("BBDDLocation.txt", 'r')
    data = str(bbddlocation.read())
    bbddlocation.close()
    return data

# crea una base de datos, aunque sin ninguna tabla, solo el archivo


def createBBDD():
    ubication = filedialog.asksaveasfile(title="Crear", initialdir="/")
    if ubication:
        messagebox.showinfo("BBDD creada", "La base de datos ha sido creada")
    else:
        None

# Conecta con una bbdd y crea una tabla dentro


def connectToBBDD():
    ubication = filedialog.askopenfilename(title="Abrir", initialdir="/")
    saveBBDDLocation(str(ubication))
    try:
        if ubication:
            conection = sqlite3.connect(str(readBBDDLocation()))
            myCursor = conection.cursor()
            try:
                myCursor.execute("CREATE TABLE ENZYMES (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_ENZIMA VARCHAR(40), MICROORGANISMO_PROCEDENCIA VARCHAR(50), TIPO_ENZYMA VARCHAR(50), VECTOR VARCHAR(50), pH_OPTIMO FLOAT, ACTIVIDAD VARCHAR(50), SUSTRATO_ESPECIFICO VARCHAR(50), TIPO_AJUSTE_CINETICO VARCHAR(50), INTRACELULAR_EXTRACELULAR VARCHAR(50), SOLUBLE_CUERPOS VARCHAR(50), PROTOCOLO_PURIFICACION VARCHAR(50), PROTOCOLO_REPLIEGUE VARCHAR(50), TAMAÑO FLOAT, PESO_MOLECULAR FLOAT, TEMPERATURA_OPTIMA_EXPRESION FLOAT, TEMPERATURA_OPTIMA_ACTIVIDAD FLOAT, PUNTO_ISOELECTRICO FLOAT, CONCENTRACION_IPTG_mM FLOAT, COEF_EXTINCION_MOLAR FLOAT, TIEMPO_EXPRESION_h FLOAT, Km FLOAT, UNIDAD_Km VARCHAR(50), ERROR_ESTANDAR_Km FLOAT, Kcat FLOAT, UNIDAD_Kcat VARCHAR(50), ERROR_ESTANDAR_Kcat FLOAT, KmKcat FLOAT, UNIDAD_KmKcat Varchar(50), ERROR_ESTANDAR_KmKcat FLOAT, SECUENCIA_DNA LONGTEXT, SECUENCIA_AA LONGTEXT, COMENTARIOS LONGTEXT)")
                conection.commit()
                myCursor.close()
                conection.close()
                messagebox.showinfo("Conexión establecida",
                                    "¡BBDD conectada con éxito!")
            except sqlite3.OperationalError:
                conection.commit()
                myCursor.close()
                conection.close()
                messagebox.showinfo("Conexión establecida",
                                    "¡BBDD conectada con éxito!")
        else:
            None

    except sqlite3.OperationalError:
        messagebox.showinfo("ERROR", "¡Cree primero la BBDD!")

# Función para obtener el ID a realizar


def obtainNewID():
    conection = sqlite3.connect(readBBDDLocation())
    myCursor = conection.cursor()
    myCursor.execute("SELECT Max(seq) from sqlite_sequence")
    data = myCursor.fetchall()
    conection.commit()
    myCursor.close()
    conection.close()
    if data[0][0] == None:
        return "1"
    else:
        return str(data[0][0]+1)

# Añadir una instancia en la base de datos


def CreateData(name, microrganism, type, vector, pH, activity, substrate, adjustmenttype, intraextracellular, soluble, protocolpurification, protocolreplegament, aa, mw, temperatureexpression, temperatureactivity, pi, iptg, coefficient, timeexpression, km, unitkm, kmerror, kcat, unitkcat, kcaterror, kmkcat, unitkmkcat, kmkcaterror, seqdna, seqaa, comments, idtext):
    data = [str(name), str(microrganism), str(type), str(vector), pH, str(activity), str(substrate), str(adjustmenttype), str(intraextracellular), str(soluble), str(protocolpurification), str(protocolreplegament), aa, mw,
            temperatureexpression, temperatureactivity, pi, iptg, coefficient, timeexpression, km, str(unitkm), kmerror, kcat, str(unitkcat), kcaterror, kmkcat, str(unitkmkcat), kmkcaterror, str(seqdna), str(seqaa), str(comments)]
    conection = sqlite3.connect(readBBDDLocation())
    myCursor = conection.cursor()
    myCursor.execute(
        "INSERT INTO ENZYMES VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (data))
    conection.commit()
    myCursor.close()
    conection.close()
    messagebox.showinfo("Éxito", "Instancia creada en la tabla Enzymes")
    idtext.config(text=obtainNewID())

# Busca instancias en la base de datos que coincidan con los datos aportados


def searchInstance(id, name, microrganism, type, vector, ph, activity, substrate, adjustmenttype, intraextracellular, soluble, protocolpurification, protocolreplegament, aa, mw, temperatureexpression, temperatureactivity, pi, iptg, coefficient, timeexpression, km, kmunit, kmerror, kcat, kcatunit, kcaterror, kmkcat, kmkcatunit, kmkcaterror, seqdnatext, seqaatext, commentstext, root):
    input = []
    data = []
    if id.get() != "":
        input.append("ID=(?)")
        data.append(id.get())
    if name.get() != "":
        input.append("NOMBRE_ENZIMA=(?)")
        data.append(str(name.get()))
    if microrganism.get() != "":
        input.append("MICROORGANISMO_PROCEDENCIA=(?)")
        data.append(str(microrganism.get()))
    if type.get() != "":
        input.append("TIPO_ENZYMA=(?)")
        data.append(str(type.get()))
    if vector.get() != "":
        input.append("VECTOR=(?)")
        data.append(str(vector.get()))
    if ph.get() != "":
        input.append("pH_OPTIMO=(?)")
        data.append(str(ph.get()))
    if activity.get() != "":
        input.append("ACTIVIDAD=(?)")
        data.append(str(activity.get()))
    if substrate.get() != "":
        input.append("SUSTRATO_ESPECIFICO=(?)")
        data.append(str(substrate.get()))
    if adjustmenttype.get() != "":
        input.append("TIPO_AJUSTE_CINETICO=(?)")
        data.append(str(adjustmenttype.get()))
    if intraextracellular.get() != "":
        input.append("INTRACELULAR_EXTRACELULAR=(?)")
        data.append(str(intraextracellular.get()))
    if soluble.get() != "":
        input.append("SOLUBLE_CUERPOS=(?)")
        data.append(str(soluble.get()))
    if protocolpurification.get() != "":
        input.append("PROTOCOLO_PURIFICACION=(?)")
        data.append(str(protocolpurification.get()))
    if protocolreplegament.get() != "":
        input.append("PROTOCOLO_REPLIEGUE=(?)")
        data.append(str(protocolreplegament.get()))
    if aa.get() != "":
        input.append("TAMAÑO=(?)")
        data.append(str(aa.get()))
    if mw.get() != "":
        input.append("PESO_MOLECULAR=(?)")
        data.append(str(mw.get()))
    if temperatureexpression.get() != "":
        input.append("TEMPERATURA_OPTIMA_EXPRESION=(?)")
        data.append(str(temperatureexpression.get()))
    if temperatureactivity.get() != "":
        input.append("TEMPERATURA_OPTIMA_ACTIVIDAD=(?)")
        data.append(str(temperatureactivity.get()))
    if pi.get() != "":
        input.append("PUNTO_ISOELECTRICO=(?)")
        data.append(str(pi.get()))
    if iptg.get() != "":
        input.append("CONCENTRACION_IPTG_mM=(?)")
        data.append(str(iptg.get()))
    if coefficient.get() != "":
        input.append("COEF_EXTINCION_MOLAR=(?)")
        data.append(str(coefficient.get()))
    if timeexpression.get() != "":
        input.append("TIEMPO_EXPRESION_h=(?)")
        data.append(str(timeexpression.get()))
    if km.get() != "":
        input.append("Km=(?)")
        data.append(str(km.get()))
    if kmunit.get() != "":
        input.append("UNIDAD_Km=(?)")
        data.append(str(kmunit.get()))
    if kmerror.get() != "":
        input.append("'ERROR_ESTANDAR_Km'=(?)")
        data.append(str(kmerror.get()))
    if kcat.get() != "":
        input.append("'Kcat'=(?)")
        data.append(str(kcat.get()))
    if kcatunit.get() != "":
        input.append("'UNIDAD_Kcat'=(?)")
        data.append(str(kcatunit.get()))
    if kcaterror.get() != "":
        input.append("ERROR_ESTANDAR_Kcat=(?)")
        data.append(str(kcaterror.get()))
    if kmkcat.get() != "":
        input.append("KmKcat=(?)")
        data.append(str(kmkcat.get()))
    if kmkcatunit.get() != "":
        input.append("UNIDAD_KmKcat=(?)")
        data.append(str(kmkcatunit.get()))
    if kmkcaterror.get() != "":
        input.append("ERROR_ESTANDAR_KmKcat=(?)")
        data.append(str(kmkcaterror.get()))
    if seqdnatext.get('1.0', END).rstrip("\n") != "":
        input.append("SECUENCIA_DNA=(?)")
        data.append(str(seqdnatext.get('1.0', END).rstrip("\n")))
    if seqaatext.get('1.0', END).rstrip("\n") != "":
        input.append("SECUENCIA_AA=(?)")
        data.append(str(seqaatext.get('1.0', END).rstrip("\n")))
    if commentstext.get('1.0', END).rstrip("\n") != "":
        input.append("COMENTARIOS=(?)")
        data.append(str(commentstext.get('1.0', END).rstrip("\n")))
    conection = sqlite3.connect(readBBDDLocation())
    myCursor = conection.cursor()
    myCursor.execute("SELECT * FROM 'ENZYMES' WHERE " + str(input).replace("\"",
                                                                           "").removeprefix("[").removesuffix("]").replace("\'", "").replace(",", " AND"), data)
    output = myCursor.fetchall()
    myCursor.close()
    conection.close()
    showSearchedWindow(root, output)

# Busca instancias por ID


def searchId(id, name, microrganism, type, vector, ph, activity, substrate, adjustmenttype, intraextracellular, soluble, protocolpurification, protocolreplegament, aa, mw, temperatureexpression, temperatureactivity, pi, iptg, coefficient, timeexpression, km, kmunit, kmerror, kcat, kcatunit, kcaterror, kmkcat, kmkcatunit, kmkcaterror, seqdnatext, seqaatext, commentstext):
    conection = sqlite3.connect(readBBDDLocation())
    myCursor = conection.cursor()
    myCursor.execute("SELECT * FROM 'ENZYMES' Where ID="+id.get())
    conection.commit()
    data = myCursor.fetchall()
    myCursor.close()
    conection.close()
    name.set(str(data[0][1]))
    microrganism.set(str(data[0][2]))
    type.set(str(data[0][3]))
    vector.set(str(data[0][4]))
    ph.set(str(data[0][5]))
    activity.set(str(data[0][6]))
    substrate.set(str(data[0][7]))
    adjustmenttype.set(str(data[0][8]))
    intraextracellular.set(str(data[0][9]))
    soluble.set(str(data[0][10]))
    protocolpurification.set(str(data[0][11]))
    protocolreplegament.set(str(data[0][12]))
    aa.set(str(data[0][13]))
    mw.set(str(data[0][14]))
    temperatureexpression.set(str(data[0][15]))
    temperatureactivity.set(str(data[0][16]))
    pi.set(str(data[0][17]))
    iptg.set(str(data[0][18]))
    coefficient.set(str(data[0][19]))
    timeexpression.set(str(data[0][20]))
    km.set(str(data[0][21]))
    kmunit.set(str(data[0][22]))
    kmerror.set(str(data[0][23]))
    kcat.set(str(data[0][24]))
    kcatunit.set(str(data[0][25]))
    kcaterror.set(str(data[0][26]))
    kmkcat.set(str(data[0][27]))
    kmkcatunit.set(str(data[0][28]))
    kmkcaterror.set(str(data[0][29]))
    seqdnatext.insert('1.0', str(data[0][30]))
    seqaatext.insert('1.0', str(data[0][31]))
    commentstext.insert('1.0', str(data[0][32]))

# Modificar datos de una instancia


def ModifyData(id, name, microrganism, type, vector, pH, activity, substrate, adjustmenttype, intraextracellular, soluble, protocolpurification, protocolreplegament, aa, mw, temperatureexpression, temperatureactivity, pi, iptg, coefficient, timeexpression, km, unitkm, kmerror, kcat, unitkcat, kcaterror, kmkcat, unitkmkcat, kmkcaterror, seqdna, seqaa, comments):
    data = [str(name), str(microrganism), str(type), str(vector), pH, str(activity), str(substrate), str(adjustmenttype), str(intraextracellular), str(soluble), str(protocolpurification), str(protocolreplegament), aa, mw,
            temperatureexpression, temperatureactivity, pi, iptg, coefficient, timeexpression, km, str(unitkm), kmerror, kcat, str(unitkcat), kcaterror, kmkcat, str(unitkmkcat), kmkcaterror, str(seqdna), str(seqaa), str(comments), id]
    conection = sqlite3.connect(readBBDDLocation())
    myCursor = conection.cursor()
    myCursor.execute("UPDATE ENZYMES SET 'NOMBRE_ENZIMA'=(?), 'MICROORGANISMO_PROCEDENCIA'=(?), 'TIPO_ENZYMA'=(?), 'VECTOR'=(?), 'pH_OPTIMO'=(?), 'ACTIVIDAD'=(?), 'SUSTRATO_ESPECIFICO'=(?), 'TIPO_AJUSTE_CINETICO'=(?), 'INTRACELULAR_EXTRACELULAR'=(?), 'SOLUBLE_CUERPOS'=(?), 'PROTOCOLO_PURIFICACION'=(?), 'PROTOCOLO_REPLIEGUE'=(?), 'TAMAÑO'=(?), 'PESO_MOLECULAR'=(?), 'TEMPERATURA_OPTIMA_EXPRESION'=(?), 'TEMPERATURA_OPTIMA_ACTIVIDAD'=(?), 'PUNTO_ISOELECTRICO'=(?), 'CONCENTRACION_IPTG_mM'=(?), 'COEF_EXTINCION_MOLAR'=(?), 'TIEMPO_EXPRESION_h'=(?), 'Km'=(?), 'UNIDAD_Km'=(?), 'ERROR_ESTANDAR_Km'=(?), 'Kcat'=(?), 'UNIDAD_Kcat'=(?), 'ERROR_ESTANDAR_Kcat'=(?), 'KmKcat'=(?), 'UNIDAD_KmKcat'=(?), 'ERROR_ESTANDAR_KmKcat'=(?), 'SECUENCIA_DNA'=(?), 'SECUENCIA_AA'=(?), 'COMENTARIOS'=(?) where ID=(?)", (data))
    conection.commit()
    myCursor.close()
    conection.close()
    messagebox.showinfo("Éxito", "La instancia se ha modificado con éxito")

# Eliminar datos de una instancia


def DeleteData(id, name, microrganism, type, vector, pH, activity, substrate, adjustmenttype, intraextracellular, soluble, protocolpurification, protocolreplegament, aa, mw, temperatureexpression, temperatureactivity, pi, iptg, coefficient, timeexpression, km, unitkm, kmerror, kcat, unitkcat, kcaterror, kmkcat, unitkmkcat, kmkcaterror, seqdna, seqaa, comments):
    confirmation = messagebox.askquestion(
        "Eliminar", "¿Seguro que desea eliminar permanentemente esta instancia?")
    if confirmation == "yes":
        conection = sqlite3.connect(readBBDDLocation())
        myCursor = conection.cursor()
        myCursor.execute("DELETE FROM 'ENZYMES' WHERE ID=(?)"+id.get())
        conection.commit()  # poner ventana de confirmación de eliminación
        myCursor.close()
        conection.close()
        messagebox.showinfo(
            "Éxito", "La instancia se ha eliminado correctamente")
        id.set("")
        name.set("")
        microrganism.set("")
        type.set("")
        vector.set("")
        pH.set("")
        activity.set("")
        substrate.set("")
        adjustmenttype.set("")
        intraextracellular.set("")
        soluble.set("")
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
        unitkm.set("")
        kmerror.set("")
        kcat.set("")
        unitkcat.set("")
        kcaterror.set("")
        kmkcat.set("")
        unitkmkcat.set("")
        kmkcaterror.set("")
        seqdna.delete("1.0", END)
        seqaa.delete("1.0", END)
        comments.delete("1.0", END)
    return (confirmation)

# Función para cerrar aplicación


def CloseApp(root):  # cerrar la aplicación
    confirmation = messagebox.askquestion(
        "Salir", "¿Deseas salir de la aplicación?")
    if confirmation == "yes":
        root.destroy()


# Función para exportar csv toda la base de datos
def ExportAll():
    conection = sqlite3.connect(readBBDDLocation())
    myCursor = conection.cursor()
    myCursor.execute("SELECT * FROM 'ENZYMES'")
    conection.commit()
    datatoexport = myCursor.fetchall()
    myCursor.close()
    conection.close()
    header = ["ID", "NOMBRE_ENZIMA", "MICROORGANISMO_PROCEDENCIA", "TIPO_ENZYMA", "VECTOR", "pH_OPTIMO", "ACTIVIDAD", "SUSTRATO_ESPECIFICO", "TIPO_AJUSTE_CINETICO", "INTRACELULAR_EXTRACELULAR", "SOLUBLE_CUERPOS", "PROTOCOLO_PURIFICACION", "PROTOCOLO_REPLIEGUE", "AMINOACIDOS", "PESO_MOLECULAR", "TEMPERATURA_OPTIMA_EXPRESION",
              "TEMPERATURA_OPTIMA_ACTIVIDAD", "PUNTO_ISOELECTRICO", "CONCENTRACION_IPTG_mM", "COEF_EXTINCION_MOLAR", "TIEMPO_EXPRESION_h", "Km", "UNIDAD_Km", "ERROR_ESTANDAR_Km", "Kcat", "UNIDAD_Kcat", "ERROR_ESTANDAR_Kcat", "KmKcat", "UNIDAD_KmKcat", "ERROR_ESTANDAR_KmKcat", "SECUENCIA_DNA", "SECUENCIA_AA", "COMENTARIOS"]
    savedirection = filedialog.asksaveasfile(
        title="Guardar", initialdir="/", defaultextension="*.csv")
    with open(savedirection.name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';', dialect='excel-tab')
        spamwriter.writerow(header)
        for i in datatoexport:
            spamwriter.writerow(i)

# Función para exortar csv las instancias buscadas


def ExportSearched(id, name, microrganism, type, vector, ph, activity, substrate, adjustmenttype, intraextracellular, soluble, protocolpurification, protocolreplegament, aa, mw, temperatureexpression, temperatureactivity, pi, iptg, coefficient, timeexpression, km, kmunit, kmerror, kcat, kcatunit, kcaterror, kmkcat, kmkcatunit, kmkcaterror, seqdnatext, seqaatext, commentstext, root):
    input = []
    data = []
    if id.get() != "":
        input.append("ID=(?)")
        data.append(id.get())
    if name.get() != "":
        input.append("NOMBRE_ENZIMA=(?)")
        data.append(str(name.get()))
    if microrganism.get() != "":
        input.append("MICROORGANISMO_PROCEDENCIA=(?)")
        data.append(str(microrganism.get()))
    if type.get() != "":
        input.append("TIPO_ENZYMA=(?)")
        data.append(str(type.get()))
    if vector.get() != "":
        input.append("VECTOR=(?)")
        data.append(str(vector.get()))
    if ph.get() != "":
        input.append("pH_OPTIMO=(?)")
        data.append(str(ph.get()))
    if activity.get() != "":
        input.append("ACTIVIDAD=(?)")
        data.append(str(activity.get()))
    if substrate.get() != "":
        input.append("SUSTRATO_ESPECIFICO=(?)")
        data.append(str(substrate.get()))
    if adjustmenttype.get() != "":
        input.append("TIPO_AJUSTE_CINETICO=(?)")
        data.append(str(adjustmenttype.get()))
    if intraextracellular.get() != "":
        input.append("INTRACELULAR_EXTRACELULAR=(?)")
        data.append(str(intraextracellular.get()))
    if soluble.get() != "":
        input.append("SOLUBLE_CUERPOS=(?)")
        data.append(str(soluble.get()))
    if protocolpurification.get() != "":
        input.append("PROTOCOLO_PURIFICACION=(?)")
        data.append(str(protocolpurification.get()))
    if protocolreplegament.get() != "":
        input.append("PROTOCOLO_REPLIEGUE=(?)")
        data.append(str(protocolreplegament.get()))
    if aa.get() != "":
        input.append("TAMAÑO=(?)")
        data.append(str(aa.get()))
    if mw.get() != "":
        input.append("PESO_MOLECULAR=(?)")
        data.append(str(mw.get()))
    if temperatureexpression.get() != "":
        input.append("TEMPERATURA_OPTIMA_EXPRESION=(?)")
        data.append(str(temperatureexpression.get()))
    if temperatureactivity.get() != "":
        input.append("TEMPERATURA_OPTIMA_ACTIVIDAD=(?)")
        data.append(str(temperatureactivity.get()))
    if pi.get() != "":
        input.append("PUNTO_ISOELECTRICO=(?)")
        data.append(str(pi.get()))
    if iptg.get() != "":
        input.append("CONCENTRACION_IPTG_mM=(?)")
        data.append(str(iptg.get()))
    if coefficient.get() != "":
        input.append("COEF_EXTINCION_MOLAR=(?)")
        data.append(str(coefficient.get()))
    if timeexpression.get() != "":
        input.append("TIEMPO_EXPRESION_h=(?)")
        data.append(str(timeexpression.get()))
    if km.get() != "":
        input.append("Km=(?)")
        data.append(str(km.get()))
    if kmunit.get() != "":
        input.append("UNIDAD_Km=(?)")
        data.append(str(kmunit.get()))
    if kmerror.get() != "":
        input.append("'ERROR_ESTANDAR_Km'=(?)")
        data.append(str(kmerror.get()))
    if kcat.get() != "":
        input.append("'Kcat'=(?)")
        data.append(str(kcat.get()))
    if kcatunit.get() != "":
        input.append("'UNIDAD_Kcat'=(?)")
        data.append(str(kcatunit.get()))
    if kcaterror.get() != "":
        input.append("ERROR_ESTANDAR_Kcat=(?)")
        data.append(str(kcaterror.get()))
    if kmkcat.get() != "":
        input.append("KmKcat=(?)")
        data.append(str(kmkcat.get()))
    if kmkcatunit.get() != "":
        input.append("UNIDAD_KmKcat=(?)")
        data.append(str(kmkcatunit.get()))
    if kmkcaterror.get() != "":
        input.append("ERROR_ESTANDAR_KmKcat=(?)")
        data.append(str(kmkcaterror.get()))
    if seqdnatext.get('1.0', END).rstrip("\n") != "":
        input.append("SECUENCIA_DNA=(?)")
        data.append(str(seqdnatext.get('1.0', END).rstrip("\n")))
    if seqaatext.get('1.0', END).rstrip("\n") != "":
        input.append("SECUENCIA_AA=(?)")
        data.append(str(seqaatext.get('1.0', END).rstrip("\n")))
    if commentstext.get('1.0', END).rstrip("\n") != "":
        input.append("COMENTARIOS=(?)")
        data.append(str(commentstext.get('1.0', END).rstrip("\n")))
    conection = sqlite3.connect(readBBDDLocation())
    myCursor = conection.cursor()
    myCursor.execute("SELECT * FROM 'ENZYMES' WHERE " + str(input).replace("\"",
                                                                           "").removeprefix("[").removesuffix("]").replace("\'", "").replace(",", " AND"), data)
    datatoexport = myCursor.fetchall()
    myCursor.close()
    conection.close()
    header = ["ID", "NOMBRE_ENZIMA", "MICROORGANISMO_PROCEDENCIA", "TIPO_ENZYMA", "VECTOR", "pH_OPTIMO", "ACTIVIDAD", "SUSTRATO_ESPECIFICO", "TIPO_AJUSTE_CINETICO", "INTRACELULAR_EXTRACELULAR", "SOLUBLE_CUERPOS", "PROTOCOLO_PURIFICACION", "PROTOCOLO_REPLIEGUE", "AMINOACIDOS", "PESO_MOLECULAR", "TEMPERATURA_OPTIMA_EXPRESION",
              "TEMPERATURA_OPTIMA_ACTIVIDAD", "PUNTO_ISOELECTRICO", "CONCENTRACION_IPTG_mM", "COEF_EXTINCION_MOLAR", "TIEMPO_EXPRESION_h", "Km", "UNIDAD_Km", "ERROR_ESTANDAR_Km", "Kcat", "UNIDAD_Kcat", "ERROR_ESTANDAR_Kcat", "KmKcat", "UNIDAD_KmKcat", "ERROR_ESTANDAR_KmKcat", "SECUENCIA_DNA", "SECUENCIA_AA", "COMENTARIOS"]
    savedirection = filedialog.asksaveasfile(
        title="Guardar", initialdir="/", defaultextension="*.csv")
    with open(savedirection.name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(
            csvfile, delimiter=';', dialect='excel-tab')
        spamwriter.writerow(header)
        for i in datatoexport:
            spamwriter.writerow(i)
