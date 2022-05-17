import pygame as pg

pg.init()

class TBox:
    '''A box to enter text'''

    def __init__(self, screen, pos = (0, 0), size = (30, 80)) -> None:
        self.rect = pg.Rect(pos, size)
        self.text = "" #The currently stored text
        self.pos = pos #The position of the text box
        self.size = size
        self.screen = screen
        self.__draw()

    def write(self, text) -> None:
        '''Writes text to the box'''
        self.text += text
        self.__draw()

    def clear(self) -> None:
        '''Clears all text'''
        self.text = ""
        self.write("")

    def resize(self):
        width = max(200, len(self.text) * 10)

    def __draw(self) -> None:
        '''Draws the box with text'''
        gen_text = lambda size: pg.font.Font('freesansbold.ttf', size)
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        x = self.pos[0]
        y = self.pos[1]

        text = gen_text(self.size[1] - 3).render(self.text, True, BLACK)

        pg.draw.rect(self.screen, WHITE, self.rect)
        self.screen.blit(text, (self.rect.x, self.rect.y))

    def backspace(self) -> None:
        self.text = self.text[:-1]
        self.__draw()

    def collidepoint(self, pos: tuple) -> bool:
        return self.rect.collidepoint(pos)
        

    def get_text(self) -> str:
        return self.text

    def set_pos(self, pos: tuple) -> None:
        self.pos = pos






def test():
    '''Function for testing the class'''
    screen_size = (800, 600)
    screen = pg.display.set_mode(screen_size)
    pg.display.set_caption("TBox")
    update = lambda : pg.display.flip() #Update screen
    #screen.fill((255, 255, 255))

    box = TBox(screen, size=(400, 50))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    print(box.get_text())
                    box.clear()

                elif event.key == pg.K_BACKSPACE:
                    box.backspace()

                else:
                    box.write(event.unicode)
        update()


if __name__ == "__main__":
    test()