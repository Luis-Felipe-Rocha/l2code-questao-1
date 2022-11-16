class Robot:
    def __init__(self, width, lenght, instructions):
        self._width = width
        self._lenght = lenght
        self._instructions = instructions

        self._x_axis = 0
        self._y_axis = 0
        self._direction = 'N'

        self._action()

    def position(self):
        return f'{self._direction} {self._x_axis} {self._y_axis}'

    def _move(self, command):

        if command == 'F':
            if self._direction == 'N' and self._y_axis != self._width:
                self._y_axis += 1
            elif self._direction == 'O' and self._x_axis != 0:
                self._x_axis -= 1
            elif self._direction == 'S' and self._x_axis != 0:
                self._y_axis -= 1
            elif self._direction == 'L' and self._y_axis != self._lenght:
                self._x_axis += 1

        elif command == 'T':
            if self._direction == 'N' and self._y_axis != 0:
                self._y_axis -= 1
            elif self._direction == 'O' and self._x_axis != self._lenght:
                self._x_axis += 1
            elif self._direction == 'S' and self._y_axis != self._width:
                self._y_axis += 1
            elif self._direction == 'L' and self._x_axis != 0:
                self._x_axis -= 1

    def _turn(self, command):
        if command == 'D':
            if self._direction == 'N':
                self._direction = 'L'
            elif self._direction == 'O':
                self._direction = 'N'
            elif self._direction == 'S':
                self._direction = 'O'
            elif self._direction == 'L':
                self._direction = 'S'

        elif command == 'E':
            if self._direction == 'N':
                self._direction = 'O'
            elif self._direction == 'O':
                self._direction = 'S'
            elif self._direction == 'S':
                self._direction = 'L'
            elif self._direction == 'L':
                self._direction = 'N'

    def _action(self):
        for command in self._instructions:
            if command == 'F' or command == 'T':
                self._move(command)
            elif command == 'D' or command == 'E':
                self._turn(command)
