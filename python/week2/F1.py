"""
    naam: Kasper van den Berg
    studentnummer: s1101481
    opdracht: formule-1
"""

TIME_LIMIT = 120 * 60
DISTANCE_LIMIT = 305

def to_sec(n):
    return n * 60

def rounds(afstand, gem_tijd):
    #deze loop blijft lopen zolang de afgelegde afstand kleiner is dan 300km + afstand van 1 rondje,
    #En zolang de verstreken tijd kleiner is dan 2 uur.
    #Bij elke iteratie wordt er 1 bij n opgeteld, n staat voor het aantal rondjes.
    #Op deze manier hebben we precies het aantal goede rondjes als de conditie niet meer waar is
    n = 1
    while (n * afstand < DISTANCE_LIMIT) and (n * gem_tijd < TIME_LIMIT):
        n += 1
    return n

def print_antwoord(land, rondes, afstand):
    print("De grote prijs van {} wordt verreden over {} ronden ({} km)".format(land, rondes, round(afstand, 3)))

if __name__ == '__main__':
    land = input("Voer het land in waar de race gereden wordt:\n")
    if land != "Monaco":
        try:
            afstand = float(input("Voer de afstand van 1 rondje in (in kilometer): \n"))
            gem_tijd = to_sec(float(input("Voer de gemiddelde tijd van 1 rondje in In minuten): \n")))
        except ValueError:
            exit("voer een valide getal in.")
        rondes = rounds(afstand, gem_tijd)

        print_antwoord(land, rondes, afstand * rondes)
    else:
        print_antwoord("Monaco", 78, 260.52)