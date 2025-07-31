def is_triangle(sides):
    if 0 in sides or (sides[0] + sides[1] < sides[2]) or (sides[1] + sides[2] < sides[0]) or (sides[0] + sides[2] < sides[1]):
        return False
    else:
        return True


def equilateral(sides):
    if is_triangle(sides):
        return sides[0] == sides[1] == sides [2]
    else:
        return False


def isosceles(sides):
    if is_triangle(sides):
        return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]
    else:
        return False


def scalene(sides):
    if is_triangle(sides):
        return sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]
    else:
        return False
