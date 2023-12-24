// Emily Hawkins
// CECS 325-02
// Prog 1 – Fibonacci Solitare
// 02/14/2023
//
// I certify that this program is my own original work. I did not copy any part of this program from
// any other source. I further certify that I typed each and every line of code in this program.

#include <iostream>
using namespace std;
#include "Card.h"

Card::Card() {
  setCard('0', 'X');
}

Card::Card(char r, char s) {
  setCard(r, s);
}

void Card::setCard(char r, char s) {
  rank = r;
  suit = s;
}

int Card::getValue() {
  if (rank == 'A') {
    return 1;
  }
  else if (rank == 'J' || rank == 'Q' || rank == 'K' || rank == 'T') {
    return 10;
  }
  else {
    return int(rank) - 48;
  }
}

void Card::show() {

  if (rank == 'T') {
    cout << 10 << suit << ' ';
  }
  else {
    cout << rank << suit << ',';
  }
}