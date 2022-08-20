import os
import csv

def readFileCsv(fileName):
  data = []
  with open(fileName, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for x in spamreader:
      for y in x:
        if y != '':
          data.append(int(y))
  return data

def writeFileCsv(fileName, intArray):
  f = open(fileName, 'w')
  writer = csv.writer(f, delimiter=';')
  writer.writerow(intArray)
  f.close()