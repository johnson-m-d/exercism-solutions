def score(x, y):
    import math
    radius = math.sqrt((x - 0) ** 2 + (y - 0) ** 2)
    result = 0

    if radius <= 10:
        result = 1
    if radius <= 5:
        result = 5
    if radius <= 1:
        result = 10

    return result
