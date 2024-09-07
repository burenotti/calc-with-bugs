import unittest

from calc.app import CalcController, Operator


class TestControllerInputDigits(unittest.TestCase):

    def setUp(self):
        self.ctl = CalcController()

    def test_can_add_digits(self) -> None:
        digits = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 0]

        for digit in digits:
            self.ctl.add_digit(digit)

        expected = int(''.join(map(str, digits)))
        self.assertEqual(expected, self.ctl.argument)


class TestControllerOperations(unittest.TestCase):

    def test_can_simple_operations(self) -> None:
        cases = [
            (125, '+', 5, 130),
            (-18, '*', 2, -36),
            (10, '/', 1, 10),
            (100, '/', 10, 10),
            (50, '-', 40, 10),
        ]

        for case in cases:
            accum, op, argument, expected = case
            ctl = CalcController()
            ctl.argument = accum
            ctl.add_operator(Operator(op))
            ctl.argument = argument
            ctl.execute()
            actual = ctl.argument
            self.assertEqual(expected, actual)

    def test_multiple_operations(self) -> None:
        ctl = CalcController()
        ctl.argument = 10
        ctl.add_operator(Operator.PLUS)
        ctl.argument = 20
        ctl.add_operator(Operator.TIMES)
        ctl.argument = 3
        ctl.execute()
        self.assertEqual(ctl.argument, 60)