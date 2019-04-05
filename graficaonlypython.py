import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import re
import threading

gData = []
gData.append([0])
gData.append([0])

#Configuramos la gráfica
fig = plt.figure()
ax = fig.add_subplot(111)
hl, = plt.plot(gData[0], gData[1])
plt.ylim(-90, 90)
plt.xlim(0,200)

# Función que se va a ejecutar en otro thread
# y que guardará los datos del serial en 'out_data'
def GetData(out_data):
    with serial.Serial('/dev/ttyUSB1',115200, timeout=1) as ser:
        print(ser.isOpen())
        while True:
            line = ser.readline().decode('utf-8') # Recibimos por ejemplo: '11.6855913537; 3.74792472633; 2.39604982471;'
            column = 0
            for i in line.split(";"): # Recorremos los campos que hemos recibido
                try: # Hacemos un try, porque el último campo estará vacío, en ese caso nos saltará excepción, así que simplemente pasamos
                    out_data(column).append(float(i)) # Asignamos a cada columna de los datos para pintar, la columna correspondiente del input
                    column = column + 1
                except:
                    pass
               

# Función que actualizará los datos de la gráfica
# Se llama periódicamente desde el 'FuncAnimation' 
def update_line(num, hl, data):
    hl.set_data(list(range(1,len(data)+1)), data)
    return hl,

# Configuramos la función que "animará" nuestra gráfica
line_ani = animation.FuncAnimation(fig, update_line, fargs=(hl, gData),
                                   interval=50, blit=False)

# Configuramos y lanzamos el hilo encargado de leer datos del serial
dataCollector = threading.Thread(target = GetData, args=(gData,))
dataCollector.start()

plt.show()

dataCollector.join()