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
        data = readFileCsv('../output/quicksort/python/'+str(x)+'.csv')
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
        data = readFileCsv('../output/quicksort/cpp/'+str(x)+'.csv')
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
        data = readFileCsv('../output/quicksort/go/'+str(x)+'.csv')
    # print(data)
    st_dev = np.std(data)
    media100 = np.mean(data)
    print("Para ", x, " numeros")
    print("Desviacion Estandar: ", st_dev)
    print("La Media es ", media100)
    tiempo_go.append(media100)

# create data
elementos = [100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000]
# tiempo_python = [3,3,3,3,3,4,5,6,7,8,9,10,13,14,15]
# tiempo_cpp = [3,3,3,3,3,6,8,12,14,16,18,20,24,26,28]
# tiempo_go = [3,3,3,3,3,9,12,15,18,21,24,27,30,33,36]
  
# plot lines
plt.plot(elementos, tiempo_python, label = "python")
plt.plot(elementos, tiempo_cpp, label = "C++")
plt.plot(elementos, tiempo_go, label = "go")

plt.legend()
plt.show()