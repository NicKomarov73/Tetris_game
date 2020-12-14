import random


class Figure():
    fig = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
    ]

    colors = [
        '#1F2AFF',
        '#21FF2F',
        '#1EFCFF',
        '#A551FF',
        '#FFFC3F',
        '#FF7B26',
        '#FF4758'
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.fig) - 1)
        self.rotation = 0
        self.color = self.colors[random.randint(0, len(self.colors) - 1)]

    def image(self):
        return self.fig[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.fig[self.type])
