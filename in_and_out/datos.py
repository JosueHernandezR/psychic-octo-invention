#!/usr/bin/env python
 
import serial
import MySQLdb
 #identificador del puerto, esto varia entre linux y windows para la RaspBerry
RB = serial.Serial('/dev/ttyACM0',9600)

print (RB.readline())
print (RB.readline())
while True:
    getSerialValue= RB.readline()   
    #Conección de MySQL en python
    db = MySQLdb.connect("localhost","root","password","RB")
    #SI la cadena no esta vacia procede a hacer los registros en la base de datos.
    if getSerialValue != '\n':
        try:
            #Se quita el terminador de cadena para evitar errores
            B = getSerialValue.decode('utf-8').rstrip('\n')
            #Se quitan las comas que tiene el string(json=)
            c = B.split(" ")
            #Para evitar hacer for hay que tomar en cuenta cuantos valores nos esta dando la RaspBerry, dependiendo la cantidad se hace lo siguiente:
            #Convertimos los valores que necesitamos y los asignamos en una variable, lo que hemos obtenido anteriormente son listas, entonces de acuerdo a su posicion obtenemos esos datos y los parseamos en este caso a formato float
            vol = float(c[0])
            #Si se requiere asignar mas datos se continua como lo que vemos a continuación
            #n = float(c[n])
            #Supongo que la raspberry va a mandar la intensidad de corriente
            Amp = float(c[1])
            Pot = vol*Amp
            #Se agregaran a la base de datos
            curs = db.cursor()
            #De nuevo se tiene que parsear los datos a formato string pero con el formato de un float para agregarlos a la base de datos.
            curs.execute("INSERT INTO temps(fecha,vol,pot)values(now(),"+str(vol)+","+str(Pot)+")")
            db.commit()
        except ValueError:
            print ("Datos erroneos")
 
 
RB.close()