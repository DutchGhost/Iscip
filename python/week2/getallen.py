"""
    naam: Kasper van den Berg
    studentnummer: s1101481
    opdracht: Interessante getallen
"""

"""Infinite counter"""
def count(start=0, step=1):
    n = start
    while True:
        yield n
        n += step

"""for each n in the iterable,
   this function yields a number, where the number % n equals 0,
   and the sum of the characters of number are n.
"""
def calculate_numbers(iterable):
    for n in iterable:
        for candidate in filter(lambda number: number % n == 0, count(0, 1)):
            if sum(int(c) for c in str(candidate)) == n:
                yield candidate
                break

"""for each given input, yield the input if it was valid
also, the call on print() is just so we have fancy printing in main
"""
def read_inputs(number):
    for i in range(number):
        n = int(input("geef getal {} in. ({}/{}) in: \t".format(i+1, i+1, number)))
        if n < 100 and n > 0:
            yield n
        else:
            raise ValueError
    print()

if __name__ == '__main__':
    try:
        total_inputs = int(input("Geef aan hoeveel getallen je gaat invoeren (tussen de 0 en 50): \n"))
        if total_inputs < 50:
            to_calculate = list(read_inputs(total_inputs))
            for result in calculate_numbers(to_calculate):
                print(result)
        else:
            raise ValueError
    except ValueError:
        exit("Voer valide getallen in.")