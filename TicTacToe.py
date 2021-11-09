from IPython.display import clear_output
def tictactoe():

    print("Game is starting")
    play_again = True
    while play_again:
        clear_output(True)
        board = ['p', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        player = 1
        print("Player",player, "Select your marker : ")
        marker = input()
        player_1, player_2 = set_marker(marker)
        while True:
            if player > 2:
                player = 1
            print("Player", player, "Enter your position : ")
            pos = int(input())
            if check_pos(pos, board):
                continue
            if player == 1:
                set_board(board, player_1, pos)
            else:
                set_board(board, player_2, pos)
            display(board)
            if player == 1:
                if check_win(board, player_1):
                    print("Player ",player, " has won !")
                    break
            else:
                if check_win(board, player_2):
                    print("Player ",player, " has won !")
                    break
            if check_space(board):
                print("Draw !")
                break
            player += 1
        if replay():
            play_again = True



def set_marker(marker):
    if marker == "X" or "x":
        return("X", "O")
    else:
        return("O", "X")

    


def check_pos(pos, board):
    if board[pos] == " ":
        return False
    else:
        return True



def set_board(board, marker, pos):
    board[pos] = marker



def display(board):
    clear_output(True)
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print("-----------------")
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print("-----------------")
    print(f'{board[1]} | {board[2]} | {board[3]}')



def check_win(board, marker):
    return (board[1] == marker and board[2] == marker and board[3] == marker or
            board[4] == marker and board[5] == marker and board[6] == marker or
            board[7] == marker and board[8] == marker and board[9] == marker or
            board[1] == marker and board[4] == marker and board[7] == marker or
            board[2] == marker and board[5] == marker and board[8] == marker or
            board[3] == marker and board[6] == marker and board[9] == marker or
            board[1] == marker and board[5] == marker and board[9] == marker or
            board[3] == marker and board[5] == marker and board[7] == marker)



def check_space(board):
    if " " in board:
        return False
    else:
        return True



def replay():
    print("Do you want to play again ? Y/N")
    ans = input()
    if ans == "Y" or ans == "y":
        return True
    else:
        return False


tictactoe()