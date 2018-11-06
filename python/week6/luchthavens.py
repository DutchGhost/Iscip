from contextlib import suppress
from math import radians, cos, sin, sqrt, atan, pi
import csv

'''A named tuple, to return (distance, airport_id) for the stopover'''
from collections import namedtuple
Airport = namedtuple('Airport', ['distance', 'id'])

def filereader(file):
    with open(file, 'r') as f:
        next(f)
        for row in csv.reader(f, delimiter="\t"):
            row[1] = float(row[1])
            row[2] = float(row[2])
            yield (row[0].strip().replace("[", "").replace("]", ""), row[1:])

def leesLuchthavens(file):
    return dict(filereader(file))

#b = breedte = latitude
#l = lenghte = LONGitude
def afstand(code1, code2, luchthavens):
    R = 6372.795
    
    lucht_haven_a = luchthavens[code1]
    lucht_haven_b = luchthavens[code2]

    #get the longitude
    l1 = (lucht_haven_a[1] / 180) * pi
    l2 = (lucht_haven_b[1] / 180) * pi

    #get the latitude
    b1 = (lucht_haven_a[0] / 180) * pi
    b2 = (lucht_haven_b[0] / 180) * pi

    #the lefthandside of the upper part of the calculation
    lefthand_upper = (cos(b2) * sin(l1 - l2)) ** 2

    #the righthandside of the upper part of the calculation
    righthand_upper = ((cos(b1) * sin(b2)) - (sin(b1) * cos(b2) * cos(l1 - l2))) ** 2

    #upper part of the calculation
    upper = sqrt(lefthand_upper + righthand_upper)

    #the last one, we devide by this, 'devider', (noemer)
    down = (sin(b1) * sin(b2)) + (cos(b1) * cos(b2) * cos(l1 - l2))

    return round(R * atan((upper/down)), 7)

#walk over the keys in the dict.
#calculate the distance from a to c,
#if its less than reikwijdte, calculate the distance from c to b
#if that is less than reikwijdte, return the namedtuple.
#this named tuple is a tuple of the distance from a to c, plus c to b, AND the airport_id
def airportstream(code1, code2, luchthavens, reikwijdte):
    for code3 in filter(lambda code3: not(code3 in [code1, code2]), luchthavens.keys()):
        dist_a_c = afstand(code1, code3, luchthavens)
        if dist_a_c < reikwijdte:
            dist_c_b = afstand(code3, code2, luchthavens)
            if dist_c_b < reikwijdte:
                yield Airport(distance = dist_a_c + dist_c_b, id = code3)

def tussenlanding(code1, code2, luchthavens, reikwijdte=4000):
    if afstand(code1, code2, luchthavens) < reikwijdte:
        return None
    
    with suppress(ValueError):
        stream = airportstream(code1, code2, luchthavens, reikwijdte)
        return min(stream, key=lambda airport: airport.distance).id

    # Reached only on a ValueError.    
    return None

if __name__ == '__main__':
    dic = leesLuchthavens("luchthavens.txt")
    print(afstand('P60', 'MSN', dic))
    print(afstand('ADK', 'DCA', dic))
    print(tussenlanding('ADK', 'DCA', dic, 4000))