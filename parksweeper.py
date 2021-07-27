#Created by Parker Lowney 6/21/21

import random as random
from random import randint
from tkinter import *

hiddenBoard = []

shownBoard = []


root = Tk()
root.geometry("500x500")
root.configure(background = "gray")


#txt = Label(root, text = "Parsweeper")
#txt.grid(row = 0, column = 0)

buttons = []
rows = 10
columns = 10
MINE_SIZE = 3
MINE_ODDS = 4


#Opens fields of empty squares
def openField(i, n):
    global hiddenBoard
    global buttons

    #Loop to open each bordering square
    for row in range(-1, 2):
        for col in range(-1, 2):
            #Makes sure a given value is within hiddenBoard
            if (len(hiddenBoard) > i + row > -1 and len(hiddenBoard[row]) > n + col > -1):
                if (buttons[row + i][col + n]["background"] == "gray"): #If square is unopened
                    buttons[row + i][col + n].config(background = "white")
                    if (hiddenBoard[row + i][col + n] == 0): #If opened square is also empty, calls method on itself
                        openField((row + i), (col + n))
                    else:
                        buttons[row + i][col + n].config(text = hiddenBoard[row + i][col + n])


#Flags mines upon right click
def flag(event):
    global buttons
    global hiddenBoard

    if (event.widget["text"] == "" and event.widget["background"] == "gray"):
        event.widget.config(text = "", background = "red")

    elif (event.widget["text"] == "#"):
        event.widget.config(text = "")



#Checks buttons when clicked
def check(square):
    global buttons
    global hiddenBoard

    row = square[0]
    col = square[1]

    if (hiddenBoard[row][col] == -1): #Is mine
        buttons[row][col].config(background = "yellow", text = "")

    elif (hiddenBoard[row][col] == 0): #Is empty
        buttons[row][col].config(background = "white", text = "")
        openField(row, col)

    else:
        buttons[row][col].config(background = "white", text = hiddenBoard[row][col])


#Sets buttons
def setButtons():
    for i in range(rows):
        buttons.append([])
        for n in range(columns):
            buttons[i].append(Button(root, width = MINE_SIZE, height = MINE_SIZE - 2, background = "gray", command = lambda r = (i,n): check(r)))
            buttons[i][n].grid(row = i + 1, column = n)
            buttons[i][n].bind("<Button-3>", flag)



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
    global MINE_ODDS

    setBoards(rows)

    #Sets the mines based on the mine odds
    for i in range(len(hiddenBoard)):

        for n in range(len(hiddenBoard[i])):

            if (random.randint(1, MINE_ODDS) == 3):
                hiddenBoard[i][n] = -1

                #Loop to add one to each bordering square
                for row in range(-1, 2):
                    for col in range(-1, 2):
                        #Makes sure a given value is within hiddenBoard
                        if (len(hiddenBoard) > i + row > -1 and len(hiddenBoard[row]) > n + col > -1):
                            if (hiddenBoard[row + i][col + n] != -1): #Not a mine
                                hiddenBoard[row + i][col + n] += 1


setMines()
setButtons()
root.mainloop()