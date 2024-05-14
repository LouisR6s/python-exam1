import random


def deviner_nombre():
    tentative = 0
    ppetit= int(input("Entrez le nombre le plus petit : "))
    pgrand = int(input("Entrez le nombre le plus grand : "))
    
    nombre_a_deviner = random.randint(ppetit, pgrand) 

    while True:
        tentative += 1
        proposition = int(input(f"Devinez le nombre entre {ppetit} et {pgrand} : "))


        difference = nombre_a_deviner - proposition

        if difference == 0:
            print(f"Bravo ! Vous avez deviné le nombre en {tentative} tentative(s) !")
            break
        elif abs(difference) <= 5:
            print("Tu brûles !")
        elif abs(difference) <= 10:
            print("Tu chauffes !")
        elif abs(difference) <= 20:
            print("Tu refroidis !")
        else:
            print("Tu gèles !")

deviner_nombre()
