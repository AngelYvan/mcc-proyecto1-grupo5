import matplotlib.pyplot as plt
import numpy as np
  
# create data
elementos = [100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000]
tiempo_python = [3,3,3,3,3,4,5,6,7,8,9,10,13,14,15]
tiempo_cpp = [3,3,3,3,3,6,8,12,14,16,18,20,24,26,28]
tiempo_go = [3,3,3,3,3,9,12,15,18,21,24,27,30,33,36]
  
# plot lines
plt.plot(elementos, tiempo_python, label = "python")
plt.plot(elementos, tiempo_cpp, label = "C++")
plt.plot(elementos, tiempo_go, label = "go")

plt.legend()
plt.show()