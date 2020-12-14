import pygame as pg
import Tetris

# creating colors
black = (0, 0, 0)
gray = (40, 40, 40)

# creating game window
game = Tetris.Tetris(20, 10, 45)
SIZE = (game.width * game.tile, game.height * game.tile)
FPS = 60

pg.init()
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Tetris")
clock = pg.time.Clock()

speed_counter, speed, speed_limit, super_speed_counter = 0, 500, 2000, 0

run = True
while run:
    if game.figure == None:
        game.new_figure()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                game.go_side(-1)
            if event.key == pg.K_RIGHT:
                game.go_side(1)
            if event.key == pg.K_UP:
                game.rotate()
            if event.key == pg.K_DOWN:
                speed_limit = 100

    screen.fill(black)

    # draw field
    grid = [pg.Rect(x * game.tile, y * game.tile, game.tile, game.tile) for x in range(game.width) for y in range(game.height)]
    [pg.draw.rect(screen, gray, i, 1) for i in grid]

    # draw figure
    fig = game.figure
    fig_im = fig.image()
    fig_rec = pg.Rect(0, 0, game.tile, game.tile)
    for i in range(4):
        fig_rec.x = (fig.x + fig_im[i] % 4) * game.tile
        fig_rec.y = (fig.y + fig_im[i] // 4) * game.tile
        pg.draw.rect(screen, fig.color, fig_rec)
        pg.draw.rect(screen, black, fig_rec, 1)

    # move down
    speed_counter += speed
    if speed_limit == 100:
        super_speed_counter += 1
    if speed_counter > speed_limit:
        speed_counter = 0
        if super_speed_counter > 6:
            speed_limit = 2000
            super_speed_counter = 0
        game.move_down()

        for i in range(4):
            if fig.y + fig_im[i] // 4 > game.height - 2 or game.field[fig.y + fig_im[i] // 4 + 1][fig.x + fig_im[i] % 4] != 0:
                for j in range(4):
                    game.field[fig.y + fig_im[j] // 4][fig.x + fig_im[j] % 4] = fig.color
                game.new_figure()

    for y, raw in enumerate(game.field):
        for x, col in enumerate(raw):
            if col != 0:
                fig_rec.x = x * game.tile
                fig_rec.y = y * game.tile
                pg.draw.rect(screen, col, fig_rec)
                pg.draw.rect(screen, black, fig_rec, 1)

    pg.display.flip()
    clock.tick(FPS)

pg.quit()
