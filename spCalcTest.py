import unittest
from spCalculator import spcalc


class TestCalc(unittest.TestCase):
    def test_calc1(self):
        self.assertEqual(spcalc(10000, 12, 15), 11607.54)
        self.assertEqual(spcalc(100000, 24, 17), 140159.97)
        self.assertEqual(spcalc(250000.01, 60, 13.3), 484347.56)

    def test_calc2(self):
        self.assertRaises(TypeError, spcalc, 1214, "236", 12.2)
        self.assertRaises(TypeError, spcalc, 100000, 24.3, 17)
        self.assertRaises(TypeError, spcalc, 100000, 24.3, "three")

    def test_calc3(self):
        self.assertRaises(ValueError, spcalc, -250000, 6, 3)
        self.assertRaises(ValueError, spcalc, 250000, -6, 3)
        self.assertRaises(ValueError, spcalc, 250000, 6, -3)


if __name__ == '__main__':
    unittest.main()
