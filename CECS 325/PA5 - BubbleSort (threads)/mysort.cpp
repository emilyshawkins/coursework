// Emily Hawkins
// CECS 325-02
// Prog 5 – Sorting Contest (Threading with Threads)
// 04/06/2023
//
// I certify that this program is my own original work. I did not copy any part of this program from
// any other source. I further certify that I typed each and every line of code in this program.

#include <iostream>
#include <fstream>
#include <thread>
using namespace std;

void mysort(int *arr_sec, int sec_size) {
  for (int i = 0; i < sec_size; i++) { 
    for(int j = 0; j < (sec_size) - 1; j++){
      if (arr_sec[j] > arr_sec[j+1]){
        int temp = arr_sec[j];
        arr_sec[j] = arr_sec[j + 1];
        arr_sec[j + 1] = temp;
      }
    }
  }
}

int merge(int *arr_one, int *arr_two, int size) {
  int i = 0;
  int j = 0;
  int merged[size * 2];
  for (int k = 0; k < size * 2; k++) {
    if (i == size) {
      merged[k] = arr_two[j];
      j++;
    }
    else if (j == size) {
      merged[k] = arr_one[i];
      i++;
    }
    else if (arr_one[i] <= arr_two[j]) {
      merged[k] = arr_one[i];
      i++;
    }
    else {
      merged[k] = arr_two[j];
      j++;
    }
  }

  for (int q = 0; q < size * 2; q++) {
    arr_one[q] = merged[q];
  }
  
  return 0;
}

int main(int argc, char *argv[]) {

  int total_size = 1000000;
  int subarr_size = total_size / 8;
  
  int full_array[total_size];

  ifstream fill_array;
  int ele;
  fill_array.open(argv[1], ios::in);
  int track = 0;
  while (fill_array >> ele) {
    full_array[track] = ele;
    track++;
  }

  int* chunks[8];

  for (int i = 0; i < 8; i++) {
    chunks[i] = &full_array[subarr_size * i];
  }

  thread thread_one(mysort, chunks[0], subarr_size); // Params: Function, function args
  thread thread_two(mysort, chunks[1], subarr_size);
  thread thread_three(mysort, chunks[2], subarr_size);
  thread thread_four(mysort, chunks[3], subarr_size);
  thread thread_five(mysort, chunks[4], subarr_size);
  thread thread_six(mysort, chunks[5], subarr_size);
  thread thread_seven(mysort, chunks[6], subarr_size);
  thread thread_eight(mysort, chunks[7], subarr_size);

  thread_one.join();
  thread_two.join();
  thread_three.join();
  thread_four.join();
  thread_five.join();
  thread_six.join();
  thread_seven.join();
  thread_eight.join();

  for (int j = 0; j < 2; j++) {
    for (int k = 0; k < 4; k++) {
      merge(chunks[k * 2], chunks[k * 2 + 1], subarr_size);
    }
    merge(chunks[j * 4], chunks[j * 4 + 2], subarr_size * 2);
  }
  merge(chunks[0], chunks[4], subarr_size * 4);
  
  for (int q = 0; q < total_size; q++){
    cout << full_array[q] << endl;
  }
  
  return 0;
}