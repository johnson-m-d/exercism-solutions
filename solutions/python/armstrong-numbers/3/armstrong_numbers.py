def is_armstrong_number(number: int) -> bool:
    """ This function tests whether a given number is an armstrong number
    You can find more information on the subject here: https://en.wikipedia.org/wiki/Narcissistic_number
    params: number (int)
    returns: bool
    """
    return number == sum(int(character) ** len(str(number)) for character in str(number))
