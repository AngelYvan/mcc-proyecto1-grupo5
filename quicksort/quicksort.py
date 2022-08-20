
import sys
sys.path.append('..\\')
import time
from utils.load_data import readFileCsv, writeFileCsv
# Quick sort in Python

# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)

# data = [8, 7, 2, 1, 0, 9, 6]
cantidades = [100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000]

for x in cantidades:
  tiempos = []
  for y in range(6):
    data = readFileCsv('../data/'+str(x)+'.csv')
    size = len(data)
    start = time.time_ns()
    quickSort(data, 0, size - 1)
    end = time.time_ns()
    duration = end - start
    tiempos.append(duration)
  writeFileCsv('../output/quicksort/python/'+str(x)+'.csv', tiempos)
