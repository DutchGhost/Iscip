'''Als x of y 0 is, voeg 'n' toe aan de row. Anders, de som van het veld links en boven van het huidige veld.'''
def vierkant(m, n=1):
    results = []
    for y in range(m):
        row = []
        for x in range(m):
            if x == 0 or y == 0:
                row.append(n)
            else:
                row.append(results[y - 1][x] + row[x - 1])
        results.append(row)
    return results


def paths(m, n = 1):
    square = vierkant(m, n)
    max_x = max_y = len(square) - 1
    padding = len(str(square[max_y][max_x]))

    for (idx, row) in enumerate(square):
        for item in row:
            n_spaces = 1 + padding - len(str(item))
            spaces = ''.join([' ' for _ in range(n_spaces)])
            yield ''.join([spaces, str(item)])
        if idx != max_x:
            yield "\n"

def paden(m, n = 1):
    return ''.join(paths(m, n))

if __name__ == '__main__':
    print(paden(19, 20))