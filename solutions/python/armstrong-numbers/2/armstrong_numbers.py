def is_armstrong_number(number):
    return number == sum(int(character) ** len(str(number)) for character in str(number))
