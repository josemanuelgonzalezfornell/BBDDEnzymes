from ast import Return

def connectToBBDD(): #crear base de datos y tabla. *Arreglar la creación de conexión duplicada y de tabla duplicada
    import sqlite3
    from tkinter import messagebox
    while True:
        try:
            conection=sqlite3.connect("BBDDEnzyme")
            myCursor=conection.cursor()
            myCursor.execute("CREATE TABLE ENZYMES (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_ENZIMA VARCHAR(40), TIPO_ENZYMA VARCHAR(50), pH_OPTIMO FLOAT, COEF_EXTINCION_MOLAR FLOAT, ACTIVIDAD VARCHAR(50), SUSTRATO_ESPECIFICO VARCHAR(50), COMENTARIOS LONGTEXT)")
            conection.commit()            
            myCursor.close()
            conection.close()
            messagebox.showinfo("Conexión establecida", "¡BBDD creada con éxito!")
            break
        except sqlite3.OperationalError:
            messagebox.showinfo("ERROR","¡La base de datos ya está creada!")
            break

def CreateData(name, type, pH, coefficient, activity, substrate, comments):   #Añadir una instancia en la base de datos
    import sqlite3
    from tkinter import messagebox
    data=[str(name),str(type),pH,coefficient, str(activity), str(substrate), str(comments)]
    conection=sqlite3.connect("BBDDEnzyme")
    myCursor=conection.cursor()
    myCursor.execute("INSERT INTO ENZYMES VALUES(NULL,?,?,?,?,?,?,?)", (data))
    conection.commit()
    myCursor.close()
    conection.close()
    messagebox.showinfo("Éxito", "Instancia creada en la tabla Enzymes")

def ReadData(functiontype, infogiven): #Leer datos de una instancia
    import sqlite3
    conection=sqlite3.connect("BBDDEnzyme")
    myCursor=conection.cursor()
    if functiontype=="id":
        myCursor.execute("SELECT * FROM `ENZYMES` WHERE `ID`='"+ str(infogiven)+"'")
    if functiontype=="name":
        myCursor.execute("SELECT * FROM `ENZYMES` WHERE `NOMBRE_ENZIMA`='"+ str(infogiven)+"'")
    if functiontype=="type":
        myCursor.execute("SELECT * FROM `ENZYMES` WHERE `TIPO_ENZYMA`='"+ str(infogiven)+"'")
    if functiontype=="pH":
        myCursor.execute("SELECT * FROM `ENZYMES` WHERE `pH_OPTIMO`='"+ str(infogiven)+"'")
    if functiontype=="coefficient":
        myCursor.execute("SELECT * FROM `ENZYMES` WHERE `COEF_EXTINCION_MOLAR`='"+ str(infogiven)+"'")
    if functiontype=="activity":
        myCursor.execute("SELECT * FROM `ENZYMES` WHERE `ACTIVIDAD`='"+ str(infogiven)+"'")
    if functiontype=="substrate":
        myCursor.execute("SELECT * FROM `ENZYMES` WHERE `SUSTRATO_ESPECIFICO`='"+ str(infogiven)+"'")
    if functiontype=="comments":
        myCursor.execute("SELECT * FROM 'ENZYMES' WHERE 'COMENTARIOS'='"+ str(infogiven)+"'")
    data=myCursor.fetchall()
    myCursor.close()
    conection.close()
    return(data)

def ModifyData(id, name, type, pH, coefficient, activity, substrate, comments): #Modificar datos de una instancia
    import sqlite3
    from tkinter import messagebox
    data=[str(name),str(type),pH,coefficient, str(activity), str(substrate), str(comments), id]
    conection=sqlite3.connect("BBDDEnzyme")
    myCursor=conection.cursor()
    myCursor.execute("UPDATE ENZYMES SET 'NOMBRE_ENZIMA'=(?), `TIPO_ENZYMA`=(?), `pH_OPTIMO`=(?), `COEF_EXTINCION_MOLAR`=(?), `ACTIVIDAD`=(?), `SUSTRATO_ESPECIFICO`=(?), 'COMENTARIOS'=(?) WHERE ID=(?)", (data))
    conection.commit()
    myCursor.close()
    conection.close()
    messagebox.showinfo("Éxito", "La instancia se ha modificado con éxito")

def DeleteData(id): #Eliminar datos de una instancia
    import sqlite3
    from tkinter import messagebox
    confirmation=messagebox.askquestion("Eliminar", "¿Seguro que desea eliminar permanentemente esta instancia?")
    if confirmation=="yes":
        conection=sqlite3.connect("BBDDEnzyme")
        myCursor=conection.cursor()
        myCursor.execute("DELETE FROM 'ENZYMES' WHERE ID=(?)", (id))
        conection.commit() #poner ventana de confirmación de eliminación
        myCursor.close()
        conection.close()
        messagebox.showinfo("Éxito","La instancia se ha eliminado correctamente")
    return (confirmation)

#Función para cerrar aplicación
def CloseApp(root): #cerrar la aplicación
    from tkinter import messagebox
    confirmation=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
    if confirmation=="yes":
        root.destroy()
