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

void heapify(int arr[], int n, int root)
{
   int largest = root; 
   int l = 2*root + 1; 
   int r = 2*root + 2; 
  
   if (l < n && arr[l] > arr[largest])
   largest = l;
  
   if (r < n && arr[r] > arr[largest])
   largest = r;
  
   if (largest != root)
      {
      swap(arr[root], arr[largest]);
      heapify(arr, n, largest);
      }
}

void heapSort(int arr[], int n)
{

   for (int i = n / 2 - 1; i >= 0; i--)
   heapify(arr, n, i);
   for (int i=n-1; i>=0; i--)
   {
      swap(arr[0], arr[i]);
      heapify(arr, i, 0);
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
      heapSort(data, n);
      auto stop = high_resolution_clock::now();
      auto duration = duration_cast<nanoseconds>(stop - start);
      int tiempo = duration.count();
      tiempos.push_back(tiempo);
    }
    string nombreArchivo = "../output/heapsort/cpp/"+to_string(cantidades[i])+".csv";
    writeFileCsv(nombreArchivo, tiempos);
  }

}