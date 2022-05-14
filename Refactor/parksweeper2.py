#Parker lowney 5/14/22
#Here we go again

import pygame as pg
import os
import random

screen = pg.display.set_mode((800, 600))

pg.display.set_caption("Parksweeper")

while True:
    
    for event in pg.event.get():

        if event.type == pg.QUIT:
            pg.quit()
            quit()