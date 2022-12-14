# Problem Set 2, hangman.py
# Name: Catherine Li
# Collaborators:
# Time spent: idk

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word_list = []

    for letter in secret_word:
        secret_word_list.append(letter)

    common_letters = []

    for letter in secret_word:

        if letter in letters_guessed:
            common_letters.append(letter)

    if sorted(common_letters) == sorted(secret_word_list):
        return True

    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word = ''

    for letter in secret_word:

        if letter in letters_guessed:
            word += letter

        else:
            word += '_'

    return word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = string.ascii_lowercase
    available_letters = ''

    for letter in alphabet:

        if letter not in letters_guessed:
            available_letters += letter

    return available_letters


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    letters_guessed_clone = []
    len_secret_word = len(secret_word)

    loop = 0
    num_guesses_remaining = 6
    warnings = 3

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len_secret_word))
    print("You have 3 warnings left.")
    print("------------")

    while num_guesses_remaining > 0:

        if num_guesses_remaining > 1:
            print("You have {} guesses left.".format(num_guesses_remaining))

        else:
            print("You have {} guess left.".format(num_guesses_remaining))

        print("Available letters:", get_available_letters(letters_guessed))

        letter = input("Guess a letter: ").lower()
        print()

        if str.isalpha(letter):

            if len(letter) > 1:
                print("Oops! You entered too many letters.")

            if len(letter) == 1:
                letters_guessed.append(letter)

                if letter in secret_word:

                    if loop == 0:
                        print("Good guess:", get_guessed_word(secret_word, letters_guessed))

                    if loop >= 1:
                        letters_guessed_clone.append(letters_guessed[len(letters_guessed) - 2])

                        if letter in letters_guessed_clone:
                            if warnings > 0:
                                warnings -= 1
                                print("Oops! You've already guessed that letter.", end=" ")
                                if warnings == 1 or warnings == 0:
                                    print(
                                        "You have {} warning left: ".format(warnings))
                                else:
                                    print(
                                        "You have {} warnings left: ".format(warnings))
                                print("Word to guess:", get_guessed_word(secret_word, letters_guessed))
                            else:
                                num_guesses_remaining -= 1
                                print("You have no warnings left so you lose one guess:",
                                      get_guessed_word(secret_word, letters_guessed))
                        else:
                            print("Good guess:", get_guessed_word(secret_word, letters_guessed))

                else:
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))

                    if letter in "aeiou":
                        num_guesses_remaining -= 2
                    else:
                        num_guesses_remaining -= 1

        if not str.isalpha(letter):
            if warnings > 0:
                warnings -= 1
                print("Oops! That is not a valid letter.", end=" ")

                if warnings == 1 or warnings == 0:
                    print("You now have {} warning left: ".format(warnings))

                else:
                    print("You now have {} warnings left: ".format(warnings))

                print("Word to guess:", get_guessed_word(secret_word, letters_guessed))

            else:
                num_guesses_remaining -= 1
                print("You have no warnings left so you lose one guess:",
                      get_guessed_word(secret_word, letters_guessed))

        if warnings < 0:
            num_guesses_remaining -= 1
            print("You have no warnings left so you lose one guess:",
                  get_guessed_word(secret_word, letters_guessed))

        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            print("Your total score for this game is: {}".format(num_guesses_remaining * len(set(secret_word))))
            break

        loop += 1

        print("------------")

    else:
        print("Sorry, you ran out of guesses. The word was {}.".format(secret_word))


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)