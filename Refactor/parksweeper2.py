#Parker Lowney 5/14/22
#Here we go again

from asyncio.windows_events import NULL
import time
import pygame as pg
import os
import random
import json

#Import saved settings
settings = json.load(open("Refactor\\settings.json"))["settings"]

#Game settings
TILE_SIZE = 40 #Size of each tile (always square) 
COLUMNS = 12
ROWS = 12

#Window setup
pg.init()
screen_size = (COLUMNS * TILE_SIZE, (ROWS + 1) * TILE_SIZE) #WxH
screen = pg.display.set_mode(screen_size)
pg.display.set_caption("Parksweeper")

#Quick shortcuts
update = lambda : pg.display.flip() #Update screen
gen_text = lambda size: pg.font.Font('freesansbold.ttf', size)

#Constants
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
DEFAULT_MINE_COUNT = 20 #The mine count to return to after each game (MUST BE AT LEAST 1/16th OF THE TOTAL TILE COUNT; SHOULD BE ABOUT 1/5th)
COLOR_DICT = {-1: RED, 0: WHITE, 1: GREEN, 2: GREEN, 3: GREEN, 4: GREEN, 5: GREEN, 6: GREEN, 7: GREEN, 8: GREEN}

#Game variables
hidden = []
shown = []
mines = 0

#Functions
def draw_grid(screen, size):
    '''Draws the grid on the screen'''
    width = size[0]
    height = size[1]
    for i in range(0, width, TILE_SIZE): #Draws vertical lines
        pg.draw.line(screen, (0, 0, 0), (i, TILE_SIZE), (i, height))
    for i in range(0, height, TILE_SIZE): #Draws horizontal lines
        pg.draw.line(screen, (0, 0, 0), (0, i), (width, i))


def quick_open(row, col):
    '''Opens all surrounding tiles of a fulfilled tile'''
    global hidden

    num = hidden[row][col]

    #Check that the tile's mine count is fulfilled
    for n in range(-1, 2):
        for i in range(-1, 2):
            if (len(hidden) > row + n > -1 and len(hidden[row + n]) > col + i > -1): #Check that the tile is in bounds
                if shown[row + n][col + i] == -1: #If the tile is flagged
                    num -= 1

    if num == 0: #If the mine count is fulfilled, open all surrounding tiles
        for n in range(-1, 2):
            for i in range(-1, 2):
                if (len(hidden) > row + n > -1 and len(hidden[row + n]) > col + i > -1): #Check that the tile is in bounds
                    if hidden[row + n][col + i] != -1 and shown[row + n][col + i] == 9: #If the tile isn't a mine and not flagged
                        update_tile(col + i, row + n, 1)


def open_field(x, y):
    '''Opens a field of zeros'''
    for r in range(-1, 2):
        for c in range(-1, 2):
            if (len(hidden) > r + y > -1 and len(hidden[y]) > c + x > -1): #Loops through each surrounding tile and makes sure it's valid
                if (shown[y + r][x + c] == 9):
                    #Open it
                    open_tile(x + c, y + r)

                    if (hidden[y + r][x + c] == 0): #If also 0, call this function
                        open_field(x + c, y + r)


def open_tile(x, y):
    '''Opens a given tile (seperated from update_tile for use elsewhere'''
    num = str(hidden[y][x])
    shown[y][x] = num
    text = gen_text(TILE_SIZE).render(num, False, COLOR_DICT[int(num)])

    pg.draw.rect(screen, WHITE, (x * TILE_SIZE + 1, (y + 1) * TILE_SIZE + 1, TILE_SIZE -1, TILE_SIZE -1)) #The pluses and minuses are to keep the grid lines

    #X is plus 1/4 tile size because the num is half the tile width, while y is 1/8 because the num is 6/8 the tile height
    screen.blit(text, (x * TILE_SIZE + (TILE_SIZE // 4), (y + 1) * TILE_SIZE + (TILE_SIZE // 8))) #Draw text at center of tile
    


def on_click(x, y, button):
    '''Handles logic for when a game tile is clicked'''

    if y < TILE_SIZE: #Clicked nav bar
        if (x > (screen_size[0] // 2) - (TILE_SIZE // 2)) and (x < (screen_size[0] // 2) + (TILE_SIZE // 2)): #Clicked reset button
            setup()

        elif (x < TILE_SIZE): #Clicked settings button
            print("run")
            settings_menu()
            time.sleep(2)
            redraw_board()
            print("redraw")

    else: #Clicked game tile
        y -= TILE_SIZE #Offset for nav bar
        update_tile(x // TILE_SIZE, y // TILE_SIZE, button)


def update_tile(x, y, button):
    '''Updates given tile with value'''
    global mines

    if button == 1 and (shown[y][x] != -1): #Left click and not flagged
        if (shown[y][x] == 9): #Unopened
            if hidden[y][x] == -1: #If a mine, lose
                pg.draw.rect(screen, RED, (x * TILE_SIZE + 1, (y + 1) * TILE_SIZE + 1, TILE_SIZE - 1, TILE_SIZE - 1))
                shown[y][x] = -1
                mines -= 1


            else: #If not a mine
                open_tile(x, y)

        else: #Opened
            quick_open(y, x)

        if hidden[y][x] == 0: #If no mines around, recursively call update_tile on surrounding tiles
            open_field(x, y)

    elif button == 3: #Right click
        if shown[y][x] == -1: #If already flagged
            pg.draw.rect(screen, GRAY, (x * TILE_SIZE + 1, (y + 1) * TILE_SIZE + 1, TILE_SIZE - 1, TILE_SIZE - 1))
            shown[y][x] = 9
            mines += 1

        elif shown[y][x] == 9: #If an unopened square
            pg.draw.rect(screen, RED, (x * TILE_SIZE + 1, (y + 1) * TILE_SIZE + 1, TILE_SIZE - 1, TILE_SIZE - 1))
            shown[y][x] = -1
            mines -= 1


def draw_mine_count():
    '''Draws the mine count on the nav bar'''
    text = gen_text(int(TILE_SIZE * 0.9)).render(str(mines), False, WHITE)
    rect = pg.draw.rect(screen, GRAY, (screen_size[0] - TILE_SIZE + 1, 1, TILE_SIZE - 1, TILE_SIZE - 1))
    rect.center = (screen_size[0] - TILE_SIZE // 2, TILE_SIZE // 2)
    screen.blit(text, rect)

def redraw_board():
    '''Redraws the board'''
    for y in range(len(shown)):
        for x in range(len(shown[y])):
            if shown[y][x] != 9:
                if shown[y][x] == -1:
                    pg.draw.rect(screen, RED, (x * TILE_SIZE + 1, (y + 1) * TILE_SIZE + 1, TILE_SIZE - 1, TILE_SIZE - 1))
                else:
                    open_tile(x, y)
            else:
                pg.draw.rect(screen, GRAY, (x * TILE_SIZE + 1, (y + 1) * TILE_SIZE + 1, TILE_SIZE - 1, TILE_SIZE - 1))
    draw_grid(screen, screen_size)
    update()


def fill_boards():
    '''Fills the hidden and shown boards'''
    rows = ROWS
    columns = COLUMNS

    for i in range(rows):
        hidden.append([])
        shown.append([])
        for j in range(columns):
            hidden[i].append(0)
            shown[i].append(9)


def set_mines():
    '''Fills the hidden board with randomly generated mine pattern'''
    placed = 0
    rows = ROWS
    columns = COLUMNS

    fill_boards()

    while(placed < mines): #Picks random square
        row = random.randint(0, rows - 1)
        col = random.randint(0, columns - 1)

        if hidden[row][col] != -1: #Not a mine
            placed += 1

            hidden[row][col] = -1 #Set as a mine

            #Loop to add one to each bordering square
            for r in range(-1, 2):
                for c in range(-1, 2):
                    #Makes sure a given value is within hidden
                    if (len(hidden) > r + row > -1 and len(hidden[row]) > c + col > -1):
                        if (hidden[row + r][col + c] != -1): #Not a mine
                            hidden[row + r][col + c] += 1

    #Print board for testing
    for i in range(rows):
        print(hidden[i])

def settings_menu():
    '''Displays the settings menu'''
    width = screen_size[0]
    height = screen_size[1]
    pg.draw.rect(screen, YELLOW, ((width // 2) - TILE_SIZE * 2, (width // 2) - TILE_SIZE * 2, TILE_SIZE * 4, TILE_SIZE * 4))
    update()
    

def setup():
    '''Sets up the game'''
    width = screen_size[0]
    screen.fill(GRAY)

    #Nav bar
    pg.draw.rect(screen, YELLOW, ((width // 2) - (TILE_SIZE // 2), 0, TILE_SIZE, TILE_SIZE))
    pg.draw.rect(screen, GREEN, (0, 0, TILE_SIZE, TILE_SIZE))

    #Reset vars
    global hidden; hidden = []
    global shown; shown = []
    global mines; mines = DEFAULT_MINE_COUNT

    set_mines()
    draw_mine_count()
    draw_grid(screen, screen_size)
    update()


#Main loop
if __name__ == "__main__":
    setup()
    while True:

        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()
                quit()

            if event.type == pg.MOUSEBUTTONDOWN:
            
                pos = pg.mouse.get_pos()
                x = pos[0] #Gets the square that was clicked
                y = pos[1]

                on_click(x, y, event.button)
                draw_mine_count()
                update()