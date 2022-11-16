import pytest
from robot.robot import Robot


class TestRobot:
    """
    Class that defines the test cases.
    """

    def test_case_1(self):
        """
        Test case 1.
        """

        width, lenght = 10, 10
        instructions = 'FFFFFFFFFDFFFFFFFFFDFFFFFFFFFDFFFFFFFFF'

        robot = Robot(width, lenght, instructions)
        assert robot.position() == 'O 0 0'

    def test_case_2(self):
        """
        Test case 2.
        """

        width, lenght = 5, 5
        instructions = 'FDFEFDFEFDFEFDF'

        robot = Robot(width, lenght, instructions)
        assert robot.position() == 'L 4 4'

    def test_case_3(self):
        """
        Test case 3.
        """

        width, lenght = 1232, 1232
        instructions = 'TTTTTTTTTTTTT'

        robot = Robot(width, lenght, instructions)
        assert robot.position() == 'N 0 0'

    def test_case_4(self):
        """
        Test case 4.
        """

        width, lenght = 15, 36
        instructions = 'FFFFFFFFFFFFFFFFDFETTTTTTTTTTTTTTTT'

        robot = Robot(width, lenght, instructions)
        assert robot.position() == 'N 1 0'

    def test_case_5(self):
        """
        Test case 5.
        """

        width, lenght = 50, 50
        instructions = '''
                        TTFFDTTETDEDTTDDFFDEFDTEFTTDDEDEFFTEETEDTTEEDDEFFFTEDFDFTTDDDTTTTTFDEFDFFTE
                        DTEDEFTDTETETFDFTDTFEFDTFTTEEFEEFEDDTFTEDFFTTDTTTFDETETDDTEDDTFEDFDEFDDTTDE
                        FEFTDTTDFFEDDTDFDETTDDFFTEEDFFTTTDETFTFDTETTTTDEFFETFTDFDTEEDFTEFTEFFFTDEED
                        DTTEFDFETDFEEETTDFTTTEEEEEDTETFETTETDEEFTTDDDFFTFDDEFDEFTTTEDFFFTEEDTDDTTDF
                        DEETTDETETDDETTTDEFEETTETDEDTEFTTDDEEFDFDTEEEDEDTDDTEEEEEDTFEDEDDDTTTFFDETF
                        FDDTFDTEFFFDDFEEFEFDDFDTTETTDTDTTTDEDFTTDDDTTTTTDTEDFEFDTFFETEEEFFFEFDTTDET
                        TFFETTDEETFEDTEFFDEEFEEDTTFFTEEETDTEEEFTFFEFEFDFFEFTFEDEEDFDDDFDFEFEDDDTEET
                        TETFTTFDTDEFTFEEDEFTEFETFEEEFDETEDFFTFDFFTFDTFEFDEDTTTFEDEFTTDDEEFDTFTEEDTE
                        TEFEFFEEEFFTFEETEDDFFFTFDETFDEFETDTFDDFFTFDTFTTFTTFDFDDEDEFFFETTTTFFFFTDEEE
                        FTDFDDFTFETDDEDFFFEFFDDDTTDEFETFDEFDEDETDFEETEDTFETTTFEEEFTETFFTDFDFEDFTDDT
                        EFTFFEFEEFTTTFEEFTDDDEEDTFTFDTTDFDEETFFTDFDEDEEFFDTFETEDEETTEFFFDETTTFTEETF
                        DTEFFEEFFDEDFFDTTEFDETDDETDDDTDFETTTETEEEFDFTEETDTEDETTEDETFEEEFTFFEEDTFFFT
                        EDDFDDFDDTTEDEETETEEFDDDTTTTTEEFEFFFTEFEDEFEFEFEDDFFEEEFEETTFDFEEDDTTTTETDT
                        EDEFFDFTTFFTDTEDEDEDDFEFT
                        '''

        robot = Robot(width, lenght, instructions)
        assert robot.position() == 'S 11 13'

    def test_case_6(self):
        """
        Test case 6.
        """

        width, lenght = 1000, 1000
        instructions = '''
                        EDFFEDFTTEDFTETEFDTFDTDTDTFDFTDEDTFFTFTDDDETFTFEFETEFEEEDFTTEFEEDFTFFTFTDTT
                        DFDDDTFTTTDDEETDDFTDFFETTDTTTFEEFFTDTFETDEFEDEFDFDTTEFDEEDTTDDETTDEDTTEEEFF
                        EEDDDETDFDTEDEDFTFFEEDEDDFEDEDFDDFEDEETTFTETFTTTEETTFDDTTEFDDEDTDEDEDDFTFEF
                        TDFEFFDTETFFFTDTFTEFFFEDETFETTFETDFFFDEETETFEFFTFETFEFFTEETDETDEFEFTFDEEFDE
                        EDTEDEFEFTEETTTTFEEFTDTDDFDEDFEDDDDTEDDDTFDDDEEEEDTTDFEDTDETFTFTFDFTFTDFEDE
                        FDEEEDDETEEEDDTEFEFFFDTEFTFFEETETEDDDDEFTEEDDEDDTTDTTEDFEFETFTDTFTFEEDEFEDT
                        EFDEEDEDEFDTEDEETEDEDEDDEDTDTDDFFEFDEETTEDDEFFTFDEFEFFDFDDTFEFTTDDDTDTDDFDE
                        EDETDDDFEFTEDEFEEFDETEFTDFTFDDFTFEEDEEEEEDDDTEDDFTDFDFFFDTETTTDETTEDETEDDET
                        ETDEEFTTFTDDFDEEEFFDEDTEDFTEETTEFDDFTFEFEEEETFTEFTEDFTFFEEEDFDETTEFDTFFDDDF
                        FDTEEFETDTETFDFTDEDTFFFFEETTFDFDDFTDTTDFFTFDDDTDTDDFDDEETETTFETTEFDTTFEDDFD
                        TEDETTTEDTDEFFEFFFTDTEDTTTEFFTTTTDFTDFTETDDFDEEFEFTEFTTDDDTEFEFETDDDDTETTTE
                        TEEDEETTDDFTDTETTFTFFTEFFEEDEEEFTTDEEEEFEDTEEEDEEDDDTETEFEFDDDEDEFEFTTDFDTT
                        DEDFTFDDTDTFDDDDEFEEEDEDDTTTDDTEDTEDDTDTDDTFETDTDTDFDDDTTEEEFEDTEFFDEEDTTEF
                        TDEDTDDETEFEFEFFTTTEEFDEF
                        '''

        robot = Robot(width, lenght, instructions)
        assert robot.position() == 'L 25 5'

    def test_case_width_with_negative_values_must_fail(self):
        with pytest.raises(ValueError):
            width, lenght = -10, 10
            instructions = 'FFF'
            robot = Robot(instructions=instructions,
                          width=width, lenght=lenght)
            assert robot.position()
