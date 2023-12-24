// Emily Hawkins
// CECS 325-02
// Prog 2 – Fibonacci Solitare (Single File)
// 02/21/2023
//
// I certify that this program is my own original work. I did not copy any part of this program from
// any other source. I further certify that I typed each and every line of code in this program.

#include <iostream>
using namespace std;

class Card {
  private:
    char rank;
    char suit;

  public:
    Card() {
    setCard('0', 'X');
    }

    Card(char r, char s) {
    setCard(r, s);
    }

    void setCard(char r, char s) {
      rank = r;
      suit = s;
    } 

    int getValue() {
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

    void show() {
      if (rank == 'T') {
        cout << 10 << suit << ' ';
      }
      else {
        cout << rank << suit << ',';
      }
    }
};

class Deck {
  private:
    Card cards[52];
    int deckSize;

  public:
    Deck() {
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

    void resetDeck() {
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

    Card deal() {
      Card top = cards[deckSize - 1];
      deckSize--;
  
      return top;
    }

    void shuffle() {
      for(int shuff = 0; shuff < 1000; shuff++){

        int chooseOne = rand() % 52;
        int chooseTwo = rand() % 52;

        Card temp = cards[chooseOne];
        cards[chooseOne] = cards[chooseTwo];
        cards[chooseTwo] = temp;
      }
    }

    bool isEmpty() {
      if (deckSize == 0) {
        return true;
      }
      else {
        return false;
      }
    }

    void show() {
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
};

bool isFibo(int n) {

  int fibo_ref[12] = {1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233};
  
  for (int i = 0; i < 12; i++) {
    if (n == fibo_ref[i]) {
      return true;
    }
  }
  return false;
}

int main() {
  
  srand(time(0));
  char user_input;
  
  cout << "Welcome to Fibonacci Solitaire!\n1) Create New Deck\n2) Shuffle Deck\n3) Display Deck\n4) Play Fibo Solitaire\n5) Win Fibo Solitaire\n6) Exit" << endl;  
  cin >> user_input;
  int user_input_num = int(user_input) - 48;

  Deck game_deck;

  while (user_input_num != 6){
    if (user_input_num == 1) {
      game_deck = Deck();
    }
    else if (user_input_num == 2) {
      game_deck.shuffle();
    }
    else if (user_input_num == 3) {
      if (game_deck.isEmpty()) {
        cout << "There is no deck to display, please create a new deck." << endl;
      }
      else {
        game_deck.show();
      }
    }
    else if (user_input_num == 4) {
      bool game_start = true;
      if (game_deck.isEmpty()) {
        game_start = false;
        cout << "There is no deck to play with, please create a new deck." << endl;
      }
      int card_sum = 0;
      int piles = 0;
      while (!game_deck.isEmpty()) {
        
        Card played = game_deck.deal();
        played.show();
        cout << ' ';
        card_sum += played.getValue();
           
        if (isFibo(card_sum)) {
          cout << "Fibo: " << card_sum << endl;
          card_sum = 0;
          piles++;
        }      
      }
      if(card_sum == 0 && game_start) {
        cout << "Winner in " << piles << " pile(s)" << endl;
      }
      else if(game_start) {
        piles++;
        cout << "Last Pile NOT Fibo: " << card_sum << endl; 
        cout << "Loser in " << piles << " pile(s)" << endl;
      }
    }
    else if (user_input_num == 5) {
      
      bool winner = false;
      int num_games = 0;
      game_deck = Deck();
      
      while (winner == false) {
        num_games++;
        int card_sum = 0;
        int piles = 0;
        game_deck.shuffle();
        
        while (!game_deck.isEmpty()) {
        
          Card played = game_deck.deal();
          played.show();
          cout << ' ';
          card_sum += played.getValue();
         
          if (isFibo(card_sum)) {
            cout << "Fibo: " << card_sum << endl;
            card_sum = 0;
            piles++;
          }   
        }
        if(card_sum == 0) {
          cout << "Winner in " << piles << " pile(s)" << endl;
          cout << "Games Played: " << num_games << endl;
          winner = true;
        }
        else {
          piles++;
          cout << "Last Pile NOT Fibo: " << card_sum << endl; 
          cout << "Loser in " << piles << " pile(s)" << endl;
          cout << endl;
          
          game_deck = Deck();
          
        }
      }
    }

    cin >> user_input;
    user_input_num = int(user_input) - 48;
    
  }
  return 0;
}
