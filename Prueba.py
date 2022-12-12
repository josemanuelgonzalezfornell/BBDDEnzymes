from Funciones_BBDD_Enzymes import *


typeoptions=[""]
conection = sqlite3.connect(readBBDDLocation())
myCursor = conection.cursor()
myCursor.execute("SELECT TIPO_ENZYMA FROM ENZYMES group by TIPO_ENZYMA")
diferenttypes= myCursor.fetchall()
for i in diferenttypes:
    typeoptions.append(i[0])
conection.commit()
myCursor.close()
conection.close()
print(typeoptions)