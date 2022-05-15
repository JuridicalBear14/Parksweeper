#Parker lowney 5/14/22
#Here we go again

import pygame as pg
import os
import random

#Window setup
pg.init()
screen_size = (800, 600) #WxH
screen = pg.display.set_mode(screen_size)
update = lambda : pg.display.flip() #Update screen
gen_text = lambda size: pg.font.Font('freesansbold.ttf', size)
pg.display.set_caption("Parksweeper")
screen.fill((240, 240, 240))

#Constants
RED = (255, 0, 0)
TILE_SIZE = 100 #Size of each tile (always square)

#Game variables

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
    text = gen_text(TILE_SIZE).render("7", False, RED)

    pg.draw.rect(screen, (0, 0, 0), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    #X is plus 1/4 tile size because the num is half the tile width, while y is 1/8 because the num is 6/8 the tile height
    screen.blit(text, (x * TILE_SIZE + (TILE_SIZE // 4), y * TILE_SIZE + (TILE_SIZE // 8))) #Draw text at center of tile
    

draw_grid(screen, screen_size)

update()

#Main loop
if __name__ == "__main__":
    while True:

        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()
                quit()

            if event.type == pg.MOUSEBUTTONDOWN:
            
                pos = pg.mouse.get_pos()
                x = pos[0] // TILE_SIZE #Gets the square that was clicked
                y = pos[1] // TILE_SIZE

                on_click(x, y, event.button)
                update()