def response(hey_bob):
    if hey_bob.strip().endswith('?'):
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        return 'Sure.'
    if hey_bob.isupper():
        return 'Whoa, chill out!'
    if hey_bob.isspace() or hey_bob == '':
        return 'Fine. Be that way!'
    return 'Whatever.'
