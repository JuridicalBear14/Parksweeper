#Created by Parker Lowney 6/21/21

import random as random
from random import randint
from tkinter import *

hiddenBoard = []

shownBoard = []


root = Tk()
root.geometry("800x700")
root.configure(background = "gray")
root.title("Parksweeper")

#txt = Label(root, text = "Parsweeper")
#txt.grid(row = 0, column = 0)

buttons = []
rows = 20
columns = 20
MINE_SIZE = 3
MINE_ODDS = 4

#nav = LabelFrame(root, width = 38 * rows, height = 100, background = "dim gray")
#nav.grid(row = 0, columnspan = rows)

#reset = Button(nav, width = 10, height = 5, background = "gray")
#reset.pack()


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

    elif event.widget["background"] == "red":
        event.widget.config(background = "gray")

    elif (event.widget["text"] == "#"):
        event.widget.config(text = "")


#Method for quick opening fulfilled numbers
def quickOpen(row, col):
    global hiddenBoard
    global buttons

    num = hiddenBoard[row][col]

    for i in range(-1, 2):
        for n in range(-1, 2):
            if (len(hiddenBoard) > i + row > -1 and len(hiddenBoard[row]) > n + col > -1): #Makes sure square is in range
                if buttons[row + i][col + n]["background"] == "red": #If flagged
                    num -= 1

    if num == 0: #If the number was exactly fulfilled
        for i in range(-1, 2):
            for n in range(-1, 2):
                if (len(hiddenBoard) > i + row > -1 and len(hiddenBoard[row]) > n + col > -1): #Makes sure square is in range

                    if buttons[row + i][col + n]["text"] == "": #If isn't already opened

                        check((row + i, col + n))

                    '''
                    if not buttons[row + i][col + n]["background"] == "red": #If not flagged

                        buttons[row + i][col + n].config(background = "white") #Makes background white

                        if hiddenBoard[row + i][col + n] > 0: #Not empty
                            buttons[row + i][col + n].config(text = hiddenBoard[row + i][col + n])

                        else: #Is empty
                            openField(row + i, col + n)'''


#Checks buttons when clicked
def check(square):
    global buttons
    global hiddenBoard

    row = square[0]
    col = square[1]

    if not buttons[row][col]["background"] == "red":


        if (hiddenBoard[row][col] == -1): #Is mine
            buttons[row][col].config(background = "red", text = "")

        elif (hiddenBoard[row][col] == 0): #Is empty
            buttons[row][col].config(background = "white", text = "")
            openField(row, col)

        elif hiddenBoard[row][col] > 0 and buttons[row][col]["background"] == "white": #Is opened number
            quickOpen(row, col)

        else:
            buttons[row][col].config(background = "white", text = hiddenBoard[row][col])


#Sets buttons
def setButtons():
    for i in range(rows):
        buttons.append([])
        for n in range(columns):
            buttons[i].append(Button(root, width = MINE_SIZE, height = MINE_SIZE - 2, background = "gray", font = ("bold"), command = lambda r = (i,n): check(r)))
            buttons[i][n].grid(row = i + 1, column = n)
            buttons[i][n].bind("<Button-3>", flag)


#Sets the colors for all the number
def setColors():
    global hiddenBoard
    global buttons

    for i in range(len(hiddenBoard)):
        for n in range(len(hiddenBoard[i])):

            if hiddenBoard[i][n] == 1:
                buttons[i][n].config(foreground = "blue")

            if hiddenBoard[i][n] == 2:
                buttons[i][n].config(foreground = "green")

            if hiddenBoard[i][n] == 3:
                buttons[i][n].config(foreground = "red")

            if hiddenBoard[i][n] == 4:
                buttons[i][n].config(foreground = "purple")

            if hiddenBoard[i][n] == 5:
                buttons[i][n].config(foreground = "brown")

            if hiddenBoard[i][n] == 6:
                buttons[i][n].config(foreground = "orange")

            if hiddenBoard[i][n] == 7:
                buttons[i][n].config(foreground = "black")

            if hiddenBoard[i][n] == 8:
                buttons[i][n].config(foreground = "yellow")


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
setColors()
root.mainloop()