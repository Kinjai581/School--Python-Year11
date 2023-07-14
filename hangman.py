import random

def choose_random_word():
    words = ["apple", "banana", "cherry", "orange", "grape", "strawberry", "kiwi", "watermelon", "pear", "blueberry"]
    return random.choice(list(words))

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word_to_guess = choose_random_word()
    guessed_letters = set()
    max_attempts = 6
    attempts = 0

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while True:
        if "_" not in display_word(word_to_guess, guessed_letters):
            print("Congratulations, you've won! The word was:", word_to_guess)
            break

        if attempts == max_attempts:
            print("Game over! The word was:", word_to_guess)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("Correct guess!")
        else:
            attempts += 1
            print(f"Wrong guess! Attempts remaining: {max_attempts - attempts}")

        print(display_word(word_to_guess, guessed_letters))

if __name__ == "__main__":
    hangman()