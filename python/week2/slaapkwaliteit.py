"""returns the time difference in minits from whenever you went to sleep, and whenever you're waking up"""
def diff(time_sleep_h, time_sleep_m, time_wake_h, time_wake_m):
    #aantal minuten tot 12 uur
    minits_before_midnight = (24 * 60) - (time_sleep_h * 60 + time_sleep_m)

    return (time_wake_h * 60) + time_wake_m + minits_before_midnight

"""ask the user for input with the message.
Raises an AssertionError if the input was not > 0 and < 24
Raises a ValueError if the given input wasn't a valid int
"""
def get_uur(message):
    uur = int(input(message))
    assert(uur >= 0 and uur < 24), "Voer een getal tussen de 0 en 24 in."
    return uur

"""ask the user for input with the message.
Raises an AssertionError if the input was not > 0 and < 60
Raises a ValueError if the given input wasn't a valid int
"""
def get_minuut(message):
    minuut = int(input(message))
    assert(minuut >= 0 and minuut < 60), "Voer een getal tussen de 0 en 60 in."
    return minuut

#fancy formatting voor de string om te printen
def print_tijd(wakker_uur, wakker_minuut):
    tijd = {
        (True, True): "0{}:0{}".format(wakker_uur, wakker_minuut),
        (True, False): "0{}:{}".format(wakker_uur, wakker_minuut),
        (False, True): "{}:0{}".format(wakker_uur, wakker_minuut),
        (False, False): "{}:{}".format(wakker_uur, wakker_minuut),
    }[(wakker_uur < 10, wakker_minuut < 10)]
    
    print(tijd)

if __name__ == '__main__':
    try:
        slaap_uur = get_uur("Voer het uur dat je gaat slapen in:\n")
        slaap_minuut = get_minuut("Voer de minuut dat je gaat slapen in:\n")

        wakker_uur = get_uur("Voer het uur dat je wakker wil worden in\n")
        wakker_minuut = get_minuut("Voer de minuut dat je wakker wil worden in\n")

    except AssertionError as e:
        exit("{}".format(e))
    except ValueError:
        exit("Voer een valide getal in.")

    #als je gaat slapen na 24:00 wordt het keer -1 gedaan
    if slaap_uur < 12:
        slaap_uur *= -1
    
    #zolang het verschil niet gelijk aan 90 is, tel 1 bij de minuten op.
    #hierbij wordt rekening gehouden met dat er maar 60 minuten in een uur zitten.
    while diff(slaap_uur, slaap_minuut, wakker_uur, wakker_minuut) % 90 != 0:
        if wakker_minuut > 59:
            wakker_minuut = 0
            wakker_uur += 1
        wakker_minuut += 1

    print_tijd(wakker_uur, wakker_minuut)