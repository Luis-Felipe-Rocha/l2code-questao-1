class Robot():
    """Class that defines a robotic vacuum cleaner.

    With the width and length of the environment defined, the robot will follow the path defined in
    the instructions.

    Methods:
        position(): A string indicating which direction the robot is pointing and its coordinates.
    """

    def __init__(self, width: int, lenght: int, instructions: str) -> None:
        """Inits Robot.

        Inits Robot with the width and lenght limitations, the instructions to be followed,
        pointing North and on the Cartesian plane origin (0, 0).

        """

        self._width = width
        self._lenght = lenght

        if lenght < 0 or width < 0:
            raise ValueError("Can't create dimensions with negative numbers!")

        self._instructions = instructions
        self._x_axis: int = 0
        self._y_axis: int = 0
        self._direction: str = 'N'

        self._action()

    def position(self) -> str:
        """Returns robot position.

        Retrieves which direction the robot is facing (North(N), West(O), South(S) or East(L)) and
        its Cartesian plane coordinates.

        Args:

        Returns:
            A string indicating the robot direction and its coordinates For example:

            f'N 16 18'

        """
        return f'{self._direction} {self._x_axis} {self._y_axis}'

    def _move(self, command: chr) -> None:

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

    def _turn(self, command: chr) -> None:
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

    def _action(self) -> None:
        for command in self._instructions:
            if command in ('F', 'T'):
                self._move(command)
            elif command in ('D', 'E'):
                self._turn(command)
