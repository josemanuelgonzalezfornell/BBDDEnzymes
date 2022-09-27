def connectToBBDD(): #crear base de datos y tabla. *Arreglar la creación de conexión duplicada y de tabla duplicada
	import sqlite3
	from tkinter import messagebox
	while True:
		try:
			conection=sqlite3.connect("BBDDEnzyme")
			myCursor=conection.cursor()
			myCursor.execute("CREATE TABLE ENZYMES (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_ENZIMA VARCHAR(40), MICROORGANISMO_PROCEDENCIA VARCHAR(50), TIPO_ENZYMA VARCHAR(50), VECTOR VARCHAR(50), pH_OPTIMO FLOAT, TEMPERATURA_OPTIMA_EXPRESION FLOAT, CONCENTRACION_IPTG_mM FLOAT, TIEMPO_EXPRESION_h FLOAT, INTRACELULAR_EXTRACELULAR VARCHAR(50), SOLUBLE_CUERPOS VARCHAR(50), TAMAÑO FLOAT, TEMPERATURA_OPTIMA_ACTIVIDAD FLOAT, COEF_EXTINCION_MOLAR FLOAT, ACTIVIDAD VARCHAR(50), SUSTRATO_ESPECIFICO VARCHAR(50), Km FLOAT, UNIDAD_Km VARCHAR(50), ERROR_ESTANDAR_Km FLOAT, Kcat FLOAT, UNIDAD_Kcat VARCHAR(50), ERROR_ESTANDAR_Kcat FLOAT, KmKcat FLOAT, UNIDAD_KmKcat Varchar(50), ERROR_ESTANDAR_KmKcat FLOAT, TIPO_AJUSTE_CINETICO VARCHAR(50), PROTOCOLO_PURIFICACION VARCHAR(50), PROTOCOLO_REPLIEGUE VARCHAR(50), SECUENCIA_DNA LONGTEXT, SECUENCIA_AA LONGTEXT, COMENTARIOS LONGTEXT)")
			conection.commit()            
			myCursor.close()
			conection.close()
			messagebox.showinfo("Conexión establecida", "¡BBDD creada con éxito!")
			break
		except sqlite3.OperationalError:
			messagebox.showinfo("ERROR","¡La base de datos ya está creada!")
			break

def CreateData(name, microrganism, type, vector, pH, temperatureexpression, iptg, timeexpression, intraextracellular, soluble, mw, temperatureactivity, coefficient, activity, substrate, km, unitkm, kmerror, kcat, unitkcat, kcaterror, kmkcat, unitkmkcat, kmkcaterror, adjustmenttype, protocolpurification, protocolreplegament, seqdna, seqaa, comments):   #Añadir una instancia en la base de datos
	import sqlite3
	from tkinter import messagebox
	data=[str(name), str(microrganism), str(type), str(vector), pH, temperatureexpression, iptg, timeexpression, str(intraextracellular), str(soluble), mw, temperatureactivity, coefficient, str(activity), str(substrate), km, str(unitkm), kmerror, kcat, str(unitkcat), kcaterror, kmkcat, str(unitkmkcat), kmkcaterror, str(adjustmenttype), str(protocolpurification), str(protocolreplegament), str(seqdna), str(seqaa), str(comments)]
	conection=sqlite3.connect("BBDDEnzyme")
	myCursor=conection.cursor()
	myCursor.execute("INSERT INTO ENZYMES VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (data))
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
	if functiontype=="microrganism":
		myCursor.execute("SELECT * FROM 'ENZYMES' WHERE 'MICROORGANISMO_PROCEDENCIA'='"+ str(infogiven)+"'")
	if functiontype=="type":
		myCursor.execute("SELECT * FROM `ENZYMES` WHERE `TIPO_ENZYMA`='"+ str(infogiven)+"'")
	if functiontype=="vector":
		myCursor.execute("SELECT * FROM `ENZYMES` WHERE `VECTOR`='"+ str(infogiven)+"'")
	if functiontype=="pH":
		myCursor.execute("SELECT * FROM `ENZYMES` WHERE `pH_OPTIMO`='"+ str(infogiven)+"'")
	if functiontype=="temperatureexpression":
		myCursor.execute("SELECT * FROM 'ENZYMES' WHERE 'TEMPERATURA_OPTIMA_EXPRESION'='"+ str(infogiven)+"'")
	if functiontype=="iptg":
		myCursor.execute("SELECT * FROM 'ENZYMES' WHERE 'CONCENTRACION_IPTG_mM'='"+ str(infogiven)+"'")
	if functiontype=="timeexpression":
		myCursor.execute("SELECT * FROM 'ENZYMES' WHERE 'TIEMPO_EXPRESION_h'='"+ str(infogiven)+"'")
	if functiontype=="intraextracellular":
		myCursor.execute("SELECT * FROM 'ENZYMES' WHERE 'INTRACELULAR_EXTRACELULAR'='"+ str(infogiven)+"'")
	if functiontype=="soluble":
		myCursor.execute("SELECT * FROM 'ENZYMES' WHERE 'SOLUBLE_CUERPOS'='"+ str(infogiven)+"'")
	if functiontype=="mw":
		myCursor.execute("SELECT * FROM 'ENZYMES' WHERE 'TAMAÑO'='"+ str(infogiven)+"'")
	if functiontype=="temperatureactivity":
		myCursor.execute("SELECT * FROM 'ENZYMES' WHERE 'TEMPERATURA_OPTIMA_ACTIVIDAD'='"+ str(infogiven)+"'")
	if functiontype=="coefficient":
		myCursor.execute("SELECT * FROM `ENZYMES` WHERE `COEF_EXTINCION_MOLAR`='"+ str(infogiven)+"'")
	if functiontype=="activity":
		myCursor.execute("SELECT * FROM `ENZYMES` WHERE `ACTIVIDAD`='"+ str(infogiven)+"'")
	if functiontype=="substrate":
		myCursor.execute("SELECT * FROM `ENZYMES` WHERE `SUSTRATO_ESPECIFICO`='"+ str(infogiven)+"'")
	if functiontype=="km":
		myCursor.execute("SELECT * FROM 'ENZYMES' WHERE 'Km'='"+ str(infogiven)+"'")
	if functiontype=="kcat":
		myCursor.execute("SELECT * FROM 'ENZYMES' WHERE 'Kcat'='"+ str(infogiven)+"'")
	if functiontype=="kmkcat":
		myCursor.execute("SELECT * FROM 'ENZYMES' WHERE 'KmKcat'='"+ str(infogiven)+"'")
	if functiontype=="adjustmenttype":
		myCursor.execute("SELECT * FROM 'ENZYMES' WHERE 'TIPO_AJUSTE_CINETICO'='"+ str(infogiven)+"'")
	if functiontype=="protocolpurification":
		myCursor.execute("SELECT * FROM 'ENZYMES' WHERE 'PROTOCOLO_PURIFICACION'='"+ str(infogiven)+"'")
	if functiontype=="protocolreplegament":
		myCursor.execute("SELECT * FROM 'ENZYMES' WHERE 'PROTOCOLO_REPLIEGUE'='"+ str(infogiven)+"'")
	if functiontype=="seqdna":
		myCursor.execute("SELECT * FROM 'ENZYMES' WHERE 'SECUENCIA_DNA'='"+ str(infogiven)+"'")
	if functiontype=="seqaa":
		myCursor.execute("SELECT * FROM 'ENZYMES' WHERE 'SECUENCIA_AA'='"+ str(infogiven)+"'")
	if functiontype=="comments":
		myCursor.execute("SELECT * FROM 'ENZYMES' WHERE 'COMENTARIOS'='"+ str(infogiven)+"'")
	data=myCursor.fetchall()
	myCursor.close()
	conection.close()
	return(data)

def ModifyData(id, name, microrganism, type, vector, pH, temperatureexpression, iptg, timeexpression, intraextracellular, soluble, mw, temperatureactivity, coefficient, activity, substrate, km, unitkm, kmerror, kcat, unitkcat, kcaterror, kmkcat, unitkmkcat, kmkcaterror, adjustmenttype, protocolpurification, protocolreplegament, seqdna, seqaa, comments): #Modificar datos de una instancia
	import sqlite3
	from tkinter import messagebox
	data=[str(name), str(microrganism), str(type), str(vector), pH, temperatureexpression, iptg, timeexpression, str(intraextracellular), str(soluble), mw, temperatureactivity, coefficient, str(activity), str(substrate), km, str(unitkm), kmerror, kcat, str(unitkcat), kcaterror, kmkcat, str(unitkmkcat), kmkcaterror, str(adjustmenttype), str(protocolpurification), str(protocolreplegament), str(seqdna), str(seqaa), str(comments), id]
	conection=sqlite3.connect("BBDDEnzyme")
	myCursor=conection.cursor()
	myCursor.execute("UPDATE ENZYMES SET 'NOMBRE_ENZIMA'=(?), 'MICROORGANISMO_PROCEDENCIA'=(?), 'TIPO_ENZYMA'=(?), 'VECTOR'=(?), 'pH_OPTIMO'=(?), 'TEMPERATURA_OPTIMA_EXPRESION'=(?), 'CONCENTRACION_IPTG_mM'=(?), 'TIEMPO_EXPRESION_h'=(?), 'INTRACELULAR_EXTRACELULAR'=(?), 'SOLUBLE_CUERPOS'=(?), 'TAMAÑO'=(?), 'TEMPERATURA_OPTIMA_ACTIVIDAD'=(?), 'COEF_EXTINCION_MOLAR'=(?), 'ACTIVIDAD'=(?), 'SUSTRATO_ESPECIFICO'=(?), 'Km'=(?), 'UNIDAD_Km'=(?), 'ERROR_ESTANDAR_Km'=(?), 'Kcat'=(?), 'UNIDAD_Kcat'=(?), 'ERROR_ESTANDAR_Kcat'=(?), 'KmKcat'=(?), 'UNIDAD_KmKcat'=(?), 'ERROR_ESTANDAR_KmKcat'=(?), 'TIPO_AJUSTE_CINETICO'=(?), 'PROTOCOLO_PURIFICACION'=(?), 'PROTOCOLO_REPLIEGUE'=(?), 'SECUENCIA_DNA'=(?), 'SECUENCIA_AA'=(?), 'COMENTARIOS'=(?) WHERE ID=(?)", (data))
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
