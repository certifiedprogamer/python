import random
# Create and return a new list representing the board with indices 0 to 8.


def initialize_board():
    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    return board
# Display the current state of the board, showing 'X' or 'O' in place of the numbers.


def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Place the player's symbol ('X' or 'O') at the specified index on the board.


def make_move(board, index, player):
    board[int(index)] = player
    return board

# Determine if there is a winner. Return the winning symbol ('X' or 'O') or None if there is no winner yet.


def check_winner(board):

    # Check if player wins
    if board[0] == "X" and board[1] == "X" and board[2] == "X" or board[3] == "X" and board[4] == "X" and board[5] == "X" or board[6] == "X" and board[7] == "X" and board[8] == "X":
        return "X"
    elif board[0] == "X" and board[4] == "X" and board[8] == "X" or board[2] == "X" and board[4] == "X" and board[6] == "X":
        return "X"
    elif board[0] == "X" and board[3] == "X" and board[6] == "X" or board[1] == "X" and board[4] == "X" and board[7] == "X" or board[2] == "X" and board[5] == "X" and board[8] == "X":
        return "X"

    # Check if computer wins
    elif board[0] == "O" and board[1] == "O" and board[2] == "O" or board[3] == "O" and board[4] == "O" and board[5] == "O" or board[6] == "O" and board[7] == "O" and board[8] == "O":
        return "O"
    elif board[0] == "O" and board[4] == "O" and board[8] == "O" or board[2] == "O" and board[4] == "O" and board[6] == "O":
        return "O"
    elif board[0] == "O" and board[3] == "O" and board[6] == "O" or board[1] == "O" and board[4] == "O" and board[7] == "O" or board[2] == "O" and board[5] == "O" and board[8] == "O":
        return "O"
    else:
        return "nah"
# Determine if the game is a draw (i.e., the board is full and there is no winner).


def check_draw(board):

    # assumes board is made of 0-9
    for cell in board:
        if cell not in ["X", "O"]:
            return False
    print("It's a draw!")
    return True

# Handle the move of the human player, including input validation.


def player_move(board):
    while True:
        move = (
            input("Enter the index of the part of the board you want to claim (0-8): "))

        if move in board and move != "X" and move != "O":
            return move
        else:
            print("Index has either already been claimed or is invalid.")

# Handle the move of the computer, using a basic strategy like random moves.


def computer_move(board):
    while True:
        move = str(random.randint(0, 8))
        if move in board:
            print(f"The computer has taken index {move}")
            return move
        else:
            if check_draw(board):
                break

# Manage the game loop, alternating between the player and computer, checking for a win or draw, and announcing the result.


def play_game():
    current_board = initialize_board()
    winner = False
    print_board(current_board)
    while True:

        turn = "X"
        player_choice = player_move(current_board)
        current_board = make_move(current_board, player_choice, turn)
        print_board(current_board)
        winner = check_winner(current_board)
        if winner in ("O", "X"):
            print(f" {winner} wins!")
            break
        elif check_draw(current_board):
            break

        turn = "O"
        computer_choice = computer_move(current_board)
        current_board = make_move(current_board, computer_choice, turn)
        print_board(current_board)
        winner = check_winner(current_board)
        if winner in ("O", "X"):
            print(f" {winner} wins!")
            break
        elif check_draw(current_board):
            break


if __name__ == '__main__':
    while True:
        play_game()
        play = input(
            "Would you like to play again? (enter \"y\" to say yes, enter anything else to say no.)")
        if play != "y" or play != "Y":
            break
