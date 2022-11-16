class Robot:
    def __init__(self, width, lenght, instructions):
        self._width = width
        self._lenght = lenght
        self._instructions = instructions

        self._x_axis = 0
        self._y_axis = 0
        self._direction = 'N'

    def position(self):
        return f'{self._direction} {self._x_axis} {self._y_axis}'
