def is_armstrong_number(number):
    armstrong_test = 0
    stringy_numbers = str(number)
    for character in stringy_numbers:
        armstrong_test += int(character) ** len(stringy_numbers)
    return number == armstrong_test
