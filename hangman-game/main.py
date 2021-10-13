from random import choice

def clear_screen():
    import os
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_random_word():
    with open("words.txt", "r") as f:
        words = f.read().split()

    return choice(words)

if __name__ == '__main__':
    clear_screen()

    print("Welcome to The Hangman Game!\n")
    print("Computer will choose a random word from a list.")
    print("You have type a letter (one at a time),") 
    print("which you think may be present in the word.\n")
    input("Press Enter [↵] to play > ")

    clear_screen()

    rounds_remaining = 5
    word_to_guess    = get_random_word()
    length           = len(word_to_guess)
    guessed_word     = "_" * length
    used_letters     = set()

    print(f"{guessed_word}\n")
    print(f"Lives remaining : {rounds_remaining}")
    print("Used letters    :", *used_letters)

    while rounds_remaining:
        guessed_letter = input("> ").strip()
        used_letters.add(guessed_letter)

        if guessed_letter in word_to_guess:
                temp = ""
                for i in range(len(word_to_guess)):
                    if (word_to_guess[i] == guessed_word[i]):
                        temp += word_to_guess[i]
                    elif (word_to_guess[i] == guessed_letter):
                        temp += word_to_guess[i]
                    else:
                        temp += "_"

                guessed_word = temp
        else:
            rounds_remaining -= 1

        clear_screen()

        print(f"{guessed_word}\n")
        print(f"Lives remaining : {rounds_remaining}")
        print("Used letters    :", *used_letters)

        if guessed_word == word_to_guess:
            print("\nYay! You guessed it.\n")
            break

    else:
        print("\nOhh no! Game Over.") 
        print(f"The word was \"{word_to_guess}\".\n")
