LOOKUP = {
    'abc': '2',
    'def': '3',
    'ghi': '4',
    'jkl': '5',
    'mno': '6',
    'pqrs': '7',
    'tuv': '8',
    'wxyz': '9',
}

def translate(message):
    for c in map(lambda c: c.lower(), message):
        for (key, value) in LOOKUP.items():
            if c in key:
                yield value
                break

def T9(message):
    return ''.join(translate(message))
    
def GSMoniemen(message1, message2):
    return T9(message1) == T9(message2)