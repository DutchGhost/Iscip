def fen2gridgen(fen, fill='*'):
    lenght = len(fen.split('/')) - 1
    for (idx, row) in enumerate(fen.split('/')):
        for c in row:
            if not c.isdigit():
                yield c
            else:
                for _ in range(int(c)):
                    yield fill
        if idx != lenght:
            yield "\n"

def fen2grid(fen, fill='*'):
    return ''.join(fen2gridgen(fen, fill))

def grid2fengen(grid, fill='*'):
    lenght = len(grid.split('\n')) - 1
    for (idx, row) in enumerate(grid.split('\n')):
        n = 0
        for c in row:

            if c == fill:
                n += 1
            
            elif n > 0:
                yield str(n)
                yield(c)
                n = 0
            
            else:
                yield c
        if n > 0:
            yield str(n)
            n = 0
        if idx != lenght:
            yield '/'

def grid2fen(grid, fill='*'):
    return ''.join(grid2fengen(grid, fill))


if __name__ == '__main__':
    print(fen2grid('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR', '+'))
    print(grid2fen(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR', '+'), '+'))