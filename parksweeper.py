#Created by Parker Lowney 6/21/21

import random as random
from random import randint
from tkinter import *

hiddenBoard = []

shownBoard = []


root = Tk()
root.geometry("500x500")


txt = Label(root, text = "Parsweeper")
txt.grid(row = 0, column = 0)

buttons = []
rows = 10
columns = 10

for i in range(rows):
    buttons.append([])
    for n in range(columns):
        buttons[i].append(Button(root, padx = 10, pady = 10, text = "#", background = "gray", command = lambda r = (i,n): check(r)))
        buttons[i][n].grid(row = i + 1, column = n)



#Sets the board up
def setBoards(size):
    global shownBoard
    global hiddenBoard

    for row in range(size):

        shownBoard.append([0]), hiddenBoard.append([0])
        for col in range(size - 1):
            shownBoard[row].append(0)
            hiddenBoard[row].append(0)

#Sets the mines and numbers in the hidden board
def setMines(): 
    global rows
    global hiddenBoard
    global buttons

    setBoards(rows)

    for i in range(len(hiddenBoard)):

        for n in range(len(hiddenBoard[i])):

            if (random.randint(1, 4) == 3):
                hiddenBoard[i][n] = 1

#Checks buttons when clicked
def check(square):
    global buttons
    global hiddenBoard

    row = square[0]
    col = square[1]

    if (hiddenBoard[row][col] == 1): #Is mine
        buttons[row][col].config(foreground = "red", text = "$")

    elif (hiddenBoard[row][col] == 0): #Is empty
        buttons[row][col].config(background = "white", text = "")



setMines()
root.mainloop()