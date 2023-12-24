# Megan Waples and Emily Hawkins
# Fall 2022
# Generates a random integer between 1 - 100 and has the user input a guess for the generated random integer

from random import randint
import check_input

def main():
  '''Generates a random integer between 1 - 100 and has the user input a guess for the generated random integer'''

  random_int = randint(1, 100)

  print("- Guessing Game -")

  user_guess = check_input.get_int_range("I'm thinking of a number.  Make a guess: ", 1, 100)

  tries = 1
  
  #Ask user for input until they guess correctly
  while user_guess != random_int: 
    # Check user input and determine if the guess is too high or too low
    if user_guess < random_int:
      print("Too Low!", end=" ")
      user_guess = check_input.get_int_range("Guess again: ", 1, 100)
      tries += 1
      
    elif user_guess > random_int:
      print("Too high!", end=" ")
      user_guess = check_input.get_int_range("Guess again: ", 1, 100)
      tries += 1
    
  print("Correct!", "You got it in", tries)

main()
   

  


