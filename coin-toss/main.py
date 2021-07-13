from random import choice

def clear_screen():
    import os
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def coin_toss():
    return choice(["H", "T"])

if __name__ == "__main__":
    heads  = 0 
    tails  = 0

    clear_screen()
    
    print("Let's do some analysis of coin toss!\n")
    print("How many times you want to toss a coin?")
    
    rounds = int(input("> ").strip())

    for _ in range(rounds):
        result = coin_toss()
        if result == "H":
            heads += 1
        else:
            tails += 1

    head_percentage = round(heads / rounds * 100, 1)
    head_delta      = round(head_percentage - 50.00, 1)
    tail_percentage = round(tails / rounds * 100, 1)
    tail_delta      = round(tail_percentage - 50.00, 1)

    print()
    print(f"Heads {heads} times {str(head_percentage).rjust(5)} % {str(head_delta).rjust(5)}")
    print(f"Tails {tails} times {str(tail_percentage).rjust(5)} % {str(tail_delta).rjust(5)}")
