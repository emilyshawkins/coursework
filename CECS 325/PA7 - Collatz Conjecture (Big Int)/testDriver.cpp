// Emily Hawkins
// CECS 325-02
// Prog 7 – 3n + 1 (BigInt)
// 04/18/2023
//
// I certify that this program is my own original work. I did not copy any part of this program from
// any other source. I further certify that I typed each and every line of code in this program.

#include <iostream>
#include <limits.h>
#include <vector>
using namespace std;

class BigInt {

  private:
    vector<char> number;

  public:
    BigInt() { // Default constructor
      number = {48};
    }

    BigInt(int x) { // Passing integer
      if (x == 0) {
        number.push_back(48);
      }
      else {
        while (x != 0) {
          number.push_back((x % 10) + 48);
          x /= 10;
        }
      }
    }

    BigInt(string x) { // Passing string
      for (int i = x.length() - 1; i > -1 ; i--) {
        number.push_back(x[i]);
      }
    }

    BigInt operator+(BigInt x) { // Add
      
      vector<char> sum = {};
      int sum_part = 0;
      int carry = 0;
      bool not_equal = false;
      bool this_smaller = false;
      
      if (this->number.size() != x.number.size()) { // Makes numbers the same length
        not_equal = true;
        if (this->number.size() < x.number.size()) {
          this_smaller = true;
          int diff = x.number.size() - this->number.size();
          for (int k = 0; k < diff; k++) {
            this->number.push_back(48);
          }
        }
        else {
          int diff = number.size() - x.number.size();
          for (int k = 0; k < diff; k++) {
            x.number.push_back(48);
          }
        }
      }

      for (int i = 0; i < this->number.size(); i++) { // Calculate sum 
        sum_part = carry + (this->number.at(i) - 48) + (x.number.at(i) - 48);
        carry = 0;

        sum.push_back(BigInt(sum_part).number.at(0)); // One's place of partial sum
        
        if (BigInt(sum_part).number.size() > 1) {
          carry = BigInt(sum_part).number.at(BigInt(sum_part).number.size() - 1) - 48; // Carry value
        }
      } 
      if (carry != 0) {
        sum.push_back(carry + 48);
      }
      
      if (not_equal) {
        if(this_smaller) {
          int size = this->number.size();
          for (int j = size - 1; j > -1; j--) {
            if (this->number.at(j) == '0' && this->number.size() > 1) {
              this->number.pop_back();
            }
            else {
              break;
            }
          }
        }
        else {
          int size = x.number.size();
          for (int j = size - 1; j > -1; j--) {
            if (x.number.at(j) == '0' && x.number.size() > 1) {
              x.number.pop_back();
            }
            else {
              break;
            }
          }
        }
      }
      
      BigInt tot_sum;
      tot_sum.number = sum;
      return tot_sum;
    }
      
    BigInt operator++(int) { // Increment
      *this = *this + BigInt(1);
      return *this;
    }

    BigInt operator*(BigInt x) { // Multiply

      int times = x.number.at(0) - 48;
      BigInt prod(0);

      for (int i = 0; i < times; i++) {
        prod = prod + *this;
      }
      return prod;
    }

    BigInt half() { // Int division by 2
      BigInt half;
      vector<char> half_vec = {};
      half_vec.push_back(((int) (this->number.at(this->number.size() - 1) - 48) / 2) + 48);
      
      for (int i = this->number.size() - 2; i > -1; i--) {
        if ((int) (this->number.at(i + 1) - 48) % 2 == 1) {
          half_vec.push_back((((int) (this->number.at(i) - 48) / 2) + 5) + 48);
        }
        else {
          half_vec.push_back((((int) (this->number.at(i) - 48) / 2)) + 48);
        }
      }

      for (int k = 0; k < half_vec.size() / 2; k++) {
        int temp = half_vec.at(k);
        half_vec.at(k) = half_vec.at(half_vec.size() - 1 - k);
        half_vec.at(half_vec.size() - 1 - k) = temp;
      }

      for (int j = half_vec.size() - 1; j > -1; j--) {
        if (half_vec.at(j) == '0') {
          half_vec.pop_back();
        }
        else {
          break;
        }
      }
      
      half.number = half_vec;
      return half;
    }

    bool isOdd() {
      if ((int) (this->number.at(0) - 48) % 2 == 1) {
        return true;
      }
      return false;
    }

    bool isEven() {
      if ((int) (this->number.at(0) - 48) % 2 == 1) {
        return false;
      }
      return true;
    }

    bool operator==(BigInt x) {
      bool is_equal = true;
      if (this->number.size() == x.number.size()) {
        for (int i = 0; i < x.number.size(); i++) {
          if (this->number.at(i) != x.number.at(i)) {
            is_equal = false;
            break;
          }
        }
      }
      else {
        is_equal = false;
      }
      return is_equal;
    }

    bool operator<(BigInt x) {
      bool this_less = true;

      if(*this == x) {
        return false;
      }
      
      if (this->number.size() != x.number.size()) {
        if(this->number.size() < x.number.size()) {
          this_less = true;
        }
        else {
          this_less = false;
        }
      }
      else {
        for (int i = x.number.size() - 1; i < -1; i--) {
          if (this->number.at(i) < x.number.at(i)) {
            this_less = true;
          }
          else if (this->number.at(i) > x.number.at(i)) {
            this_less = false;
            break;
          }
        }
      }
      return this_less;
    }
    
    friend ostream& operator<<(ostream& out, const BigInt& x) {

      if (x.number.size() <= 8) {
        for (int i = x.number.size() - 1; i > -1; i--) {
          out << x.number.at(i);
        }
      }
      else {
        out << x.number.at(x.number.size() - 1);
        out << '.';
        for (int i = x.number.size() - 2; i > x.number.size() - 9; i--) {
          out << x.number.at(i);
        }
        out << 'e';
        out << x.number.size() - 1;
      }
      return out;
    } 
};



// 3n+1 test driver (required)

// create struct to store all details of 3n+1 sequences
struct ThreeNp1 {
  BigInt start;
  BigInt steps;
  BigInt max;
  BigInt odd;
  BigInt even;
};

// notice that all values are BigInt… cout << BigInt
void print(ThreeNp1 temp) {
  cout << "start: " << temp.start << endl;
  cout << "steps: " << temp.steps << endl;
  cout << "max: " << temp.max << endl;
  cout << "odds: " << temp.odd << endl;
  cout << "evens: " << temp.even << endl;
}

// recursive function to find all details about 3n+1 sequence
// Function has a default parameter as the 3rd parameter
void findThreeNp1(BigInt n, ThreeNp1 & Np1, bool printSteps = false) {
  if (printSteps) {
    cout << "->" << '(' << n << ')' ;
  }
 
  if (Np1.max < n) { // BigInt::operator<( )
     Np1.max = n; // No need to overload - C++ provides operator=( )
  }
  
  if (n == BigInt(1)) { // BigInt::operator==( )
    return; // we are done
  }
  else if (n.isEven()) { // BigInt::isEven()
    Np1.even++; // BigInt::operator++( )
    Np1.steps++;
    
    findThreeNp1(n.half(), Np1, printSteps); //BigInt::half( ) - Easy
  }
  else if (n.isOdd()) { // BigInt::isOdd( )
    Np1.odd++;
    Np1.steps++;
    BigInt tempN(n); // BigInt constructor
    findThreeNp1(tempN*BigInt(3)+BigInt(1), Np1, printSteps); //BigInt::operator*( ) BigInt::operator+( )
  }
  else {
    cout << "How the hell did I get here?\n";
    return;
  }
}

//https://en.wikipedia.org/wiki/Collatz_conjecture

int main() {
  
  BigInt MAX(INT_MAX);
  cout << "The largest integer is "<< MAX<<endl;
  cout << "Twice the largest integer is "<< MAX + MAX << endl;
  
  BigInt start(INT_MAX); // BigInt constructor - use for submission
  // BigInt start(12); // BigInt constructor – use for testing
  
  bool printSteps = false;
  ThreeNp1 N = {start,0,0,0,0}; // initialize N
  
  findThreeNp1(start, N, printSteps); // print out the steps
  cout << endl;
  print(N);

 return 0;
}
