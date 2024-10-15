import data
import lab4
import unittest

from data import Point


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)

    def test_first_element_2(self):
        input = [[5, 7], [51, 37]]
        result = lab4.first_element(input)
        expected = [5, 51]
        self.assertEqual(expected, result)

    # Part 2
    def test_x_coordinates_1(self):
        x1 = Point(3,2)
        x2 = Point(8,7)
        input = [x1, x2]
        result = lab4.x_coordinates(input)
        expected = [3, 8]
        self.assertEqual(expected, result)

    def test_x_coordinates_2(self):
        x1 = Point(7,4)
        x2 = Point(346,983)
        input = [x1, x2]
        result = lab4.x_coordinates(input)
        expected = [7, 346]
        self.assertEqual(expected, result)

    # Part 3
    def test_are_in_positive_quadrant_1(self):
        x1 = Point(3, 2)
        x2 = Point(-8, 7)
        x3 = Point(-5, -9)
        x4 = Point(46, -63)
        x5 = Point(465, 635)
        input = [x1, x2, x3, x4, x5]
        result = lab4.are_in_positive_quadrant(input)
        expected = [x1,x5]
        self.assertEqual(expected, result)

    def test_are_in_positive_quadrant_2(self):
        x1 = Point(6, 9)
        x2 = Point(-54, 34)
        x3 = Point(-75, -34)
        x4 = Point(363463, -7545)
        x5 = Point(45, 5)
        input = [x1, x2, x3, x4, x5]
        result = lab4.are_in_positive_quadrant(input)
        expected = [x1, x5]
        self.assertEqual(expected, result)

    # Part 4
    def test_distance_1(self):
        x1 = Point(1, 1)
        x2 = Point(7, 9)
        result = lab4.distance(x1, x2)
        expected = 10
        self.assertEqual(expected, result)

    def test_distance_2(self):
        x1 = Point(4, 3)
        x2 = Point(8, 6)
        result = lab4.distance(x1, x2)
        expected = 5
        self.assertEqual(expected, result)

    # Part 5
    def test_manhattan_distance_1(self):
        x1 = Point(0, 0)
        x2 = Point(3, 5)
        result = lab4.manhattan_distance(x1, x2)
        expected = 8
        self.assertEqual(expected, result)

    def test_manhattan_distance_2(self):
        x1 = Point(5, 7)
        x2 = Point(-9, -10)
        result = lab4.manhattan_distance(x1, x2)
        expected = 31
        self.assertEqual(expected, result)

    # Part 6
    def test_distance_all_1(self):
        x1 = Point(4, 3)
        x2 = Point(6, 8)
        input = [x1,x2]
        result = lab4.distance_all(input)
        expected = [5,10]
        self.assertEqual(expected, result)

    def test_distance_all_2(self):
        x1 = Point(-6, 8)
        x2 = Point(4, -3)
        input = [x1,x2]
        result = lab4.distance_all(input)
        expected = [10,5]
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()