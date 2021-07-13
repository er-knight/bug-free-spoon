from random import randint

def clear_screen():
    import os
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def dice_roll():
    return randint(1, 6)

if __name__ == "__main__":
    stats = {
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0,
    }

    clear_screen()

    print("Let's do some analysis of dice rolls!\n")
    print("How many times you want to roll a die?")
    
    rounds = int(input("> ").strip())

    for _ in range(rounds):
        result = dice_roll()
        stats[result] += 1

    print()
    for number, count in stats.items():
        percentage = round(count / rounds * 100, 1)
        delta = round(percentage - (1 / 6 * 100), 1)
        print(f"{number}s {count:5.0f} times, {str(percentage).rjust(5)} % {str(delta).rjust(5)}")