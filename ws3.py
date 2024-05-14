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
    print("Tablea trié :", tableau)

def tableau():
    # Exemple de tableau trié
    tableau = [2, 4, 7, 9, 13, 16, 19, 22, 25]
    element_recherche = 16

    afficher_tableau(tableau)
    
    index_trouve = recherche_dichotomique(tableau, element_recherche)

    if index_trouve != -1:
        print(f"L'élément {element_recherche} se trouve à l'index {index_trouve}")
    else:
        print(f"L'élément {element_recherche} n'a pas été trouvé")

if __name__ == "__main__":
    tableau()
