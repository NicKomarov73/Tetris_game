import Figure


class Tetris():
    figure = None

    def __init__(self, height, width, tile):
        self.height = height
        self.width = width
        self.tile = tile
        self.field = [[0 for i in range(self.width+1)] for j in range(self.height+1)]

    def new_figure(self):
        self.figure = Figure.Figure(3, -1)

    def intersect(self):
        intersection = False
        fig_im = self.figure.image()
        for i in range(4):
            pos_x = self.figure.x + fig_im[i] % 4
            if pos_x < 0 or pos_x > self.width - 1:
                intersection = True

        return intersection

    def go_side(self, dx):
        temp = self.figure.x
        self.figure.x += dx
        if self.intersect():
            self.figure.x = temp

    def move_down(self):
        temp = self.figure.y
        self.figure.y += 1
        if self.intersect():
            self.figure.y = temp

    def rotate(self):
        temp = self.figure.rotation
        self.figure.rotate()
        if self.intersect():
            self.figure.rotation = temp
