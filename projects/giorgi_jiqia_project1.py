import random

def choose_word():
    words = ['cat', 'dog', 'fish', 'bird', 'apple', 'python', 'hangman', 'computer', 'programming', 'developer', 'software', 'algorithm']
    return random.choice(words)

def display(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    hangman_parts = [
        """
         -----
         |   |
             |
             |
             |
             |
        """,
        """
         -----
         |   |
         O   |
             |
             |
             |
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        """,
        """
         -----
         |   |
         O   |
        /|\  |
             |
             |
        """,
        """
         -----
         |   |
         O   |
        /|\  |
        /    |
             |
        """,
        """
         -----
         |   |
         O   |
        /|\  |
        / \  |
             |
        """
    ]

    print("Welcome to Hangman!")
    print("Guess the word!")

    while attempts > 0:
        print("\nWord: ", display(word, guessed_letters))
        print("Guessed Letters: ", guessed_letters)
        print(f"Attempts Left: {attempts}")
        print(hangman_parts[6 - attempts])

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word!")
        else:
            print(f"Oops! '{guess}' is not in the word.")
            attempts -= 1

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(f"Game Over! The word was: {word}")


hangman()