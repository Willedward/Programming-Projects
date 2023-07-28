## Tic Tac Toe

count = 0
board = [['', '', ''], ['', '', ''], ['', '', '']]
ai = 'O'
p2 = 'X'
namewinner = ""
currentplayer = ai

def checkwin():
    #winner = False
    namewinner = "null"
    #x
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != '':
            namewinner = board[i][0]
    
    
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != '':
            namewinner = board[0][i]
    
    #diagonals
    
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != '':
        namewinner = board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != '':
        namewinner = board[0][2]
    win = namewinner
    os = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                os += 1
    if namewinner == "null" and os == 0:
        k = "tie"
        return k
    else:
        return win


def available(board, plot):
    if board[plot[0]][plot[1]] == '':
        return True
    else:
        return False

def bestMove():
    best_score = -100000000
    bestmove = None
    for i in range(3):
        for j in range(3):
            
            if available(board, (i, j)):
                board[i][j] = ai
                
                score = minimax(board, 0, False)
            
                board[i][j] = ''
                if score > best_score:
                    best_score = score
                    bestmove = (i, j)
                #print(str(available(board, (i, j))) + " "+ str(i) + " "+ str(j))
                #print(best_score)
    currentplayer = p2
    board[bestmove[0]][bestmove[1]] = "O"
    return bestmove

scores = {
    "X" : -10,
    "O" : 10,
    "tie" : 0
}

def minimax(board, d, isMax):
    res = checkwin()
    if res != "null":
        sc = scores[res]
        return sc
    if isMax == True:
        bestscore1 = -100000000
       # print("Flagmax" + str(depth))
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = ai
                    score2 = minimax(board, d+1, False)
                    board[i][j] = ''
                    if score2 > bestscore1:
                        bestscore1 = score2
        #print("bestscore1: ")
        #print(bestscore1)
        return bestscore1
    else:
        #print("flagmin" + str(depth))
        bestscore1 = 1000000000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = p2
                    score2 = minimax(board, d+1, True)
                    board[i][j] = ''
                    if score2 < bestscore1:
                        bestscore1 = score2
        #print("bs: ")
        #print(bestscore2)
        return bestscore1



b = [" ", " ", " ", " "," "," "," "," "," "]
def printboard():
    #print(" |   | ")
    print(' '+board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    #print(" |   | ")
    print("-----------")
    print(' '+ board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    #print(" |   | ")
    print("-----------")
    #print(" |   | ")
    print(' '+board[2][0] + " | " + board[2][1] + " | " + board[2][2])
    #print(" |   | ")
#print(printboard())
print(' '+"1" + " | " + "2" + " | " + "3")
    #print(" |   | ")
print("-----------")
print(' '+ "4" + " | " + "5" + " | " + "6")
    #print(" |   | ")
print("-----------")
    #print(" |   | ")
print(' '+ "7" + " | " + "8" + " | " + "9")






while count < 9:
    if currentplayer == p2:
        x = int(input("Please click position 1-9: "))
        y = x-1
        xy = (y//3, y%3)
        while available(board, xy) == False:
            x = int(input("Please click a vaccant position 1-9: "))
            y = x-1
            xy = (y//3, y%3)
        board[xy[0]][xy[1]] = "X"
        b[x-1] = "X"
        currentplayer = ai
        printboard()
        z = checkwin()
        if z == "X":
            print("Player Wins!")
            break        
        
    elif currentplayer == ai:
        bestMove()
        currentplayer = p2
        #print("yz: ")
        print()
        print("AI: ")
        printboard()
        z = checkwin()
        if z == "O":
            print("AI wins")
            break
    count+=1
    #print(count)
    #print(board)
    if count == 9:
        print("tie!!")
        break
