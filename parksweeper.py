#Created by Parker Lowney 6/21/21

import random as random
from random import randint
from tkinter import *

hiddenBoard = []

shownBoard = []


window = Tk()
window.geometry("500x500")


txt = Label(window, text='Hello World')
txt.pack()

#buttons = Button(window)

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
    pass


window.mainloop()