import random

def deviner_nombre():
    ntentative = 0
    ppetit = int(input("Entrez le nombre le plus petit : "))
    pgrand = int(input("Entrez le nombre le plus grand : "))
    
    nombre_a_deviner = random.randint(ppetit, pgrand) 
    plage = pgrand - ppetit
    difference_maximale = max(abs(nombre_a_deviner - ppetit), abs(nombre_a_deviner - pgrand))
    bruler = difference_maximale * 0.05
    chauffer = difference_maximale * 0.1
    difference_precedente = None #pour "tu refroidis"

    while True:
        ntentative += 1
        proposition = int(input(f"Devinez le nombre entre {ppetit} et {pgrand} : "))

        difference = nombre_a_deviner - proposition
        difference_abs = abs(difference)
        
        if difference == 0:
            print(f"Bravo, Vous avez deviné le nombre en {ntentative} tentative(s) !")
            break
        elif difference_abs <= bruler:
            print("Tu brules !")
        elif difference_abs <= chauffer:
            print("Tu chauffes !")
        elif difference_precedente is not None and difference_abs > difference_precedente:
            print("Tu refroidis !")
        else:
            print("Tu geles !")

        difference_precedente = difference_abs

deviner_nombre()