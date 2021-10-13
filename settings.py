#Parker Lowney
from tkinter import *

#Makes screen elements global so I can be lazy
set_root = None
set_mines = None
set_rows = None
set_cols = None

height = None
width = None

def setWindow():
    global set_root

    set_root = Tk()
    set_root.geometry("300x300")
    set_root.configure(background = "dim gray")
    set_root.title("Settings")


#PLaces elements on screen
def placeElements():
    global set_rows
    global set_mines
    global set_cols

    window_label = Label(set_root, width = 40, height = 1, background = "green", text = "Window Size")
    window_label.pack()

    set_screen = Button(set_root, width = 25, height = 2, background = "gray", text = "Set default screen size")
    set_screen.pack()

    row_label = Label(set_root, width = 40, height = 1, background = "blue", text = "Rows and Columns")
    row_label.pack()

    set_rows = Entry(set_root, width = 25)
    set_rows.pack()

    set_cols = Entry(set_root, width = 25)
    set_cols.pack()

    auto_size = Button(set_root, width = 25, height = 2, background = "gray", text = "Auto set board size", command = autoRow)
    auto_size.pack()

    mine_label = Label(set_root, width = 40, height = 1, background = "Red", text = "Mines")
    mine_label.pack()

    set_mines = Entry(set_root, width = 25)
    set_mines.pack()

    auto_mine = Button(set_root, width = 25, height = 2, background = "gray", text = "Auto set mines")
    auto_mine.pack()

    done = Button(set_root, width = 40, height = 3, background = "gray", text = "DONE")
    done.pack()

#Puts existing values into placed elements
def setValues():
    global height
    global width

    f = open("parSets.txt", "r")
    height = f.readline().lower().replace("height=", "").strip()
    width = f.readline().lower().replace("width=", "").strip()
    set_rows.insert(0, f.readline().lower().replace("rows=", "").strip())
    set_cols.insert(0, f.readline().lower().replace("cols=", "").strip())
    set_mines.insert(0, f.readline().lower().replace("mines=", "").strip())



#Auto sets rows and cols based on window size
def autoRow():

    set_rows.delete(0, END)
    set_rows.insert(0, str(int(int(height) / 62)))

    set_cols.delete(0, END)
    set_cols.insert(0, str(int(int(width) / 43)))

#Automatically sets mine num based on board size
def autoMine():
    pass

#Updates values in settings file
def updateValues():
    pass

#Sets screen height and width
def setScreen():
    pass

#Opens the settings window
def run():
    global set_root

    setWindow()
    placeElements()
    setValues()
    set_root.mainloop()

run()

