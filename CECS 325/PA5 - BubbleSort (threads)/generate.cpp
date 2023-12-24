// Emily Hawkins
// CECS 325-02
// Prog 5 – Sorting Contest (Threading with Threads)
// 04/06/2023
//
// I certify that this program is my own original work. I did not copy any part of this program from
// any other source. I further certify that I typed each and every line of code in this program.

#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char *argv[]) { // Number of arguments + arguments in array
  srand(time(0));

  if (argc != 4) { // If it's not file name and count min max
    cout << "There must be three parameters -> number of elements, minimum value, maximum value. Please try again." << endl;
    exit(EXIT_SUCCESS); // End
  }

  int array_size = stoi(argv[1]);
  int array[array_size];
  int min_count = stoi(argv[2]);
  int max_count = stoi(argv[3]);

  for (int i = 0; i < array_size; i++) {
    array[i] = min_count + rand() % (max_count - min_count + 1);
  }

  ofstream numbers;
  numbers.open("numbers.dat", ios::out | ios::trunc);
  for (int k = 0; k < array_size; k++) {
    numbers << (array[k]) << endl;
  }
  numbers.close();
  return 0;
}