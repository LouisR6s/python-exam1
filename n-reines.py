def est_en_securite(tab, ligne, colonne, taille):
    # Vérifie si une dame peut être placée en (ligne, colonne) sur l'échiquier
    # sans être menacée par une autre dame déjà placée
    
    # Vérification de la colonne
    for i in range(ligne):
        if tab[i][colonne] == 1:
            return False
    
    # Vérification de la diagonale supérieure gauche
    for i, j in zip(range(ligne, -1, -1), range(colonne, -1, -1)):
        if tab[i][j] == 1:
            return False
    
    # Vérification de la diagonale supérieure droite
    for i, j in zip(range(ligne, -1, -1), range(colonne, taille)):
        if tab[i][j] == 1:
            return False
    
    return True

def placer_dames(tab, ligne, taille):
    # Fonction récursive pour placer les dames sur l'échiquier
    
    if ligne >= taille:
        return True
    
    for colonne in range(taille):
        if est_en_securite(tab, ligne, colonne, taille):
            tab[ligne][colonne] = 1
            if placer_dames(tab, ligne + 1, taille):
                return True
            tab[ligne][colonne] = 0
    
    return False

def resoudre_n_dames(taille):
    # Fonction principale pour résoudre le problème des N dames
    
    tab = [[0] * taille for _ in range(taille)]
    
    if not placer_dames(tab, 0, taille):
        print("Aucune solution trouvée.")
        return
    
    for ligne in tab:
        print(ligne)

# Exemple d'utilisation avec un échiquier 8x8
resoudre_n_dames(8)
