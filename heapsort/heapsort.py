
import sys
sys.path.append('..\\')
import time
from utils.load_data import readFileCsv, writeFileCsv
# Heapsort in Python

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
 
 # See if left child of root exists and is
 # greater than root
 
    if l < n and arr[i] < arr[l]:
        largest = l
 
 # See if right child of root exists and is
 # greater than root
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
 # Change root, if needed
 
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
 
  # Heapify the root.
 
        heapify(arr, n, largest)
 
 
# The main function to sort an array of given size
 
def heapSort(arr):
    n = len(arr)
 
 # Build a maxheap.
 # Since last parent will be at ((n//2)-1) we can start at that location.
 
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
 
 # One by one extract elements
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)

# data = [8, 7, 2, 1, 0, 9, 6]
cantidades = [100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000]

for x in cantidades:
  tiempos = []
  for y in range(6):
    data = readFileCsv('../data/'+str(x)+'.csv')
    size = len(data)
    start = time.time_ns()
    heapSort(data)
    end = time.time_ns()
    duration = end - start
    tiempos.append(duration)
  writeFileCsv('../output/heapsort/python/'+str(x)+'.csv', tiempos)
