"""
    naam: Kasper van den Berg
    studentnummer: s1101481
    opdracht: Game of Life
"""

from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])

def toonGeneratie(grid):
    for row in grid:
        print(' '.join([c for c in map(lambda alive: 'X' if alive else 'O', row)]))

def in_range(current_point, field_point):
    valids = [(0, 1), (1, 0), (1, 1)]
    
    diff_x = abs(current_point.x - field_point.x)
    diff_y = abs(current_point.y - field_point.y)

    return (diff_x, diff_y) in valids

#als de huidige coordinaten in range zijn, en het huidige field True is, hebben we een buur gevonden
def neighborstream(generatie, field_point):
    for current_y, row in enumerate(generatie):
        for current_x, field in enumerate(row):
            if in_range(Point(x = current_x, y = current_y), field_point) and field == True:
                yield 1

def aantalBuren(generatie, y, x):
    return sum(neighborstream(generatie, Point(x=x, y=y)))
    
"""Als een levende cel (field == True) door 2 of 3 buurcellen omgeven wordt, blijft deze in de volgende generatie leven
als een dode cel omgeven wordt door 3 levende cellen, wordt deze cel levend.
"""
def field_is_alive(old_generation, field_point, field):
    aantal_buren = aantalBuren(old_generation, field_point.y, field_point.x)
    return (aantal_buren in [2, 3] and field == True) or aantal_buren == 3

'''loop over the rows in the old generation,
   make a new row, and fill with with booleans based on if the field is alive
'''
def new_rows(old_generation):
    for y, row in enumerate(old_generation):
        yield [field_is_alive(old_generation, Point(x = x, y = y), field) for x, field in enumerate(row)]

'''maak een list van new_rows(old_generation). Dit wordt dus een list van lists, new_rows yields rows'''
def volgende_generatie(old_generation):
    return list(new_rows(old_generation))

if __name__ == '__main__':
    generatie = [[True] + [False] * 7 for _ in range(6)]
    for i in generatie:
        print(i)
    toonGeneratie(generatie)

    print()
    nxt = volgende_generatie(generatie)
    toonGeneratie(nxt)

    print()
    nxt = volgende_generatie(nxt)
    toonGeneratie(nxt)

    print()
    nxt = volgende_generatie(nxt)
    toonGeneratie(nxt)

    print()
    nxt = volgende_generatie(nxt)
    toonGeneratie(nxt)