from random import choice, shuffle

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

def jumbled(word):
    word = list(word)
    shuffle(word)
    return "".join(word)

if __name__ == "__main__":
    clear_screen()

    print("Welcome to The Jumble Game!\n")
    print("A word will be given to you,")
    print("but it's letters are jumbled.")
    print("Can you guess the original word?\n")
    input("Press Enter [↵] to play > ")

    clear_screen()

    original_word = get_random_word()
    jumbled_word  = jumbled(original_word)

    print(f"Jumbled word : {jumbled_word}")
    guess = input("Your guess   : ").strip()

    if guess == original_word:
        print("\nYay! You guessed it.\n")
    else:
        print(f"\nNo! It was \"{original_word}\".\n")