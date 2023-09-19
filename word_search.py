"""
    File: word_search.py
    Author: Nees Abusaada
    Purpose: This program will read a file provided by the user.
    It will iterate through the puzzle grid in the file and find the words
    located at the bottom of the file. It will iterate with 8 directions
    left to right horizontally, up and down vertically, diagonally right
    to left and left to right searching for words. Finally, it will print
    out the grid with the words that are found. Otherwise, it will print
    (.) to complete the grid.
"""

def process_data():
    '''
    This function will take input from the user, which is the
    file name. Using for loop to iterate through each line and
    using if statement to check if there is a blank line then it
    change the puzzle_end varibale to Ture. If puzzle_end is
    False then it will append to the puzzle array. Otherwise
    if length of each row is greater than 0 it will append
    to the words array. It returns puzzle and words arrays.
    If the file doesn't exist it will print an error message.
    '''
    file_name = input("Please give the puzzle filename:\n")
    try:
        puzzle_grid = open(file_name, "r").readlines()
        puzzle = []
        words = []
        puzzle_end = False
        for line in puzzle_grid:
            if line == "\n":
                puzzle_end = True
            if not puzzle_end:
                # using strip to delete the spaces at the beginning and end
                puzzle.append(list(line.strip()))
            else:
                if len(line.strip()) > 0:
                    words.append(line.strip())
    except FileNotFoundError:
        print("Sorry, the file doesn’t exist or cannot be opened.")
    return puzzle, words

def search_horizontal(puzzle, word):
    '''
    This function has two parameters. It searches for the specific
    words using a nested while loop. It iterates in each row, and search
    the word exists. It has an empty variable to find the words and store
    them in the variable, an empty list to save the word location in
    a tuple as (x,y). Each loop has a variable set to a zero, and each
    iteration is incremented by one. When it finshes looping it returns
    word_location and for the first loop it returns None.
    puzzle: a list that contains strings
    word: a string
    '''
    y = 0
    # Using while loop if the length of the puzzle is greater than y
    while len(puzzle) > y:
        x = 0
    # Using while loop if the length of the puzzle at index y is greater than x
        while (len(puzzle[y])) > x:
            i = 0
            word_find = ""
            word_location = []
    # While loop if the word's length that we are looking for is
    # greater or equal i
            while len(word) >= i:
                # x + i is less than the list the contains all the strings
                if x + i < len(puzzle[y]):
                    # add the letter into the word_find variable
                    word_find += puzzle[y][x + i]
                    # append the tuple that has location as (x,y) for each word
                    word_location.append((y, x + i))
                # check if the word matches left to right or right to left
                if word_find == word or word_find[::-1] == word:
                    return word_location
                i += 1
            x += 1
        y += 1
    return None


def search_diagonal_right_to_left(puzzle, word):
    '''
    This function has two parameters. It searches for the specific
    words using a nested while loop. It iterates in diagonal
    direcation from the right to left and search if the word exists.
    It has an empty variable to find the words and store
    them in the variable, an empty list to save the word location. Each
    loop has a variable set to a zero, and each iteration it decrementes
    by one. When it finshes looping it returns word_location and
    for the first loop it returns None.
    puzzle: a list that contains strings
    word: a string
    '''
    column = len(puzzle[0])
    # using while loop if the length of column greater than zero
    while column > 0:
        # using while loop if the length of row greater than zero
        row = len(puzzle)
        while row > 0:
            i = len(word)
            col_index = len(puzzle[0])
            word_find = ""
            word_location = []
            while i > 0:
                if row - i > 0:
                    # check if the puzzle at index row - i (word's length)
                    # is greater than col_index - column
                    if len(puzzle[row - i]) > col_index - column:
                        # add the letter that we looked for into word_find
                        word_find += puzzle[row - i][col_index - column]
                # append the tuple that has location as (x,y) for each word
                        word_location.append((row - i,  col_index - column))
                # check if the word matches left to right or right to left
                if word_find == word or word_find[::-1] == word:
                    return word_location
                i -= 1
                col_index -= 1
            row -= 1
        column -= 1
    return None


def search_diagonal_left_to_right(puzzle, word):
    '''
    This function has two parameters. It searches for the specific
    words using a nested while loop. It iterates in diagonal
    direcation from the left to right and search if the word exists.
    It has an empty variable to find the words and store
    them in the variable, an empty list to save the word location. Each
    loop has a variable set to a zero, and each iteration it incrementes
    by one. When it finshes looping it returns word_location and
    for the first loop it returns None.
    puzzle: a list that contains strings
    word: a string
    '''
    column = 0
    # Using while loop to check if each row in puzzle is greater than column
    while len(puzzle[0]) > column:
        row = 0
        # Using while loop if the length of row greater than row
        while len(puzzle) > row:
            i = 0
            column_index = 0
            word_find = ""
            word_location = []
            # Using while loop if the word's length greater or equal than i
            while len(word) >= i:
                if row + i < len(puzzle):
                    if len(puzzle[row + i]) > column + column_index:
                        # add the letter that we looked for into word_find
                        word_find += puzzle[row + i][column + column_index]
                        # append the tuple that has location as (x,y)
                        # for each word
                        word_location.append((row + i, column + column_index))
                # check if the word matches left to right or right to left
                if word_find == word or word_find[::-1] == word:
                    return word_location
                i += 1
                column_index += 1
            row += 1
        column += 1
    return None


def search_vertically(puzzle, word):
    '''
    This function will have two parameters. It searches for the specific
    words using a nested while loop. It iterates in each coulmn, and search
    the word exists. It has an empty variable to find the words and store
    them in the variable, an empty list to save the word location. each
    loop has a variable set to a zero, and each iteration is incremented
    by one. When it finshes looping it returns word_location and
    for the first loop it returns None.
    puzzle: a list that contains strings
    word: a string
    '''
    column = 0
    # Using while loop to check if each row in puzzle is greater than column
    while len(puzzle[0]) > column:
        row = 0
        # Using while loop if the length of row greater than row
        while len(puzzle) > row:
            i = 0
            word_find = ""
            word_location = []
            # Using while loop if the word's length greater or equal than i
            while len(word) >= i:
                # using if statement to check if row and i is less
                # than puzzle's length
                if row + i < len(puzzle):
                    # add the letter that we looked for into word_find
                    word_find += puzzle[row + i][column]
                    # append the tuple that has location as (x,y) for each word
                    word_location.append((row + i, column))
                # check if the word matches left to right or right to left
                if word_find == word or word_find[::-1] == word:
                    return word_location
                i += 1
            row += 1
        column += 1
    return None


def is_word_in_location(y, x, word_location):
    '''
    This funcation has three parameters. Uing if statement
    to check if word_location that contains the tuples in
    an array of the the word's locarion. if the there is
    nothing in word_location it retuns False. Otherwise,
    using for loop to check each tuple if the first index
    equals y and the sencon equals x return True.
    or it returns False.
    y: an integer
    x: an integer
    word_location : Array has a tuples as (x,y)
    '''
    if word_location is None:
        return False
    else:
        for word in word_location:
            if word[0] == y and word[1] == x:
                return True
    return False


def print_grid(puzzle, word_location):
    '''
    This function has two parameters. Using nested while loop
    to iterate over the length of the puzzle. Set y and x to
    zero. Has an empty sting to store the letter for each row.
    using while loop to check if the length of each row in puzzle
    is greater than x. Using if statement and calling the
    is_word_in_location function to check if the words we are looking
    for exist and add the letter to the line varible. Otherwise add
    dots inseted of the other random letter to complete the grid
    word_location : Array has a tuples as (x,y)
    puzzle: a list that contains strings
    '''
    y = 0
    while len(puzzle) > y:
        x = 0
        line = ""
        while (len(puzzle[y])) > x:
            # if we find the words in the function then print them out
            if is_word_in_location(y, x, word_location):
                line += puzzle[y][x]
            else:
                line += "."
            x += 1
        print(line + "\n")
        y += 1



if __name__ == '__main__':
    puzzle , words = process_data()
    # check horizontal first
    for word in words:
        word_location = search_diagonal_left_to_right(puzzle, word)
        if word_location is None:
            word_location = search_diagonal_right_to_left(puzzle, word)
        if word_location is None:
            word_location = search_horizontal(puzzle, word)
        if word_location is None:
            word_location = search_vertically(puzzle, word)
        if word_location is None:
            print("Word '" + word + "' not found")
        else:
            print_grid(puzzle, word_location)
