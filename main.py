import pygame as pg
import Tetris

# creating colors
black = (0, 0, 0)
green = (0, 255, 0)
gray = (40, 40, 40)


# creating game window
game = Tetris.Tetris(20, 10, 45)
SIZE = (game.width*game.tile, game.height*game.tile)
FPS = 60

pg.init()
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Tetris")
clock = pg.time.Clock()


run = True
while run:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    screen.fill(black)

    grid = [pg.Rect(x*game.tile, y*game.tile, game.tile, game.tile) for x in range(game.width) for y in range(game.height)]

    [pg.draw.rect(screen, gray, i, 1) for i in grid]

    pg.display.flip()


pg.quit()