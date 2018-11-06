AVG = 70

FUNCTIONS = [
                lambda geslacht: 0 if geslacht == 'man' else 4,
                lambda rookt: -5 if rookt else 5,
                lambda sport: -3 if not sport else sport,
                lambda alcohol: 2 if not alcohol else -((alcohol - 7) * 0.5) if alcohol > 7 else 0,
                lambda fastfood: 3 if not fastfood else 0,
            ]

def levensverwachting(geslacht, roker, sport, alcohol, fastfood):
    return AVG + sum(func(variable) for (func, variable) in zip(FUNCTIONS, [geslacht, roker, sport, alcohol, fastfood]))