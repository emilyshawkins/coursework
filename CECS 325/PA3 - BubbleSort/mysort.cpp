// Emily Hawkins
// CECS 325-02
// Prog 3 – Sort Race
// 03/07/2023
//
// I certify that this program is my own original work. I did not copy any part of this program from
// any other source. I further certify that I typed each and every line of code in this program.

#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char *argv[]) {

  ifstream numbers;
  numbers.open(argv[1], ios::in);

  int array_size = 0;
  int ele;
  while (numbers >> ele) { // Size for array
    array_size++;
  }

  numbers.close();

  ifstream num_arr;
  num_arr.open(argv[1], ios::in);
  
  int a[array_size];
  int count = 0;
  while (num_arr >> ele) {
    a[count] = ele;
    count++;
  }

  num_arr.close();

  for (int i = 0; i < sizeof(a)/sizeof(a[0]); i++) { // Bubble sort
    for(int j = 0; j < (sizeof(a)/sizeof(a[0])) - 1; j++){
      if (a[j] > a[j+1]){
        int temp = a[j];
        a[j] = a[j + 1];
        a[j + 1] = temp;
      }
    }
  }

  ofstream sortout;
  sortout.open(argv[2], ios::out | ios::trunc);
  
  for (int k = 0; k < array_size; k++){
    sortout << a[k] << endl;
  }

  sortout.close();
  return 0;
}