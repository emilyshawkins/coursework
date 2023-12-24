// Emily Hawkins
// CECS 325-02
// Prog 1 – Fibonacci Solitare
// 02/14/2023
//
// I certify that this program is my own original work. I did not copy any part of this program from
// any other source. I further certify that I typed each and every line of code in this program.

#ifndef DECK_H
#define DECK_H

#include "Card.h"

class Deck {
  private:
    Card cards[52];
    int deckSize;
  public:
    Deck();

    void resetDeck();
    Card deal();
    void shuffle();
    bool isEmpty();
    void show();
};

#endif