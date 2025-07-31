""" Functions to translate English words into Pig Latin """

def is_vowel(letter: str) -> bool:
    """Determine whether a character is a vowel.
    
    :param letter: str - the letter to evaluate
    :return: bool - True if vowel, False if not
    """
    
    vowels = 'aeiou'
    if letter in vowels:
        return True
    return False

def is_consonant(letter: str) -> bool:
    """Determine whether a character is a consonant.
    
    :param letter: str - the letter to evaluate
    :return: bool - True if consonant, False if not
    """
    
    consonants = 'qwrtypsdfghjklzxcvbnm'
    if letter in consonants:
        return True
    return False

def rule1(text: str) -> str:
    """Append 'ay' to the end of text that begins with a vowel.
    
    :param text: str - A word that begins with a vowel
    :return str - The given word with 'ay' appended
    """
    
    return text + 'ay'

def rule2(text: str) -> str:
    """Move the consonants from the beginning of the text to the end and append 'ay' to the end.
    
    :param text: str - A word that begins with one or more consonants
    :return str - The given word with its beginning consonants and 'ay' on the end
    """
    
    index = 0
    suffix = ''
    for character in text:
        if not is_vowel(character):
            suffix += character
            index += 1
        else:
            return text[index:] + suffix + 'ay'

def rule3(text: str) -> str:
    """Move any consonants and 'qu' to the end of text and append 'ay'

    :param text: str - A word containing qu and any number of leading consonants
    :return str - The given word with its beginning consonants with 'qu' and 'ay' on the end
    """
    
    suffix = ''
    index = text.index('u') + 1
    for number in range(index):
        suffix += text[number]
    return text[index:] + suffix + 'ay'

def rule4(text: str) -> str:
    """Move any consonants followed by a 'y' in text to the end and append 'ay'
    
    :param text: str - A word containing 'y' with consonants before it
    :return str - A word with the leading consonants and y of text at the end with 'ay' appended
    """
    
    index = text.index('y')
    suffix = ''
    vowels_before_y = False
    for letter in text:
        if is_vowel(letter) and text.index(letter) < index:
            vowels_before_y = True
    if is_consonant(text[(index-1)]) and not vowels_before_y:
        for number in range(index):
            suffix += text[number]
        return text[index:] + suffix + 'ay'
    return rule2(text)

def translate(text: str) -> str:
    """Translate a string of English word(s) and returns the word(s) in Pig Latin

    :param text: str - A word or string of words to translate
    :return str - Translated word(s)
    """
    treated_text = text.split()
    result = ''
    words = len(treated_text)

    for word in treated_text:
        if words > 1 and len(result) != 0:
            result += ' '
        if word.startswith('xr') or word.startswith('yt') or is_vowel(word[0]):
            result += rule1(word)
            continue
        if 'qu' in word and not is_vowel(word[word.index('q')-1]):
            result += rule3(word)
            continue
        if is_consonant(word[0]):
            if 'y' in word and not word.startswith('y'):
                result += rule4(word)
                continue
            result += rule2(word)
            continue

    return result

