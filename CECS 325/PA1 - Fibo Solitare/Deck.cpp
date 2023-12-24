// Emily Hawkins
// CECS 325-02
// Prog 1 – Fibonacci Solitare
// 02/14/2023
//
// I certify that this program is my own original work. I did not copy any part of this program from
// any other source. I further certify that I typed each and every line of code in this program.

#include <iostream>
#include <cstdlib>
using namespace std;
#include "Deck.h"

Deck::Deck() {
  deckSize = 52;
  char suits [4] = {'S', 'H', 'D', 'C'};
  char ranks [13] = {'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'};
  int cardNum = 0;
  
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 13; j++) {
      cards[cardNum].setCard(ranks[j], suits[i]);
      cardNum++;
    }
  }
}

void Deck::resetDeck() {
  char suits [4] = {'S', 'H', 'D', 'C'};
  char ranks [13] = {'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'};
  int cardNum = 0;
  
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 13; j++) {
      cards[cardNum].setCard(ranks[j], suits[i]);
      cardNum++;
    }
  }
}

Card Deck::deal() {
  Card top = cards[deckSize - 1];
  deckSize--;
  
  return top;
}

void Deck::shuffle() {
  for(int shuff = 0; shuff < 1000; shuff++){

    int chooseOne = rand() % 52;
    int chooseTwo = rand() % 52;

    Card temp = cards[chooseOne];
    cards[chooseOne] = cards[chooseTwo];
    cards[chooseTwo] = temp;
  }
}

bool Deck::isEmpty() {
  if (deckSize == 0) {
    return true;
  }
  else {
    return false;
  }
}

void Deck::show() {
  int cardNum = 0;
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 13; j++) {
      cards[cardNum].show();
      cout << ' ';
      cardNum++;
    }
    cout << endl;
  }
}

