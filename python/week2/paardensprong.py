from collections import namedtuple

Point = namedtuple('Point', ['field', 'location'])
Location = namedtuple('Location', ['x', 'y'])

"""these constants are used in boardstream(), for the creation of the fields"""
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
CIJFERS = ['1', '2', '3', '4', '5', '6', '7', '8']

def boardstream():
    for y, number in enumerate(reversed(CIJFERS)):
        for x, letter in enumerate(LETTERS):
            yield Point(field = ''.join([letter, number]), location = Location(x = x, y = y))

def boardfilter(from_field, to_field):
    return filter(lambda point: point.field in [from_field, to_field], boardstream())

"""a horse jump is either a difference on 2 of the x-axis and 1 on the y-axis, OR 1 on the x-axis and 2 on the y-axis.
This means that a horse jump is valid if the value of the absolute difference of point_a and point_b is either (2, 1) or (1, 2)
"""
def valid_jump(point_a, point_b):
    valids = [(2, 1), (1, 2)]
    diff_x = abs(point_a.x - point_b.x)
    diff_y = abs(point_a.y - point_b.y)
    return (diff_x, diff_y) in valids

if __name__ == '__main__':
    from_field = input("Vanaf welk veld ga je Springen?: ")
    to_field = input("Naar welk veld ga je springen?: ")

    board = boardfilter(from_field, to_field)
    location_a = next(board).location
    location_b = next(board).location

    if valid_jump(location_a, location_b):
        print("Het paard kan springen van {} naar {}".format(from_field, to_field))
    else:
        print("Het paard kan niet springen van {} naar {}".format(from_field, to_field))