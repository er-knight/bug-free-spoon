import random
import json

def clear_screen():
    import os
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_random_quote():
    with open("quotes.json", "r") as f:
        quotes = json.load(f)

    quote = random.choice(quotes)
    return quote["text"], quote["author"]

def prettified(quote, author):
    width = 50
    words = quote.split()
    lines = []
    line  = []
    length = 0
    for word in words:
        if (length + len(word)) < width:
            line.append(word)
            length += len(word) + 1
        else:
            lines.append(" ".join(line))
            line = [word]
            length = len(word) + 1
    
    if len(line) > 0:
        lines.append(" ".join(line))

    upper_border = f" ╭─{'─' * width}─╮"

    prettified_quote = [f" │ {line.ljust(width)} │" for line in lines]
    
    prettified_author = f" │ {('~ ' + author).rjust(width)} │"
    
    lower_border = f" ╰─{'─' * width}─╯"

    return "\n".join([upper_border, *prettified_quote, prettified_author, lower_border]) + "\n"

if __name__ == "__main__":
    quote, author = get_random_quote()

    clear_screen()

    print(prettified(quote, author))

#  ╭────────────────────────────────────────────────────╮
#  │ Time stays long enough for anyone who will use     │
#  │ it.                                                │
#  │                                ~ Leonardo da Vinci │
#  ╰────────────────────────────────────────────────────╯
