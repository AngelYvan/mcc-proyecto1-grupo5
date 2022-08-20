// Quick sort in C++

#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <chrono>
#include <string> 
#include "../utils/load_data.h"
#include <typeinfo>
using namespace std;
using namespace std::chrono;

// function to swap elements
void swap(int *a, int *b) {
  int t = *a;
  *a = *b;
  *b = t;
}

// function to print the array
void printArray(int array[], int size) {
  int i;
  for (i = 0; i < size; i++)
    cout << array[i] << " ";
  cout << endl;
}

// function to rearrange array (find the partition point)
int partition(int array[], int low, int high) {
    
  // select the rightmost element as pivot
  int pivot = array[high];
  
  // pointer for greater element
  int i = (low - 1);

  // traverse each element of the array
  // compare them with the pivot
  for (int j = low; j < high; j++) {
    if (array[j] <= pivot) {
        
      // if element smaller than pivot is found
      // swap it with the greater element pointed by i
      i++;
      
      // swap element at i with element at j
      swap(&array[i], &array[j]);
    }
  }
  
  // swap pivot with the greater element at i
  swap(&array[i + 1], &array[high]);
  
  // return the partition point
  return (i + 1);
}

void quickSort(int array[], int low, int high) {
  if (low < high) {
      
    // find the pivot element such that
    // elements smaller than pivot are on left of pivot
    // elements greater than pivot are on righ of pivot
    int pi = partition(array, low, high);

    // recursive call on the left of pivot
    quickSort(array, low, pi - 1);

    // recursive call on the right of pivot
    quickSort(array, pi + 1, high);
  }
}

// Driver code
int main() {
  int cantidades [15]= {100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000};
  for (size_t i = 0; i < 15; i++)
  {
    vector<int> tiempos;
    for (size_t j = 0; j < 5; j++)
    {
      vector<int> numeros;
      string nombreArchivo = "../data/"+to_string(cantidades[i])+".csv";
      numeros = readFileCsv(nombreArchivo);

      int longitud = numeros.size();
      int data[longitud];
      for (int i = 0; i < longitud; i++) {
          data[i] = numeros[i];
      }
      int n = sizeof(data) / sizeof(data[0]);
      // cout << "Unsorted Array: \n";
      // printArray(data, n);
      auto start = high_resolution_clock::now();
      quickSort(data, 0, n - 1);
      auto stop = high_resolution_clock::now();
      auto duration = duration_cast<nanoseconds>(stop - start);
      int tiempo = duration.count();
      tiempos.push_back(tiempo);
    }
    string nombreArchivo = "../output/quicksort/cpp/"+to_string(cantidades[i])+".csv";
    writeFileCsv(nombreArchivo, tiempos);
  }

}