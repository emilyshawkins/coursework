// Emily Hawkins
// CECS 325-02
// Prog 1 – Fibonacci Solitare
// 02/14/2023
//
// I certify that this program is my own original work. I did not copy any part of this program from
// any other source. I further certify that I typed each and every line of code in this program.

#ifndef CARD_H
#define CARD_H

class Card {
  private:
    char rank;
    char suit;

  public:
    Card();
    Card(char r, char s);

    void setCard(char r, char s);
    int getValue();
    void show();

};

#endif