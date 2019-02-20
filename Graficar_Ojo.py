# NOTA IMPORTANTE
# para correr este programa es necesario: 
# 1) tener instalada la libreria de Diagrama de Ojo, la cual se encuentra en este 
# enlace: https://github.com/hortegab/Diagrama-de-ojo-Comunicaciones-II.git
# 2) Correr en grc de gnuradio el archivo Estudio de ISI_file.grc para que este cree a su ves los archivos con datos que nuestra aplicación necesita leer para graficar.


from eyediagram.mpl import eyediagram
import matplotlib.pyplot as plt
import scipy 
import numpy as np

# Configuracion del Diagrama de Ojo
# Ndat: Es el numero de datos a graficar
# Sps: El numero de muestras por simbolo del archivo generado en gnuradio
Ndat=10000 
Sps = 16 

# Leemos el archivo producido por gnuradio
f=scipy.fromfile(open("Senal1"), dtype=scipy.float32) 

#Escogemos una porcion de datos para graficar
fp=(f[0:Ndat])

#Grafica para Rectangular
# plt.subplot(221)
eyediagram(fp, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
plt.show()

# Leemos el archivo producido por gnuradio
f=scipy.fromfile(open("Senal2"), dtype=scipy.float32) 

#Escogemos una porcion de datos para graficar
fp=(f[0:Ndat])

#Grafica para Rectangular
# plt.subplot(221)
eyediagram(fp, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
plt.show()

# Leemos el archivo producido por gnuradio
f=scipy.fromfile(open("Senal3"), dtype=scipy.float32) 

#Escogemos una porcion de datos para graficar
fp=(f[0:Ndat])

#Grafica para Rectangular
# plt.subplot(221)
eyediagram(fp, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
plt.show()

# Leemos el archivo producido por gnuradio
f=scipy.fromfile(open("Senal4"), dtype=scipy.float32) 

#Escogemos una porcion de datos para graficar
fp=(f[0:Ndat])

#Grafica para Rectangular
# plt.subplot(221)
eyediagram(fp, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
plt.show()

# Leemos el archivo producido por gnuradio
f=scipy.fromfile(open("Senal5"), dtype=scipy.float32) 

#Escogemos una porcion de datos para graficar
fp=(f[0:Ndat])

#Grafica para Rectangular
# plt.subplot(221)
eyediagram(fp, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
plt.show()

