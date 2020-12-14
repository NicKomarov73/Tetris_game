import Figure


class Tetris():
    figure = None

    def __init__(self, height, width, tile):
        self.height = height
        self.width = width
        self.tile = tile

    def new_figure(self):
        self.figure = Figure.Figure(3, 0)

    def intersect(self):
        intersection = False
        fig_im = self.figure.image()
        for i in range(4):
            if self.figure.x + fig_im[i] % 4 < 0 or self.figure.x + fig_im[i] % 4 > self.width - 1:
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
