def is_triangle(sides):
    return all(sides) and (2 * max(sides) < sum(sides))


def equilateral(sides):
    return is_triangle(sides) and sides[0] == sides[1] == sides [2]


def isosceles(sides):
    return is_triangle(sides) and (sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2])


def scalene(sides):
    return is_triangle(sides) and (sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2])
