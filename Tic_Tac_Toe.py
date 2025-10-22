board = [[" "," "," "],[" "," "," "],[" "," "," "]]
def show_board():
    for i in range(3):
        print("|".join(board[i]))
        print("_ _ _")

show_board()
