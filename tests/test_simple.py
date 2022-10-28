# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from sample.simple import add_one, subtract_one, inverse


class TestSimple(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(add_one(5), 6)

    def test_subtract_one(self):
        self.assertEqual(subtract_one(6), 5)

    def test_inverse(self):
        self.assertEqual(inverse(1), 1)

    def test_inverse_0(self):
        with self.assertRaises(ZeroDivisionError):
            inverse(0)
        inverse(2) == 0.5


if __name__ == '__main__':
    unittest.main()
