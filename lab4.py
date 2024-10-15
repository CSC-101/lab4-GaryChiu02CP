import math

import data
from data import Point


# Write your functions for each part in the space below.

# Part 1
def first_element(x:list[list[int]]) -> list:
    newlist = []
    for i in x:
        newlist.append(i[0])
    return newlist

# Part 2
def x_coordinates(x:list[Point]):
    xlist = [i.x for i in x]
    return xlist

# Part 3
def are_in_positive_quadrant(x:list[Point]) -> list[Point]:
    xlist = [i for i in x if i.x > 0 and i.y > 0]
    return xlist

# Part 4
def distance(x1:Point, x2:Point) -> float:
    a = x2.x - x1.x
    b = x2.y - x1.y
    c = math.sqrt(a**2+b**2)
    return c

# Part 5
def manhattan_distance(x1:Point, x2:Point) -> float:
    a = x2.x - x1.x
    b = x2.y - x1.y
    total = math.fabs(a)+math.fabs(b)
    return total

# Part 6
def distance_all(x:list[Point]) -> list[float]:
    alldist = [math.sqrt((i.x**2)+(i.y)**2) for i in x]
    return alldist