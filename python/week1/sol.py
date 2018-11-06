from contextlib import suppress
FACTOR = (24*60*60) + (39*60) + 35.244

if __name__ == '__main__':
    with suppress(ValueError):
        marsdays = int(input("geef het aantal Marsdagen(sol):\n"))

        #reken het ingevoerde aantal sol dagen om naar seconden op aarde
        earth_seconds = marsdays * FACTOR

        #divmod(x, n) returned de qotient (x / n), en de remainder (x % n)
        #hoeveel minuten passen er in ... seconden, en hoeveel seconden houden we over
        (m, s) = divmod(earth_seconds, 60)
        #hoeveel uur passen er in ... minuten, en hoeveel minuten houden we over
        (h, m) = divmod(m, 60)
        #hoeveel dagen passen er in ... uur, en hoeveel uur houden we over
        (d, h) = divmod(h, 24)

        print("{} sol = {} dagen, {} uren, {} minuten, en {} seconden".format(marsdays, int(d), int(h), int(m), int(s)))