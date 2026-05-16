# Create empty board
board = [" "] * 9


# Function to display board
def show():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])


# Function to check winner
def check(player):

    win = [
        (0,1,2), (3,4,5), (6,7,8),   # Rows
        (0,3,6), (1,4,7), (2,5,8),   # Columns
        (0,4,8), (2,4,6)             # Diagonals
    ]

    for x in win:
        if board[x[0]] == board[x[1]] == board[x[2]] == player:
            return True

    return False


# Main game loop
for i in range(9):

    show()

    # Human move
    move = int(input("Enter position (1-9): ")) - 1
    board[move] = "X"


    # Check Human win
    if check("X"):
        show()
        print("Human Wins!")
        break


    # Check draw
    if " " not in board:
        show()
        print("Draw!")
        break


    # Computer move
    for j in range(9):

        if board[j] == " ":
            board[j] = "O"
            break


    # Check Computer win
    if check("O"):
        show()
        print("Computer Wins!")
        break
