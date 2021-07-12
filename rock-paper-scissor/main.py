from random import choice

def clear_screen():
    import os
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def winner(computer, player):      
    if computer == "rock" and player == "scissor":
        return "computer"
    elif player == "rock" and computer == "scissor":
        return "player"
    elif computer == "paper" and player == "rock":
        return "computer"
    elif player == "paper" and computer == "rock":
        return "player"
    elif computer == "scissor" and player == "paper":
        return "computer"
    elif player == "scissor" and computer == "paper":
        return "player"

    return "tie"

if __name__ == '__main__':
    stats = {
        "total"    : 0,
        "player"   : 0,
        "computer" : 0,
        "tie"      : 0
    }
    options = ["rock", "paper", "scissor"]

    clear_screen()

    print("Welcome to The Rock-Paper-Scissor Game!\n")
    print("You have to choose one, either Rock or Paper or Scissor.")
    print("Simultaneously, computer will also choose one of them.")
    print("If you want to quit, Enter \"quit\" and press Enter [↵].")
    print("\nWinner will be selected according to following rule.")
    print("Rock beats Scissor, Scissor beats Paper, Paper beats Rock.\n")

    while True:
        computer = choice(options)
        player   = input("> ").strip().lower()

        if player == "quit":
            break

        if player not in options:
            continue

        result = winner(computer, player)
        stats[result]  += 1
        stats["total"] += 1

        if result == "player":
            print("Yay! You won.")
        elif result == "computer":
            print("Ohh! You lost.")
        else:
            print("It's a tie!")

    print(f"\nAfter {stats['total']} round{'s' * (stats['total'] > 1)},")
    print(f"You won {stats['player']} time{'s' * (stats['player'] > 1)} & Computer won {stats['computer']} time{'s' * (stats['computer'] > 1)}.")  
    print(f"{stats['tie']} time{'s' * (stats['tie'] > 1)}, result was a Tie.")
    print(f"Your win percentage is {stats['player'] / stats['total'] * 100:.2f} %.\n")  

