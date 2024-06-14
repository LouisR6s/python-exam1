import random
import os

def charger_mots(chemin_fichier):
    mots = []
    with open(chemin_fichier, 'r', encoding='utf-8') as f:
        mots.extend(f.read().splitlines())
    return mots

def choisir_mot(mots):
    return random.choice(mots)

def afficher_mot(mot, lettres_trouvees):
    affichage = ''
    for lettre in mot:
        if lettre in lettres_trouvees:
            affichage += lettre
        else:
            affichage += '_ '
    return affichage

def afficher_bonhomme(tentatives):
    hangman = [
        '''
   +---+
       |
       |
       |
      ===''', 
        '''
   +---+
   O   |
       |
       |
      ===''', 
        '''
   +---+
   O   |
   |   |
       |
      ===''', 
        '''
   +---+
   O   |
  /|   |
       |
      ===''', 
        '''
   +---+
   O   |
  /|\  |
       |
      ===''', 
        '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', 
        '''
   +---+
   O   |
  /|\  |
  / \  |
      ==='''
    ]
    return hangman[6 - tentatives]

def jeu_pendu():
    mots = charger_mots('mots_francais.txt')
    mot_a_deviner = choisir_mot(mots)
    lettres_trouvees = []
    lettres_ratees = []
    tentatives_restantes = 6

    print("BIenvenu !")
    
    while tentatives_restantes > 0:
        print(afficher_bonhomme(tentatives_restantes))
        print("\nMot à deviner:", afficher_mot(mot_a_deviner, lettres_trouvees))
        print(f"Tentatives restantes: {tentatives_restantes}")
        print(f"Lettres déjà proposées: {', '.join(lettres_ratees)}")

        lettre = input("Proposez une lettre: ").lower()

        if lettre in lettres_trouvees or lettre in lettres_ratees:
            print("Vous avez déjà proposé cette lettre.")
            continue

        if lettre in mot_a_deviner:
            lettres_trouvees.append(lettre)
            if all(l in lettres_trouvees for l in mot_a_deviner):
                print("\nFélicitations! Vous avez deviné le mot:", mot_a_deviner)
                break
        else:
            lettres_ratees.append(lettre)
            tentatives_restantes -= 1
            print("Lettre incorrecte!")

        if tentatives_restantes == 0:
            print(afficher_bonhomme(tentatives_restantes))
            print("\nVous avez perdu! Le mot était:", mot_a_deviner)

if __name__ == "__main__":
    jeu_pendu()
