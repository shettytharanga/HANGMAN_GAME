import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():

    word = get_valid_word(words)
    word_letters = set(word)
    used_letters = set()
    alphabets = set(string.ascii_uppercase)
    lives = 6
    while len(word_letters) > 0 and lives > 0:
        print(f" You have {lives} lives and" ," You have used these letters : ", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word:", ' '.join(word_list))

        user_letter = input("guess a letter : ").upper()
        if user_letter in alphabets - used_letters:
             used_letters.add(user_letter)
             if user_letter in word_letters:
                 word_letters.remove(user_letter)
             else:
                 lives = lives - 1
                 print("That letter is not in the word.")

        elif user_letter in used_letters:
              print("you have already used that letter.")
        else:
            print("Invalid character. Please try again.")
    if lives == 0:
        print(f"you die . The correct word was {word}")
    else:
        print("yayyyy!! you guessed the word !!")

hangman()