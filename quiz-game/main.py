import json
import os
import random
import rich

TERM_WIDTH = os.get_terminal_size().columns // 2 * 2
# nearest even integer less than or equal to terminal width

TOTAL_QUESTIONS = 5
# number of question which will be asked

SPC = " " # space
EMT = ""  # empty string
ULC = "╭" # upper left corner
URC = "╮" # upper right corner
LLC = "╰" # lower left corner
LRC = "╯" # lower right corner
VER = "│" # vertical bar
HOR = "─" # horizontal bar

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def format_row(text: str, width: int, label: str, color: str = "white"):
    rows, row, row_size = [], [], 0

    for word in text.split():
        if (row_size + len(word)) < width:
            row.append(word)
            row_size += len(word) + 1
        else:
            rows.append(" ".join(row))
            row = [word]
            row_size = len(word) + 1

    if len(row) > 0:
        rows.append(" ".join(row))

    upper_border  = f"{ULC}{(label.center(len(label) + 2)).center(width + 2, HOR)}{URC}"
    formatted_txt = [f"{VER} [{color}]{row.center(width)}[/{color}] {VER}" for row in rows]
    lower_border  = f"{LLC}{EMT.center(width + 2, HOR)}{LRC}"

    return [upper_border, *formatted_txt, lower_border]

def format_columns(columns: list, width: int, labels: list, colors: list):

    first_column  = format_row(columns[0], width, labels[0], colors[0])
    second_column = format_row(columns[1], width, labels[1], colors[1])

    if len(first_column) != len(second_column):
        d = len(first_column) - len(second_column)
        for _ in range(abs(d)):
            if d < 0:
                first_column.insert(-1, f"{VER}{EMT.center(width + 2)}{VER}")
            else:
                second_column.insert(-1, f"{VER}{EMT.center(width + 2)}{VER}")

    return [f"{first_columns_row}{second_column_row}" for first_columns_row, second_column_row in zip(first_column, second_column)]

def main():

    if TERM_WIDTH < 40:
        rich.print("[red]Warning: Width of terminal window is less than 40 columns[/red]")
        return

    with open("data.json", "r") as f:
        data = json.load(f)

    questions = random.sample(data, k=TOTAL_QUESTIONS)

    correct_answers = 0
    summary_color   = "green"

    for question_number, question in enumerate(questions, start=1):

        options_colors = ["white", "white", "white", "white"]

        clear_screen()

        # print summary
        rich.print("\n".join(format_row(f"{correct_answers} correct out of {question_number - 1} question{'s' * (question_number > 1)}", (TERM_WIDTH - 4), "SUMMARY", summary_color)))
        # print question
        rich.print("\n".join(format_row(question["Q"], (TERM_WIDTH - 4), "QUESTION", "violet")))
        # print first row of options
        rich.print("\n".join(format_columns([question["A"], question["B"]], ((TERM_WIDTH - 8) // 2), ["(A)", "(B)"], options_colors[:2])))
        # print second row of options
        rich.print("\n".join(format_columns([question["C"], question["D"]], ((TERM_WIDTH - 8) // 2), ["(C)", "(D)"], options_colors[2:])))

        answer = input("A B C D ? : ").strip()[0].upper()

        options_colors[ord(question["R"]) - ord("A")] = "green"

        if answer == question["R"]:
            correct_answers += 1
        else:
            options_colors[ord(answer) - ord("A")] = "red"

        summary_color = "green" if ((correct_answers / question_number) >= 0.5) else "red"

        clear_screen()

        # print summary
        rich.print("\n".join(format_row(f"{correct_answers} correct out of {question_number} question{'s' * (question_number > 1)}", (TERM_WIDTH - 4), "SUMMARY", summary_color)))
        # print question
        rich.print("\n".join(format_row(question["Q"], (TERM_WIDTH - 4), "QUESTION", "violet")))
        # print first row of options
        rich.print("\n".join(format_columns([question["A"], question["B"]], ((TERM_WIDTH - 8) // 2), ["(A)", "(B)"], options_colors[:2])))
        # print second row of options
        rich.print("\n".join(format_columns([question["C"], question["D"]], ((TERM_WIDTH - 8) // 2), ["(C)", "(D)"], options_colors[2:])))

        if question_number < TOTAL_QUESTIONS:
            input("press enter for next question : ")

    clear_screen()

    # print summary
    rich.print("\n".join(format_row(f"{correct_answers} correct out of {TOTAL_QUESTIONS} question{'s' * (question_number > 1)}", (TERM_WIDTH - 4), "SUMMARY", summary_color)))

if __name__ == "__main__":
    main()

# if answer is correct it is shown in green color
# if answer is wrong, it is shown in red and correct answer shown in green
# if number of correct questions >= 50% then summary is shown in green else in red