from contextlib import suppress
def reverse_rot(message, rot):
    for c in message:
        if c in [' ', ',', '.', '!', '?']:
            yield c
        else:
            ascii = ord(c)
            rot = rot % 26
            shift = 97 if c.islower() else 65

            decrypted = (ascii - rot - shift) % 26
            decrypted += shift

            yield chr(decrypted)

if __name__ == '__main__':
    with suppress(ValueError):
        rot = int(input("Voer het aantal rotaties in: "))
    
        encrypted = input("Voer de ge-encrypte string in om te dycrypten: \t")

        print("De originele tekst is: '{}'.".format(''.join(reverse_rot(encrypted, rot))))