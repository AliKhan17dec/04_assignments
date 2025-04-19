import random
import string  # Needed for string.ascii_uppercase
from words import words  # Import the list named 'words' from words.py

print(words)

def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()  # Optional: convert to uppercase for consistent comparison

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Not words!
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    print("Let's play Hangman!")

    while len(word_letters) > 0:
        print('You have used these letters: ', ' '.join(used_letters))
        print('Current word: ', ' '.join([letter if letter in used_letters else '_' for letter in word]))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                print('Letter is not in word.')
        elif user_letter in used_letters:
            print('You have already used that letter.')
        else:
            print('Invalid character. Please try again.')

    print(f'🎉 You guessed the word {word} correctly!')

# Run the game
hangman()

# Optional: separate test input if needed
# user_input = input('Type something: ')
# print(user_input)
