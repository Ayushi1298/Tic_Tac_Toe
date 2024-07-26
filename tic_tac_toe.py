import random
board=["-","-","-",
   "-","-","-",
   "-","-","-"]
winner=None
curr_player = "X"
game=True
def onBoard(board):
    print(board[0]+ " | " +board[1] + " | " + board[2])
    print("----------")
    print(board[3]+ " | " +board[4] + " | " + board[5])
    print("----------")
    print(board[6]+ " | " +board[7] + " | " + board[8])

def Input(board):

    inp=int (input("Enter the number between 1-9:"))
    if(inp>=1 and inp<=9 and board[inp-1]=="-"):
            board[inp - 1] = curr_player

    else:
        print("Slot already filled!!")

def checkwin():
    global game
    if(horizontal(board) or vertical(board) or diagonal(board)):
        onBoard(board)
        print("The winner is:"+ winner)
        game=False

def chechTie(board):
    global game
    if "-" not in board:
        onBoard(board)
        print("Game Tie!")
        game=False


def horizontal(board):
    global winner
    if ((board[0]==board[1]==board[2] )and (board[1]!="-")):
        winner=board[0]
        return True
    if ((board[3]==board[4]==board[5] )and (board[4]!="-")):
        winner=board[4]
        return True
    if ((board[6]==board[7]==board[8] )and (board[7]!="-")):
        winner=board[7]
        return True

def vertical(board):
    global winner
    if ((board[0] == board[3] == board[6]) and (board[3] != "-")):
        winner=board[3]
        return True
    if ((board[1] == board[4] == board[7]) and (board[4] != "-")):
        winner=board[4]
        return True
    if ((board[2] == board[5] == board[8]) and (board[5] != "-")):
        winner=board[5]
        return True
def diagonal(board):
    global winner
    if((board[0]==board[4]==board[8]) and (board[4]!="-")):
        winner = board[4]
        return True
    elif((board[2]==board[4]==board[6])and (board[4]!="-")):
        winner=board[4]
        return True

def switchplayer():
    global curr_player
    if curr_player=="X":
        curr_player="O"
    else:
        curr_player="X"

def second_player(board):
    while curr_player =="O":
        position=random.randint(0,8)
        if board[position]=="-":
            board[position]="O"
            switchplayer()
while game:
    onBoard(board)
    Input(board)
    checkwin()
    chechTie(board)
    switchplayer()
    second_player(board)









