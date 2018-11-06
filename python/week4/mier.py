from functools import partial
from itertools import islice
from enum import Enum

class Wall(Enum):
    RIGHT = "RIGHT",
    LEFT = "LEFT",
    UPPER = "UPPER",
    BOTTEM = "DOWN",
    NONE = "NONE"

#returns a chunk of the iterable
def take(n, iterable):
    return list(islice(iterable, n))

#returns a chucked iterator over the iterable
def chunk(iterable, n):
    return iter(partial(take, n, iter(iterable)), [])

def to_string(iterable, positional = " "):
    for row in iterable:
        yield positional.join(row)

def tekst(matrix):
    return '\n'.join(to_string(matrix))

"""First do 2 asserts.
One to check if the input is squarable (n * n should be equal to the lenght of 'configuratie'),
and another to check if there's no other character than '^', '>', 'v' or '<'.
"""
def rooster(n, configuratie):
    valids = ['^', '>', 'v', '<']
    
    assert(n * n == len(configuratie)), "ongeldige argumenten"
    assert(all(map(lambda token: token in valids, configuratie))), "ongeldige argumenten"
    
    return list(chunk(configuratie, n))

"""Walls are only important if the next step would be in the wall.
so if the field is '<', and the x = 0...we return the the wall is "LEFT".
MAX_X and MAX_Y are the maximum x and y values in the matrix.
"""
def type_wall(x, y, field, MAX_X, MAX_Y):
    if field == '<' and x == 0: return Wall.LEFT
    elif field == '^' and y == 0: return Wall.UPPER
    elif field == '>' and x == MAX_X: return Wall.RIGHT
    elif field == 'v' and y == MAX_Y: return Wall.BOTTEM
    else: return Wall.NONE

def turn_field(field):
    if field == '^': return '>'
    if field == '>': return 'v'
    if field == 'v': return '<'
    if field == '<': return '^'

"""ONLY perform a step if we can.
   NOTE:
        with the y axis, we subtract 1 if the wall is NOT 'UPPER' and the field is '^',
        and we add 1 if the wall is NOT 'BOTTEM' and the field is 'v'
        this is becouse the higher we go in the matrix, the lesser the y value becomes.
"""
def nxt(type_wall, current_x, current_y, field):
    return \
    {
        '^': lambda wall: (current_y, current_x) if wall == Wall.UPPER else (current_y - 1, current_x),
        '>': lambda wall: (current_y, current_x) if wall == Wall.RIGHT else (current_y, current_x + 1),
        'v': lambda wall: (current_y, current_x) if wall == Wall.BOTTEM else (current_y + 1, current_x),
        '<': lambda wall: (current_y, current_x) if wall == Wall.LEFT else (current_y, current_x - 1),
    }[field](type_wall)

def stap(matrix, y_x):
    (y, x) = y_x
    MAX_X, MAX_Y = (len(matrix) - 1, len(matrix) - 1)
    for (current_y, row) in enumerate(matrix):
        for (current_x, field) in enumerate(row):
            if (current_x, current_y) == (x, y):
                wall = type_wall(current_x, current_y, field, MAX_X, MAX_Y)            
                matrix[current_y][current_x] = turn_field(field)
                return nxt(wall, current_x, current_y, field)

"""first yield current.
Then, for as long as the end is not reached, set a step, and yield that step.
"""
def stepstream(matrix, start, end):
    current = start
    yield current
    while current != end:
        current = stap(matrix, current)
        yield current


def stappen(matrix):
    start = (len(matrix) - 1, 0)
    stop = (0, len(matrix) - 1)
    return list(stepstream(matrix, start, stop))

if __name__ == '__main__':
    vierkant = rooster(4, ">>>>^<^v^v^^>>v>")
    
    print(tekst(vierkant))
    t = stappen(vierkant)
    print(t)

    #print(tekst(vierkant))