## Tic Tac Toe
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Tictactoe")
root.iconbitmap('c:/gui')

# X starts so true
clicked = True
count = 0
board = [[' ', '', ''], ['', '', ''], ['', '', '']]
ai = 'O'
p2 = 'X'
global winner
#namewinner = ""
#messagebox.showinfo("Tictactoe", "Congratulations, X wins!")
currentplayer = "Human"
def checkwin():
    winner = False
    namewinner = " "
    #x
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        winner = True
        namewinner = "X"
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        winner = True
        namewinner = "X"
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        winner = True
        namewinner = "X"
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        winner = True
        namewinner = "X"
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        winner = True
        namewinner = "X"
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        winner = True
        namewinner = "X"
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        winner = True
        namewinner = "X"
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        winner = True
        namewinner = "X"
    #o
    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        winner = True
        namewinner = "O"
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        winner = True
        namewinner = "O"
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        winner = True
        namewinner = "O"
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        winner = True
        namewinner = "O"
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        winner = True
        namewinner = "O"
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        winner = True
        namewinner = "O"
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        winner = True
        namewinner = "O"
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        winner = True
        namewinner = "O"
    elif count == 9:
        Winner = True
        namewinner = "null"
    win = namewinner
    return win


# button click function
def b_click(b):
    global clicked, count
    if b["text"] == " " and clicked == True:
        b["text"] =  "X"
        clicked = False
        count+=1
        if checkwin() == "X":
            messagebox.showinfo("Tictactoe", "Congratulations, X wins!")
            exit(0)
        elif checkwin == "null":
            messagebox.showinfo("Tictactoe", "Tie!")

    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count+=1
        currentplayer = "Human"
        if checkwin() == "O":
            messagebox.showinfo("Tictactoe", "Congratulations, O wins!")
            exit(0)
        elif checkwin == "null":
            messagebox.showinfo("Tictactoe", "Tie!")
    if count == 9:
        messagebox.showinfo("Tictactoe", "Tie!")

#global coord



#build buttons
b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

#grid our buttons on screen
b1.grid(row = 0, column = 0)
b2.grid(row = 0, column = 1)
b3.grid(row = 0, column = 2)

b4.grid(row = 1, column = 0)
b5.grid(row = 1, column = 1)
b6.grid(row = 1, column = 2)

b7.grid(row = 2, column = 0)
b8.grid(row = 2, column = 1)
b9.grid(row = 2, column = 2)




root.mainloop()


