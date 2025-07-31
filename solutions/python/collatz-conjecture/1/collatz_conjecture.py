def steps(number):
    steps = 0
    # when argument is zero or a negative integer
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    while number > 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        steps = steps + 1
    return steps