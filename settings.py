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

    set_screen = Button(set_root, width = 25, height = 2, background = "gray", text = "Set default screen size", command = setScreen)
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

    auto_mine = Button(set_root, width = 25, height = 2, background = "gray", text = "Auto set mines", command = autoMine)
    auto_mine.pack()

    done = Button(set_root, width = 40, height = 3, background = "gray", text = "DONE", command = updateValues)
    done.pack()

#Puts existing values into placed elements
def setValues():
    global height
    global width

    #Opens settings file and formats its info into settings
    f = open("parSets.txt", "r")
    height = f.readline().lower().replace("height=", "").strip()
    width = f.readline().lower().replace("width=", "").strip()
    set_rows.insert(0, f.readline().lower().replace("rows=", "").strip())
    set_cols.insert(0, f.readline().lower().replace("cols=", "").strip())
    set_mines.insert(0, f.readline().lower().replace("mines=", "").strip())

    f.close()



#Auto sets rows and cols based on window size
def autoRow():
    #Squares are 62 pixels tall and I guess 43 wide, and even then it varies by computer :(
    set_rows.delete(0, END)
    set_rows.insert(0, str(int(int(height) / 62)))

    set_cols.delete(0, END)
    set_cols.insert(0, str(int(int(width) / 43)))

#Automatically sets mine num based on board size
def autoMine():
    rows = int(set_rows.get())
    cols = int(set_cols.get())

    mines = int(rows * cols / 5) #Makes a 5th of the board mines

    set_mines.delete(0, END)
    set_mines.insert(0, str(mines))

#Updates values in settings file and then closes the program
def updateValues():
    f = open("parSets.txt", "w")

    #Was this the most effective way to do this? I'm not sure, but it works
    f.write("height=" + str(height) + "\n")
    f.write("width=" + str(width) + "\n")
    f.write("rows=" + set_rows.get() + "\n")
    f.write("cols=" + set_cols.get() + "\n")
    f.write("mines=" + set_mines.get())

    set_root.destroy() #Closes setting window

#Sets screen height and width
def setScreen():
    global height
    global width
    
    height = set_root.winfo_height()
    width = set_root.winfo_width()

    #print(height, width)

#Opens the settings window
def run():
    global set_root

    setWindow()
    placeElements()
    setValues()
    set_root.mainloop()

run()

