#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
using namespace std;

vector<int> readFileCsv(string nameFile){
  std::vector<int> numeros;
  ifstream archivo(nameFile);
    string linea;
    char delimitador = ';';
    // Leemos todas las líneas
    while (getline(archivo, linea))
    {
      int num = 0;

      for (size_t i = 0; i <= linea.size(); i++)
      {
        if ((linea[i] != delimitador) && (linea[i] != '\0'))
        {
          num = (num * 10) + ((int)linea[i] -'0');
        } else {
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

void writeFileCsv(string nameFile, vector<int> vals){
  ofstream myFile(nameFile);
  for(int i = 0; i < vals.size(); ++i)
  {
      myFile << vals.at(i) << "\n";
  }
  myFile.close();
}