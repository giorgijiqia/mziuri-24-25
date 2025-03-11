
import random

words = ['apple', 'banana', 'cherry', 'grape', 'orange', 'melon', 'peach', 'pear']

def jumble_word(word):
    word_list = list(word)
    random.shuffle(word_list)

    jumbled_word = ''
    for letter in word_list:
        jumbled_word += letter

    return jumbled_word

def play_word_jumble():

    while True:
        word = random.choice(words)
        jumbled_word = jumble_word(word)
        print("\nგადაწერილი სიტყვა:", jumbled_word)

        user_guess = input("გამოიცანი სიტყვა (დაწერე 'quit' გამოსასვლელად): ")

        if user_guess.lower() == 'quit':
            print("თამაში დასრულდა!")
            break

        elif user_guess.lower() == word:
            print("გილოცავთ! სწორად გამოიცანით სიტყვა.")
        else:
            print(f"არასწორი პასუხია. სწორია: {word}")

        continue_game = input("გსურთ თამაშის გაგრძელება? (yes/no): ")
        if continue_game.lower() != 'yes':
            print("თამაში დასრულდა!")
            break
play_word_jumble()