# Megan Waples and Emily Hawkins
# Fall 2022
# Quizzes the user on States and capitals then returns the score

import random

def read_file_to_dict(file_name):
  '''Takes in the text file and creates and returns a dictionary of states as keys and capitals as values.'''

  state_dict = {}
  
  state_list = file_name.readlines()

  for i in range(0, len(state_list)):
    key = state_list[i].strip().split(',')

    state_dict[key[0]] = key[1]
    
  return state_dict

def get_random_state(states):
  '''Passes in the states dictionary and converts the dictionary to a list of key:value pairs. A random key:value pair is generated and returned as the correct state and capital for the question'''
  
  cap_state = []
  state_list = list(states)
  #convert dictionary to list
  for i in range(len(state_list)):
    cap_state.append([state_list[i], states[state_list[i]]])
  #return a random pair for the answer
  random_key = random.randint(0, len(cap_state) - 1)
  return cap_state[random_key]

def get_random_choices(states, correct_capital):
  '''Passes in the states dictionary, and the capital of the correct answer. Creates and shuffles for options, including the correct answer, for the answer options to the question and returns them'''

  cap_state = []
  state_list = list(states)
  options = [correct_capital, 0, 0, 0]
  
#convert dictionary to list of values
  for i in range(len(state_list)):
    cap_state.append([state_list[i], states[state_list[i]]])

  choices = 1
  duplicate = False

  while choices < 4: #Add 3 more incorret options

    random_key = random.randint(0, len(cap_state) - 1)
    
    for j in range(0, len(options)): #Check if the random pair is already the answer
      if cap_state[random_key][1] != options[j]:
        duplicate = False
      elif cap_state[random_key][1] == options[j]:
        duplicate = True
        break
        
    if duplicate == False: #If it isn't already an option add it to the options
      options[choices] = cap_state[random_key][1]
      choices += 1

  random.shuffle(options) #Shuffle the options so the answer isn't in the same place everytime
        
  return options

def ask_question(correct_state, possible_answers):
  '''Passes in the name of the correct state and the list of 4 possible answers. The question is displayed and the user's selection is taken in and validated. Then the user's input is converted into a number and returned. '''
  
  #Format question
  print(f'   A. {possible_answers[0]}\n   B. {possible_answers[1]}\n   C. {possible_answers[2]}\n   D. {possible_answers[3]}')

  while True: #check input and return user input
    
    user_answer = input('\nEnter selection: ').upper()
    
    if user_answer == 'A':
      return 0
      break
    elif user_answer == 'B':
      return 1
      break
    elif user_answer == 'C':
      return 2
      break
    elif user_answer == 'D':
      return 3
      break
    else:
      print('Invalid input. Input choice A-D')


def main():

  score = 0
  
  print('- State Capital Quiz -')

  file_name = open('StateCapitals.txt', 'r')

  read_file = read_file_to_dict(file_name)
  
  for i in range(1, 11): #Ask user 10 questions
    
    rand_state = get_random_state(read_file)

    options = get_random_choices(read_file, rand_state[1])

    print(f'\n{i}. The capital of {rand_state[0]} is:\n')

    user_selection = ask_question(rand_state[0], options)
    #determine is user is correct or not
    if options[user_selection] == rand_state[1]:
      score += 1
      print('Correct!')
    else:
      print(f'Incorrect! The correct answer is: {rand_state[1]}.')

  print(f'\nEnd of test. You got {score} correct.')
  
main()
