# Ejercicio5
# imprima el mensaje: "hola mundo super CRUEL!"

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import OrderedDict

print("hola mundo SUPER cruel")

#Carga archivo dat.txt
data=np.loadtxt('dat.txt',delimiter=' ')

#Datos X y Y
x=data[:,0]
y=data[:,1]

plt.plot(x,y,"m",label="Global data")
plt.legend()
plt.xlabel("Años")
plt.ylabel("Anomalías de temperatura (°C)")
plt.savefig('Grafica_temp.png')

