import random
import json

def clear_screen():
    import os
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def show_plays_card(plays_card):
    plays_card = [
        f" ╭─────────────────────╮",
        f" │ {plays_card['name'].upper().center(19)} │",
        f" ├──────────────┬──────┤",
        f" │ [1] HP       │ {plays_card['hp']:4.0f} │",
        f" ├──────────────┼──────┤",
        f" │ [2] ATTACK   │ {plays_card['attack']:4.0f} │",
        f" ├──────────────┼──────┤",
        f" │ [3] DEFENSE  │ {plays_card['defense']:4.0f} │",
        f" ├──────────────┼──────┤",
        f" │ [4] ATTACK+  │ {plays_card['attack+']:4.0f} │",
        f" ├──────────────┼──────┤",
        f" │ [5] DEFENSE+ │ {plays_card['defense+']:4.0f} │",
        f" ├──────────────┼──────┤",
        f" │ [6] SPEED    │ {plays_card['speed']:4.0f} │",
        f" ╰──────────────┴──────╯"
    ]
    oppos_card = [
        f"╭─────────────────────╮",
        f"│ ░░░░░░░░░░░░░░░░░░░ │",
        f"├──────────────┬──────┤",
        f"│ [1] HP       │ ░░░░ │",
        f"├──────────────┼──────┤",
        f"│ [2] ATTACK   │ ░░░░ │",
        f"├──────────────┼──────┤",
        f"│ [3] DEFENSE  │ ░░░░ │",
        f"├──────────────┼──────┤",
        f"│ [4] ATTACK+  │ ░░░░ │",
        f"├──────────────┼──────┤",
        f"│ [5] DEFENSE+ │ ░░░░ │",
        f"├──────────────┼──────┤",
        f"│ [6] SPEED    │ ░░░░ │",
        f"╰──────────────┴──────╯"
    ]
    print("\n".join([
        plays_card[i] + "    "  + oppos_card[i] for i in range(len(plays_card))
    ]))

def show_oppos_card(plays_card, oppos_card, option):
    plays_card = [
        f" ╭─────────────────────╮",
        f" │ {plays_card['name'].upper().center(19)} │",
        f" ├──────────────┬──────┤",
        f" │ [1] HP       │ {plays_card['hp']:4.0f} │",
        f" ├──────────────┼──────┤",
        f" │ [2] ATTACK   │ {plays_card['attack']:4.0f} │",
        f" ├──────────────┼──────┤",
        f" │ [3] DEFENSE  │ {plays_card['defense']:4.0f} │",
        f" ├──────────────┼──────┤",
        f" │ [4] ATTACK+  │ {plays_card['attack+']:4.0f} │",
        f" ├──────────────┼──────┤",
        f" │ [5] DEFENSE+ │ {plays_card['defense+']:4.0f} │",
        f" ├──────────────┼──────┤",
        f" │ [6] SPEED    │ {plays_card['speed']:4.0f} │",
        f" ╰──────────────┴──────╯"
    ]
    oppos_card = [
        f"╭─────────────────────╮",
        f"│ {oppos_card['name'].upper().center(19)} │",
        f"├──────────────┬──────┤",
        f"│ [1] HP       │ {oppos_card['hp']:4.0f} │",
        f"├──────────────┼──────┤",
        f"│ [2] ATTACK   │ {oppos_card['attack']:4.0f} │",
        f"├──────────────┼──────┤",
        f"│ [3] DEFENSE  │ {oppos_card['defense']:4.0f} │",
        f"├──────────────┼──────┤",
        f"│ [4] ATTACK+  │ {oppos_card['attack+']:4.0f} │",
        f"├──────────────┼──────┤",
        f"│ [5] DEFENSE+ │ {oppos_card['defense+']:4.0f} │",
        f"├──────────────┼──────┤",
        f"│ [6] SPEED    │ {oppos_card['speed']:4.0f} │",
        f"╰──────────────┴──────╯"
    ]
    print("\n".join([
        plays_card[i] + (" ←→ " if i == (option * 2) + 1 else "    ")  + oppos_card[i] for i in range(len(plays_card))
    ]))

def differ(plays_card, oppos_card, option):
    if option == 1:
        return (plays_card["hp"] - oppos_card["hp"])
    elif option == 2:
        return (plays_card["attack"] - oppos_card["attack"])
    elif option == 3:
        return (plays_card["defense"] - oppos_card["defense"])
    elif option == 4:
        return (plays_card["attack+"] - oppos_card["attack+"])
    elif option == 5:
        return (plays_card["defense+"] - oppos_card["defense+"])
    else:
        return (plays_card["speed"] - oppos_card["speed"])

def oppos_choice(oppos_card):
    options = { 
        1 : oppos_card["hp"], 
        2 : oppos_card["attack"], 
        3 : oppos_card["defense"], 
        4 : oppos_card["attack+"], 
        5 : oppos_card["defense+"], 
        6 : oppos_card["speed"]
    }

    return random.choice([option for option in options if options[option] == max(options.values())])

def scorecard(rounds, points):
    return "\n".join([
        f" ╭──────────────────╮",
        f" │ {(str(rounds) + ' ROUNDS').center(16)} │",
        f" ├──────────┬───────┤",
        f" │ PLAYER   │ {points['player']:5.0f} │",
        f" ├──────────┼───────┤",
        f" │ OPPONENT │ {points['opponent']:5.0f} │",
        f" ╰──────────┴───────╯"
    ])

if __name__ == "__main__":

    with open("pokemons.json", "r") as f:
        pokemons = json.load(f)

    cards = [pokemon for pokemon in pokemons]

    pickedcards = random.sample(cards, k=30)
    plays_cards = pickedcards[:15]
    oppos_cards = pickedcards[15:]

    points = {
        "player"   : 0,
        "opponent" : 0
    }

    round_number = 1

    while plays_cards and oppos_cards:
        plays_card = random.choice(plays_cards)
        oppos_card = random.choice(oppos_cards)

        oppos_cards.remove(oppos_card)
        plays_cards.remove(plays_card)

        clear_screen()
        show_plays_card(plays_card)

        option = None
        if round_number % 2:
            option = input("player   > ").strip()
            if option.isdecimal():
                option = int(option)
            else:
                break
        else:
            option = oppos_choice(oppos_card)
            input(f"opponent > {option}")

        differs = differ(plays_card, oppos_card, option)

        if differs > 0:
            points["player"] += differs
            clear_screen()
            show_oppos_card(plays_card, oppos_card, option)
            input(f"> You won by {differs} points.")
        elif differs < 0:
            differs = abs(differs)
            points["opponent"] += differs
            clear_screen()
            show_oppos_card(plays_card, oppos_card, option)
            input(f"> You lost by {differs} points.")
        else:
            clear_screen()
            show_oppos_card(plays_card, oppos_card, option)
            input(f"> It's a tie.")

        round_number += 1

    clear_screen()
    print(scorecard(round_number - 1, points))

#  ╭─────────────────────╮    ╭─────────────────────╮
#  │       SWELLOW       │    │ ░░░░░░░░░░░░░░░░░░░ │
#  ├──────────────┬──────┤    ├──────────────┬──────┤
#  │ [1] HP       │   60 │    │ [1] HP       │ ░░░░ │
#  ├──────────────┼──────┤    ├──────────────┼──────┤
#  │ [2] ATTACK   │   85 │    │ [2] ATTACK   │ ░░░░ │
#  ├──────────────┼──────┤    ├──────────────┼──────┤
#  │ [3] DEFENSE  │   60 │    │ [3] DEFENSE  │ ░░░░ │
#  ├──────────────┼──────┤    ├──────────────┼──────┤
#  │ [4] ATTACK+  │   75 │    │ [4] ATTACK+  │ ░░░░ │
#  ├──────────────┼──────┤    ├──────────────┼──────┤
#  │ [5] DEFENSE+ │   50 │    │ [5] DEFENSE+ │ ░░░░ │
#  ├──────────────┼──────┤    ├──────────────┼──────┤
#  │ [6] SPEED    │  125 │    │ [6] SPEED    │ ░░░░ │
#  ╰──────────────┴──────╯    ╰──────────────┴──────╯
# player   > 6

#  ╭─────────────────────╮    ╭─────────────────────╮
#  │       SWELLOW       │    │       DONPHAN       │
#  ├──────────────┬──────┤    ├──────────────┬──────┤
#  │ [1] HP       │   60 │    │ [1] HP       │   90 │
#  ├──────────────┼──────┤    ├──────────────┼──────┤
#  │ [2] ATTACK   │   85 │    │ [2] ATTACK   │  120 │
#  ├──────────────┼──────┤    ├──────────────┼──────┤
#  │ [3] DEFENSE  │   60 │    │ [3] DEFENSE  │  120 │
#  ├──────────────┼──────┤    ├──────────────┼──────┤
#  │ [4] ATTACK+  │   75 │    │ [4] ATTACK+  │   60 │
#  ├──────────────┼──────┤    ├──────────────┼──────┤
#  │ [5] DEFENSE+ │   50 │    │ [5] DEFENSE+ │   60 │
#  ├──────────────┼──────┤    ├──────────────┼──────┤
#  │ [6] SPEED    │  125 │ ←→ │ [6] SPEED    │   50 │
#  ╰──────────────┴──────╯    ╰──────────────┴──────╯
# > You won by 75 points.

#  ╭─────────────────────╮    ╭─────────────────────╮
#  │      BOUNSWEET      │    │ ░░░░░░░░░░░░░░░░░░░ │
#  ├──────────────┬──────┤    ├──────────────┬──────┤
#  │ [1] HP       │   42 │    │ [1] HP       │ ░░░░ │
#  ├──────────────┼──────┤    ├──────────────┼──────┤
#  │ [2] ATTACK   │   30 │    │ [2] ATTACK   │ ░░░░ │
#  ├──────────────┼──────┤    ├──────────────┼──────┤
#  │ [3] DEFENSE  │   38 │    │ [3] DEFENSE  │ ░░░░ │
#  ├──────────────┼──────┤    ├──────────────┼──────┤
#  │ [4] ATTACK+  │   30 │    │ [4] ATTACK+  │ ░░░░ │
#  ├──────────────┼──────┤    ├──────────────┼──────┤
#  │ [5] DEFENSE+ │   38 │    │ [5] DEFENSE+ │ ░░░░ │
#  ├──────────────┼──────┤    ├──────────────┼──────┤
#  │ [6] SPEED    │   32 │    │ [6] SPEED    │ ░░░░ │
#  ╰──────────────┴──────╯    ╰──────────────┴──────╯
# opponent > 4

#  ╭─────────────────────╮    ╭─────────────────────╮
#  │      BOUNSWEET      │    │       VIKAVOLT      │
#  ├──────────────┬──────┤    ├──────────────┬──────┤
#  │ [1] HP       │   42 │    │ [1] HP       │   77 │
#  ├──────────────┼──────┤    ├──────────────┼──────┤
#  │ [2] ATTACK   │   30 │    │ [2] ATTACK   │   70 │
#  ├──────────────┼──────┤    ├──────────────┼──────┤
#  │ [3] DEFENSE  │   38 │    │ [3] DEFENSE  │   90 │
#  ├──────────────┼──────┤    ├──────────────┼──────┤
#  │ [4] ATTACK+  │   30 │ ←→ │ [4] ATTACK+  │  145 │
#  ├──────────────┼──────┤    ├──────────────┼──────┤
#  │ [5] DEFENSE+ │   38 │    │ [5] DEFENSE+ │   75 │
#  ├──────────────┼──────┤    ├──────────────┼──────┤
#  │ [6] SPEED    │   32 │    │ [6] SPEED    │   43 │
#  ╰──────────────┴──────╯    ╰──────────────┴──────╯
# > You lost by 115 points.

#  ╭──────────────────╮
#  │     2 ROUNDS     │
#  ├──────────┬───────┤
#  │ PLAYER   │    75 │
#  ├──────────┼───────┤
#  │ OPPONENT │   115 │
#  ╰──────────┴───────╯
