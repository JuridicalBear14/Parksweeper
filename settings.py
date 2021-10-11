from tkinter import *

set_root = None

def setWindow():
    global set_root

    set_root = Tk()
    set_root.geometry("300x300")
    set_root.configure(background = "dim gray")
    set_root.title("Settings")


#PLaces elements on screen
def placeElements():
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

    auto_size = Button(set_root, width = 25, height = 2, background = "gray", text = "Auto set board size")
    auto_size.pack()

    mine_label = Label(set_root, width = 40, height = 1, background = "Red", text = "Mines")
    mine_label.pack()

    set_mines = Entry(set_root, width = 25)
    set_mines.pack()

    auto_mine = Button(set_root, width = 25, height = 2, background = "gray", text = "Auto set mines")
    auto_mine.pack()

#Puts existing values into placed elements
def setValues():
    pass

#Auto sets rows and cols based on window size
def autoRow():
    pass

#Automatically sets mine num based on board size
def autoMine():
    pass

#Updates values in settings file
def updateValues():
    pass

#Opens the settings window
def run():
    global set_root

    setWindow()
    placeElements()
    set_root.mainloop()

run()

