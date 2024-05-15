def recherche_dichotomique(tableau, element_recherche):
    debut = 0
    fin = len(tableau) - 1

    while debut <= fin:
        milieu = (debut + fin) // 2
        milieu_element = tableau[milieu]

        if milieu_element == element_recherche:
            return milieu
        elif milieu_element < element_recherche:
            debut = milieu + 1
        else:
            fin = milieu - 1

    return -1

def afficher_tableau(tableau):
    print("Tableau trié :", tableau)

def saisie_tableau():
    while True:
        try:
            taille = int(input("Veuillez entrer la taille du tableau : "))
            if taille <= 0:
                print("Veuillez entrer un nombre entier positif.")
                continue
            break
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

    tableau = list(range(1, taille + 1))  # Générer une liste de 1 à taille
    print(f"Tableau de taille {taille} généré automatiquement.")
    return tableau

def recherche():
    tableau_entre = saisie_tableau()
    afficher_tableau(tableau_entre)
    
    while True:
        try:
            element_recherche = int(input("Entrez le nombre que vous cherchez : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

    index_trouve = recherche_dichotomique(tableau_entre, element_recherche)

    if index_trouve != -1:
        print(f"L'élément {element_recherche} se trouve à l'index {index_trouve} dans le tableau.")
    else:
        print(f"L'élément {element_recherche} ne fait pas partie du tableau.")

if __name__ == "__main__":
    recherche()
