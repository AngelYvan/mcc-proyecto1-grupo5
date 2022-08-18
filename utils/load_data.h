#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#define NOMBRE_ARCHIVO "data/1000.csv"
using namespace std;

vector<int> readFileCsv(){
  std::vector<int> numeros;
  ifstream archivo(NOMBRE_ARCHIVO);
    string linea;
    char delimitador = ';';
    // Leemos todas las líneas
    while (getline(archivo, linea))
    {
      // cout << linea << endl;
      int num = 0;

      for (size_t i = 0; i <= linea.size(); i++)
      {
        // cout << linea[i] << endl;
        if ((linea[i] != delimitador) && (linea[i] != '\0'))
        {
          num = (num * 10) + ((int)linea[i] -'0');
        } else {
          // cout << num << endl;
          if (num != 0)
          {
            numeros.push_back(num);
            num = 0;
          }
        }
      }
    }

    archivo.close();
  return numeros;
}