# Write your code here
import random  # Allows us to randomize starting word
'''
Take on the popular game Hangman
Eventually will include the following aspects
    In the main menu, a player can choose to either play or exit the game.
    If the user chooses to play, the computer picks a word from a list: this will be the answer to the puzzle.
    The computer asks the player to enter a letter that they think is in the word.
    If that letter does not appear in the word and this letter hasn't already been guessed, the computer counts it as a miss. A player can only afford 8 misses before the game is over.
    If the letter does occur in the word, the computer notifies the player. If there are letters left to guess, the computer invites the player to go on.
    When the entire word is uncovered, it's a victory! The game calculates the final score and returns to the main menu.

Adding the following functionality
    The game starts with a menu where a player can choose to either play or exit.
    Print Type "play" to play the game, "exit" to quit: and show this message again if the player inputs something else.
    If the user chooses to play, the game begins.
'''

def menu():
    game_state = input('Type "play" to play the game, "exit" to quit: ')  # Prompts the user if they would like to play the game or quit
    if game_state == 'play':  # If the user enters play, the game will begin
        game_start()

def game_start():
    hidden_words = ['python', 'java', 'kotlin', 'javascript']
    hidden_word = hidden_words[random.randint(0, len(hidden_words) - 1)]  # picks a random word
    word_display = ("-" * (len(hidden_word)))  # formats the word to provide a hint
    remaining_attempts = 8
    guessed_letters = []
    while remaining_attempts > 0:  # Looping structure until user is out of attempts
        print()
        print(f"{word_display}")  # display the word, hidden by "-"
        guess = input("Input a letter: ")  # Prompts user for a guess(with hint provided) and stores as a string
        guessed_letters.append(guess)  # Adds the users guess to guessed_letters along side the users previous attempts
        temp_display = hidden_word  # copy of hidden_word
        for letters in hidden_word:  # parses through every character in hidden_word
             if letters not in guessed_letters:  # boolean check if a character in hidden_word is a part of guessed_letters
                 temp_display = temp_display.replace(letters, "-")  #replaces every character that fulfils the above requirements with "-"
        word_display = temp_display  # overwrite what is display at the start of the loop
        if word_display == hidden_word:  # Checks if the user has solved the word, If so break out of loop
            break
        if len(guess) > 1:  # Checks if the input is multiple characters
            print("You should input a single letter")
        elif guessed_letters.count(guess) > 1:  # Checks if the input is in the previous guesses (current guess already appended to list)
            print("You've already guessed this letter")
        elif (not guess.isalpha() or guess.isupper()):  # Checks if the input is a valid character and in lower case format
            print("Please enter a lowercase English letter")
        elif guess not in hidden_word:  # Checks if the input is a part of the hidden word
            print("That letter doesn't appear in the word")
            remaining_attempts = remaining_attempts - 1  # Reduces remaining attempts

    if word_display == hidden_word:  # Win/Loss conditions as well as the resulting outputs
        print(word_display)
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You lost!")
    print()
    menu()  # Prompts the user if they would like ot play the game again


print("H A N G M A N")  #Formatting the title
menu()  # Initiating the game menu
