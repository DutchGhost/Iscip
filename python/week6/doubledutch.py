'''yields (letter, word) for every letter - word in the given file'''
def translatestream(file):
    ERROR_MESSAGE = "ongeldige vertaling"
    klinkers = ["a", "e", "i", "o", "u"]
    medeklinkers = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    letters_seen = []
    with open(file, 'r') as f:
        for (letter, word) in map(lambda line: line.strip().split(' - '), f.readlines()):
            
            #Een regel een letter bevat die geen medeklinker is
            assert(not any(letter == c for c in klinkers))

            #een regel een lettergreep bevat die niet begint met de medeklinker op die regel
            assert(word.startswith(letter)), ERROR_MESSAGE

            #sommige medeklinkers van het alfabet meerdere keren voorkomen in het bestand
            assert(letter not in letters_seen), ERROR_MESSAGE

            letters_seen.append(letter)
            yield (letter, word)

def medeklinkers(file): 
    return dict(translatestream(file))
    
'''
if the character was upper, change the first item of the translation to uppercase, and return it
otherwise just return the translation
'''
def to_upper(item, is_upper):
    assert(len(item) > 0), "Strings passed to this function have to have a lenght of bigger than 0"
    if is_upper:
        return ''.join([item[0].upper(), item[1::]])
    else:
        return item

'''grab the first and the second item of the string'''
'''then yield (first, second), set first to second, set second to next(iterable)'''
'''if there's a StopIteration exception, yield (second, fillchar), and break'''
def windowed_by_two(word, fillchar=' '):
    iterable = iter(word)
    first = next(iterable)
    second = next(iterable)
    while True:
        try:
            yield (first, second)
            first = second
            second = next(iterable)
        except StopIteration:
            yield (second, fillchar)
            break
'''
first check if 'quat' is in last_append, if this is true we know that at the previous iteration
we had a double, c1 was equal to c2. But on this iteration c1 becomes c2, and we dont want to get
something like "Squatoho", so just do nothing then on the current iteration
and continue to the next iteration

If there was no 'quat' in last_appended,
get the lambda from the dict with 'c1 == c2', (that evaluates to either True or False)
than appy the lambda on c1.lower()

lastly we need to make it upper, so we call to_upper() on char_translate.

NOTE:
    the call to to_upper() is always safe, the lenght of the string we pass in is ALWAYS bigger than 0 due to the .get() calls.
    .get(c1, c1) returns the value of the dict associated with c1, and on a keyerror, it returns just c1. The lenght of c1 is always bigger than 0
'''
def translate(woord, dic):
    klinkers = ["a", "e", "i", "o", "u"]
    last_yielded = ""
    for (c1, c2) in windowed_by_two(woord):
        if "quat" in last_yielded:
            last_yielded = ""
            continue
        else:
            char_translate = {
                True : lambda c1: ''.join(["squat", d.get(c1, c1), "h"]),
                False : lambda c1: d.get(c1, c1),
            }[(c1 == c2 and c1.lower() in klinkers)](c1.lower())
            last_yielded = to_upper(char_translate, c1.isupper())
            yield last_yielded
            
def vertaalWoord(woord, d):
    return ''.join(translate(woord, d))
        
    
#This is just one big word???
def vertaal(zin, d):
    return vertaalWoord(zin, d)

if __name__ == '__main__':
    d = medeklinkers("dutchletters.txt")
    print(vertaalWoord("took", d))
    print(vertaalWoord('BAMBOO', d))
    print(vertaalWoord('Yesterday', d))
    print(vertaal('I took a walk to the park yesterday.', d))