from contextlib import suppress

SPECIALS = "~`!@#$%^&*()_-+={}[]:>;',</?*-+"

CONDITIONS = [
                lambda password: len(password) >= 8,
                lambda password: any(c.isupper() for c in password),
                lambda password: any(c.islower() for c in password),
                lambda password: any(c.isdigit() for c in password),
                lambda password: any(c in SPECIALS for c in password)
            ]
            
def sterkte(sterkte):
    #als aan alle criteria voldaan wordt is het sterk,
    if sterkte == len(CONDITIONS):
        return "sterk"    
    #anders matig,
    elif sterkte == 4 or sterkte == 3:
        return "matig"
    #anders zwak
    else:
        return "zwak"

if __name__ == '__main__':
    with suppress(ValueError):
        n = int(input("Voer in hoeveel wachtwoorden je in gaat voeren:\n"))
        
        if n < 1 or n > 100:
            exit("Voer een valide getal tussen de 1 en 100 in.")
    
        passwords = [input() for _ in range(n)]

        print()
 
        for password in passwords:
            print(sterkte(sum(condition(password) for condition in CONDITIONS)))