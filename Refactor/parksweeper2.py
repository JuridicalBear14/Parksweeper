#Parker lowney 5/14/22
#Here we go again

import pygame as pg
import os
import random

#Window setup
pg.init()
screen_size = (1000, 900) #WxH
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
TILE_SIZE = 100 #Size of each tile (always square)

#Game variables
hidden = []
shown = []
mines = 18

#Functions
def draw_grid(screen, size):
    '''Draws the grid on the screen'''
    width = size[0]
    height = size[1]
    for i in range(0, width, TILE_SIZE): #Draws vertical lines
        pg.draw.line(screen, (0, 0, 0), (i, TILE_SIZE), (i, height))
    for i in range(0, height, TILE_SIZE): #Draws horizontal lines
        pg.draw.line(screen, (0, 0, 0), (0, i), (width, i))


def on_click(x, y, button):
    '''Handles logic for when a game tile is clicked'''

    if y < TILE_SIZE: #Clicked nav bar
        if (x > (screen_size[0] // 2) - (TILE_SIZE // 2)) and (x < (screen_size[0] // 2) + (TILE_SIZE // 2)): #Clicked reset button
            setup()

    else: #Clicked game tile
        update_tile(x // 100, y // 100, button)


def update_tile(x, y, button):
    '''Updates given tile with value'''

    if button == 1: #Left click
        num = str(hidden[x][y])
        text = gen_text(TILE_SIZE).render(num, False, GREEN)

        pg.draw.rect(screen, WHITE, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

        #X is plus 1/4 tile size because the num is half the tile width, while y is 1/8 because the num is 6/8 the tile height
        screen.blit(text, (x * TILE_SIZE + (TILE_SIZE // 4), y * TILE_SIZE + (TILE_SIZE // 8))) #Draw text at center of tile

    elif button == 3: #Right click
        pg.draw.rect(screen, RED, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

def fill_boards():
    '''Fills the hidden and shown boards'''
    rows = screen_size[0] // TILE_SIZE
    columns = screen_size[1] // TILE_SIZE

    for i in range(rows):
        hidden.append([])
        shown.append([])
        for j in range(columns):
            hidden[i].append(0)
            shown[i].append(0)


def set_mines():
    '''Fills the hidden board with randomly generated mine pattern'''
    placed = 0
    rows = screen_size[0] // TILE_SIZE
    columns = screen_size[1] // TILE_SIZE

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
    
def setup():
    '''Sets up the game'''
    width = screen_size[0]
    screen.fill(GRAY)

    #Nav bar
    pg.draw.rect(screen, YELLOW, ((width // 2) - (TILE_SIZE // 2), 0, TILE_SIZE, TILE_SIZE))

    #Reset vars
    global hidden; hidden = []
    global shown; shown = []
    global mines; mines = 18

    set_mines()
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
                update()