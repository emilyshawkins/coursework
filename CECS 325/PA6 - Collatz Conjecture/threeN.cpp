// Emily Hawkins
// CECS 325-02
// Prog 6 – 3n + 1 (Integer)
// 04/18/2023
//
// I certify that this program is my own original work. I did not copy any part of this program from
// any other source. I further certify that I typed each and every line of code in this program.

#include <iostream>
#include <limits.h>
using namespace std;

struct threeNstats {
  int steps = 0; // How many steps to get to 1
  int max = 0; // Maximum number reached in the process
  int odds = 0; // Number of odds in the process
  int evens = 0; // Number of evens in the process
};

void threeN(int user_num, int num, threeNstats &stats) { 
  cout << "->(" << num << ")";

  if (num > stats.max) { // To find maximum
    stats.max = num;
  }
  
  if (num == 1) { // When number is one
    stats.odds++; // For 1
    
    cout << endl;
    cout << "   Start: " << user_num << endl;
    cout << "   Steps: " << stats.steps << endl;
    cout << "   Max: " << stats.max << endl;
    cout << "   Odds: " << stats.odds << endl;
    cout << "   Evens: " << stats.evens << endl;
    cout << endl;
    
    return;
  }
  else if (num % 2 == 0) { // When number is even
    stats.steps++;
    stats.evens++;
    threeN(user_num, num / 2, stats);
  }
  else if (num % 2 == 1) { // When number is odd
    stats.odds++;
    stats.steps++;

    if (num > double ((INT_MAX - 1) / 3)) {
      cout << "->(###overflow###)" << endl;
      cout << endl;
      cout << "   Overflow detected for n = " << num << endl;
      cout << "   3n + 1 = " << (3 * num) + 1 << endl;
      
      throw "   Integer Overflow";
    }
    
    threeN(user_num, (3 * num) + 1, stats);
  }
  
}

int main(int argc, char *argv[]) {

  if (argc == 1) {
    
    int num_choice; // Original number chosen by the user
    struct threeNstats stats;
    
    cout << "Enter a 3n + 1 candidate number: ";
    cin >> num_choice;

    try {
      threeN(num_choice, num_choice, stats);
    }
    catch(const char* overflow) {
      cout << overflow << endl;
      cout << endl;
    }
  }

  else if (argc > 1) {
    for (int i = 1; i < argc; i++) {

      int num_choice; // Original number chosen by the user
      struct threeNstats stats;

      num_choice = stoi(argv[i]);

      cout << "Solving 3n + 1: Starting Value: " << num_choice << endl;
    
      try {
        threeN(num_choice, num_choice, stats);
      }
      catch(const char* overflow) {
        cout << overflow << endl;
        cout << endl;
      }
    }
  }
  
  return 0;
}