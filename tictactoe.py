# cse210-01
#First assignment


def main():
    # player1 = input("First player: ")
    # player2 = input("Second player: ")
    print("\nThis tictactoe game is similar to real life, if you really wanted to, \nyou could erase your partners selection and put yours in place of it...\nbe sure to watch out for the deception or use the honor system\n")
    board = [1,2,3,4,5,6,7,8,9]
    while not game_over(board) or tie(board):
        show_board(board)
        move1 = int(input("Where would X like to move: "))
        board[move1 -1] = "X"
        if not game_over(board) or tie(board):
            show_board(board)
            move2 = int(input("Where would O like to move: "))
            board[move2 -1] = "O"

def game_over(board):
    if (board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or
        board[0] == board[3] == board[6] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8] or
        board[0] == board[4] == board[8] or
        board[2] == board[4] == board[6]):
        print("Winner!")
        return True
def tie(board):   
    for i in range(9):
        if board[i] != "X" or board[i] != "O":
            return False
        else:
            print("draw")
            return True 


def show_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}\n{board[3]}|{board[4]}|{board[5]}\n{board[6]}|{board[7]}|{board[8]}")





if __name__ == "__main__":
    main()

