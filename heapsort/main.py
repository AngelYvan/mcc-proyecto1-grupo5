import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('..\\')
from utils.load_data import readFileCsv, writeFileCsv
  
cantidades = [100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000]

tiempo_python = []
print("Resultados en Python")
for x in cantidades:
    data = []
    for y in range(6):
        data = readFileCsv('../output/heapsort/python/'+str(x)+'.csv')
    # print(data)
    st_dev = np.std(data)
    media100 = np.mean(data)
    print("Para ", x, " numeros")
    print("Desviacion Estandar: ", st_dev)
    print("La Media es ", media100)
    tiempo_python.append(media100)

tiempo_cpp = []
print("Resultados en C++")
for x in cantidades:
    data = []
    for y in range(6):
        data = readFileCsv('../output/heapsort/cpp/'+str(x)+'.csv')
    # print(data)
    st_dev = np.std(data)
    media100 = np.mean(data)
    print("Para ", x, " numeros")
    print("Desviacion Estandar: ", st_dev)
    print("La Media es ", media100)
    tiempo_cpp.append(media100)

tiempo_go = []
print("Resultados en Go")
for x in cantidades:
    data = []
    for y in range(6):
        data = readFileCsv('../output/heapsort/go/'+str(x)+'.csv')
    # print(data)
    st_dev = np.std(data)
    media100 = np.mean(data)
    print("Para ", x, " numeros")
    print("Desviacion Estandar: ", st_dev)
    print("La Media es ", media100)
    tiempo_go.append(media100)

# create data
elementos = [100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000]
  
# plot lines
plt.plot(elementos, tiempo_python, label = "python")
plt.plot(elementos, tiempo_cpp, label = "C++")
plt.plot(elementos, tiempo_go, label = "go")

plt.legend()
plt.show()