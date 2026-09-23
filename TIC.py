import random

board = [' ' for _ in range(9)]

def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(symbol):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == symbol:
            return True

    return False

def computer_move(symbol):
    empty = []

    for i in range(9):
        if board[i] == ' ':
            empty.append(i)

    position = random.choice(empty)
    board[position] = symbol

# Human chooses symbol
human = input("Choose X or O: ").upper()

if human == 'X':
    computer = 'O'
else:
    computer = 'X'

for turn in range(9):

    display_board()

    # Human move
    while True:
        position = int(input("Enter position (1-9): ")) - 1

        if board[position] == ' ':
            board[position] = human
            break
        else:
            print("Cell already occupied. Try again.")

    if check_winner(human):
        display_board()
        print("HUMAN WINS!")
        break

    if turn == 8:
        display_board()
        print("GAME DRAW!")
        break

    # Computer move
    computer_move(computer)

    print("Computer made its move.")

    if check_winner(computer):
        display_board()
        print("COMPUTER WINS!")
        break