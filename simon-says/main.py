from time import sleep
from random import choice

def clear_screen():
    import os
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear_screen()
print("Let's play A Memory Game!\n")
print("A sequence of colors (R, G, B, Y) will be given to you.")
print("In each turn a random color is added to that sequence.")
print("You have to memorize that sequence in 3 seconds.")
print("After 3 seconds, sequence will be removed from screen.")
print("You need enter that sequence and press Enter [↵].\n")
input("Press Enter [↵] to play > ")

colors = ["R", "G", "B", "Y"]
score = 0
sequence = ""
response = ""

while True:
    sequence += choice(colors)
    clear_screen()
    print(sequence, end="", flush=True)
    sleep(5)
    clear_screen()
    response = input("> ")
    if response == sequence:
        score += 1
    else:
        break

print(f"\nOhh! It was \"{sequence}\".")
print(f"Your score is {score}.\n")