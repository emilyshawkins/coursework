// Emily Hawkins
// CECS 325-02
// Prog 4 – Sorting Contest (pthread)
// 03/21/2023
//
// I certify that this program is my own original work. I did not copy any part of this program from
// any other source. I further certify that I typed each and every line of code in this program.

#include <iostream>
#include <fstream>
#include <pthread.h>
using namespace std;

struct section {
  int *arr;
  int size;
};

void *mysort(void *arr_and_num) {
  section *params = (section *) arr_and_num; // cast to arr section type pointer from void
  for (int i = 0; i < params->size; i++) { // Bubble sort, -> access struc
    for(int j = 0; j < (params->size) - 1; j++){
      if (params->arr[j] > params->arr[j+1]){
        int temp = params->arr[j];
        params->arr[j] = params->arr[j + 1];
        params->arr[j + 1] = temp;
      }
    }
  }
  return NULL;
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

  section chunks[8];

  for (int i = 0; i < 8; i++) {
    chunks[i].arr = &full_array[subarr_size * i];
    chunks[i].size = subarr_size; 
  }

  pthread_t thread_one, thread_two, thread_three, thread_four, thread_five, thread_six, thread_seven, thread_eight; // Threads

  int return_one, return_two, return_three, return_four, return_five, return_six, return_seven, return_eight; // Will contain return values

  return_one = pthread_create(&thread_one, NULL, mysort, (void *) &chunks[0]); // Params: Thread Location, attr for created thread, func for exec, arg passed to func (void ptr to add)
  return_two = pthread_create(&thread_two, NULL, mysort, (void *) &chunks[1]);
  return_three = pthread_create(&thread_three, NULL, mysort, (void *) &chunks[2]);
  return_four = pthread_create(&thread_four, NULL, mysort, (void *) &chunks[3]);
  return_five = pthread_create(&thread_five, NULL, mysort, (void *) &chunks[4]);
  return_six = pthread_create(&thread_six, NULL, mysort, (void *) &chunks[5]);
  return_seven = pthread_create(&thread_seven, NULL, mysort, (void *) &chunks[6]);
  return_eight = pthread_create(&thread_eight, NULL, mysort, (void *) &chunks[7]);

  pthread_join(thread_one, NULL); // Params: Thread, Ex stat
  pthread_join(thread_two, NULL);
  pthread_join(thread_three, NULL);
  pthread_join(thread_four, NULL);
  pthread_join(thread_five, NULL);
  pthread_join(thread_six, NULL);
  pthread_join(thread_seven, NULL);
  pthread_join(thread_eight, NULL);

  for (int j = 0; j < 2; j++) {
    for (int k = 0; k < 4; k++) {
      merge(chunks[k * 2].arr, chunks[k * 2 + 1].arr, subarr_size);
    }
    merge(chunks[j * 4].arr, chunks[j * 4 + 2].arr, subarr_size * 2);
  }
  merge(chunks[0].arr, chunks[4].arr, subarr_size * 4);
  
  ofstream sortout;
  sortout.open(argv[2], ios::out | ios::trunc);
  for (int q = 0; q < total_size; q++){
    sortout << full_array[q] << endl;
  }
  sortout.close();
  
  return 0;
}