PRICES = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1, 2]
QUESTIONS = [
                "Voer het aantal 1 centen in:\n",
                "Voer het aantal 2 centen in: \n",
                "Voer het aantal 5 centen in: \n",
                "Voer het aantal 10 centen in: \n",
                "Voer het aantal 20 centen in: \n",
                "Voer het aantal 50 centen in: \n",
                "Voer het aantal 1 euro's in: \n",
                "Voer het aantal 2 euro's in: \n"
            ]
            
if __name__ == '__main__':
    munten = [int(input(question)) for question in QUESTIONS]
    aantal_munten = sum(munten)
    totale_waarde = sum(quantity * value for (quantity, value) in zip(munten, PRICES))
    print("Totaal aantal munten: {}".format(aantal_munten))
    print("Totale waarde van de munten: {} euro".format(totale_waarde))