from random import choice

def clear_screen():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def valid(position, board):
    return (1 <= position <= 9) and (board[position - 1] not in ["X", "O"])

def updated(board, position, player):
    board[position - 1] = player
    return board 

def evaluate(board, player):
    if all([(board[i] in ["X", "O"]) for i in range(9)]):
        return None

    winner  = all([(board[i] == player) for i in [0, 1, 2]]) 
    winner |= all([(board[i] == player) for i in [3, 4, 5]])
    winner |= all([(board[i] == player) for i in [6, 7, 8]])
    winner |= all([(board[i] == player) for i in [0, 3, 6]])
    winner |= all([(board[i] == player) for i in [1, 4, 7]])
    winner |= all([(board[i] == player) for i in [2, 5, 8]])
    winner |= all([(board[i] == player) for i in [0, 4, 8]])
    winner |= all([(board[i] == player) for i in [2, 4, 6]])

    return winner
        
if __name__ == "__main__":
    board_entries  = [i for i in range(1, 10)]
    current_player = choice(["X", "O"])

    clear_screen()

    print("Welcome to The Tic-Tac-Toe Game!\n")
    print("You have to enter the number,")
    print("where you want place the X or O.\n")
    input("Press Enter [↵] to play > ")

    while True:
        clear_screen()
        print("\n".join([
            f" {board_entries[0]} │ {board_entries[1]} │ {board_entries[2]} ",
            f"───┼───┼───",
            f" {board_entries[3]} │ {board_entries[4]} │ {board_entries[5]} ",
            f"───┼───┼───",
            f" {board_entries[6]} │ {board_entries[7]} │ {board_entries[8]} ",
        ]))

        position = 0
        while not valid(position, board_entries):
            position = int(input(f"\n{current_player}'s turn > ").strip())

        board_entries = updated(board_entries, position, current_player)

        winner = evaluate(board_entries, current_player)

        if winner == True:
            clear_screen()
            print("\n".join([
                f" {board_entries[0]} │ {board_entries[1]} │ {board_entries[2]} ",
                f"───┼───┼───",
                f" {board_entries[3]} │ {board_entries[4]} │ {board_entries[5]} ",
                f"───┼───┼───",
                f" {board_entries[6]} │ {board_entries[7]} │ {board_entries[8]} ",
            ])) 
            print(f"\n{current_player} is a winner!\n")
            break

        if winner == None:
            clear_screen()
            print("\n".join([
                f" {board_entries[0]} │ {board_entries[1]} │ {board_entries[2]} ",
                f"───┼───┼───",
                f" {board_entries[3]} │ {board_entries[4]} │ {board_entries[5]} ",
                f"───┼───┼───",
                f" {board_entries[6]} │ {board_entries[7]} │ {board_entries[8]} ",
            ]))  
            print("\nIt's a draw!\n")
            break

        current_player = "X" if current_player == "O" else "O"