# Megan Waples and Emily Hawkins
# Fall 2022
# Generates a RxC solution board for the game Minesweeper and displays the grid

import check_input
import random


def places_mines(board, mines):
    '''Each mine location, row and column is generated within bounds and added to the board if the generated location is not already a mine.'''

    i = 0

    while i < mines:  # Assign a random integer pair to each position
        row = random.randint(1, len(board) - 2)
        column = random.randint(1, len(board[0]) - 2)
        if board[row][column] == '0':  #if the integer is zero reassign to an X for a mine
            board[row][column] = 'X'
            i += 1


def count_mines(board):
    '''Checks if the location is a mine and checks the surrounding eight spots if the location is not a mine. Then the number of mines surrounding is placed in the location.'''

    mines = 0

    for row in range(1, len(board) - 1):
        for column in range(1, len(board[row]) - 1):
            if board[row][column] != 'X':
                for r in range(-1, 2):
                    for c in range(-1, 2):
                        if r == 0 and c == 0:
                            continue
                        else:
                            if board[r + row][c + column] == 'X':
                                mines += 1

                board[row][column] = mines
                mines = 0



def display_board(board):
    '''Display the contents of the grid using a set of nested loops.'''
    for row in board:
        for column in row:
            print(column, end=' ')
        print()



def main():

    print("Minesweeper Maker\n")
    # get 3 user inputs and check that they are in range(5 to 10)
    rows = check_input.get_int_range(' Enter number of rows (5-10): ', 5, 10)
    columns = check_input.get_int_range(" Enter number of columns (5-10): ", 5,10)
    mines = check_input.get_int_range(' Enter number of mines (5-10): ', 5, 10)

    # generate a grid using user inputs and fill it with zeros
    board = []
    for i in range(rows):
        list = []
        empty = []
        for i in range(columns):
            list.append('0')
            empty.append('-')

        list.insert(0, "|")
        list.append('|')
        board.append(list)

    empty.append('-')
    empty.append('-')

    board.insert(0, empty)
    board.append(empty)

    places_mines(board, mines)
    count_mines(board)
    display_board(board)



main()
