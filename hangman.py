import random
import string

def choose_random_word():
    word_list = ['banana','giraffe','monkey','mouse','panda','kangaroo','scropion','lion','gorilla','cat','dog']
    return random.choice(word_list)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "-"
    return displayed_word

def hangman():
    secret_word = choose_random_word()
    guessed_letters = []
    guessed_vowels = []
    guesses_remaining = 6
    warnings_remaining = 3

    print("Welcome to Hangman!")
    print("I'm thinking of a word. Can you guess it?")
    print("The word has {} letters.".format(len(secret_word)))

    while guesses_remaining > 0:
        print("\nGuesses remaining: {}".format(guesses_remaining))
        print("Warnings remaining: {}".format(warnings_remaining))
        print("Letters not yet used: {}".format(" ".join(sorted(set(string.ascii_lowercase) - set(guessed_letters)))))
        print("Word: {}".format(display_word(secret_word, guessed_letters)))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Invalid input. You have {} warnings left.".format(warnings_remaining))
            else:
                guesses_remaining -= 1
                print("Invalid input. You lose a guess.")
        else:
            if guess in guessed_letters:
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    print("You've already guessed that letter. You have {} warnings left.".format(warnings_remaining))
                else:
                    guesses_remaining -= 1
                    print("You've already guessed that letter. You lose a guess.")
            else:
                guessed_letters.append(guess)
                if guess in secret_word:
                    print("Good guess: {}".format(display_word(secret_word, guessed_letters)))
                    if set(guessed_letters) == set(secret_word):
                        print("Congratulations! You've guessed the word: {}".format(secret_word))
                        score = guesses_remaining * len(set(secret_word))
                        print("Your score: {}".format(score))
                        return
                else:
                    print("Oops! That letter is not in the word.")
                    if guess in "aeiou":
                        guesses_remaining -= 2
                    else:
                        guesses_remaining -= 1

    print("You've run out of guesses. The word was: {}".format(secret_word))
    print("Better luck next time!")

if __name__ == "__main__":
    hangman()
