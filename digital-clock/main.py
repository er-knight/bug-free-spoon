from datetime import datetime

def clear_screen():
    import os
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def time_str(hours, minutes):
    digit_str = {
        "0" : {
            "1st" : "╭──╮",
            "2nd" : "│  │",
            "3rd" : "╰──╯"
        },
        "1" : {
            "1st" : "  ╷",
            "2nd" : "  │",
            "3rd" : "  ╵"
        },
        "2" : {
            "1st" : " ──╮",
            "2nd" : "╭──╯",
            "3rd" : "╰── "
        },
        "3" : {
            "1st" : " ──╮",
            "2nd" : " ──┤",
            "3rd" : " ──╯"
        },
        "4" : {
            "1st" : "╷  ╷",
            "2nd" : "╰──┤",
            "3rd" : "   ╵"
        },
        "5" : {
            "1st" : "╭── ",
            "2nd" : "╰──╮",
            "3rd" : " ──╯"
        },
        "6" : {
            "1st" : "╭── ",
            "2nd" : "├──╮",
            "3rd" : "╰──╯"
        },
        "7" : {
            "1st" : " ──╮",
            "2nd" : "   │",
            "3rd" : "   ╵"
        },
        "8" : {
            "1st" : "╭──╮",
            "2nd" : "├──┤",
            "3rd" : "╰──╯"
        },
        "9" : {
            "1st" : "╭──╮",
            "2nd" : "╰──┤",
            "3rd" : " ──╯"
        }
    }

    first_row, second_row, third_row = [], [], []   

    for digit in hours:
        first_row.append(digit_str[digit]["1st"])
        second_row.append(digit_str[digit]["2nd"])
        third_row.append(digit_str[digit]["3rd"])

    first_row.append(" ╷ ")
    second_row.append("   ")
    third_row.append(" ╵ ")

    for digit in minutes:
        first_row.append(digit_str[digit]["1st"])
        second_row.append(digit_str[digit]["2nd"])
        third_row.append(digit_str[digit]["3rd"])
    
    return "\n".join([
        " " + " ".join(first_row),
        " " + " ".join(second_row),
        " " + " ".join(third_row)
    ]) + "\n"

if __name__ == "__main__":
    hours, minutes = datetime.now().strftime("%I %M").split()

    clear_screen()

    print(time_str(hours, minutes))

#    ╷ ╭──╮  ╷   ──╮ ╭──╮
#    │ │  │     ╭──╯ │  │
#    ╵ ╰──╯  ╵  ╰──  ╰──╯