from robot.robot import Robot


def main():
    width, lenght = map(int, input().split())
    instructions = input()

    robot = Robot(width, lenght, instructions)


if __name__ == '__main__':
    main()
