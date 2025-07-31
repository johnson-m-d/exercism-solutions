def square(number):
    total = 1
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    if number == 1:
        return number
    for index in range(2,number+1):
        total *= 2
    return total

def total():
    return (2 ** 64) - 1
