def print_horizontal_line(num_tiles=7):
    #Ici j'ai déconstruit le cube en plusieurs partie pour formatter avec les lettres
    top_part = " --- "
    middle_part_to_format = "| {} |"
    bottom_part = " --- "
    
    # Ici on peut générer avec les lettres voulues (il y'a un espace avant les lettres sinon les lettres ne sont pas bien allignés)
    alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    middle_parts = []
    for i in range(num_tiles):
        letter = alphabet[i]
        middle_part = middle_part_to_format.format(letter)
        middle_parts.append(middle_part)
    
    # Pour définir l'epsace en les tiles
    space_between_tiles = " "
    
    # Maintenant on peut construit chaque lignes en joignant les parties entre elles
    top_line = space_between_tiles.join([top_part] * num_tiles)
    middle_line = space_between_tiles.join(middle_parts)
    bottom_line = space_between_tiles.join([bottom_part] * num_tiles)
    print(top_line)
    print(middle_line)
    print(bottom_line)

def print_row_of_grid(num_tiles=6):
    tile = [
        " --- ",
        "| X |",
        " --- "
    ]
    space_between_tiles = " "
    tile_lines = []
    for line in tile:
        # Ici on join avec des espaces
        joined_line = space_between_tiles.join([line] * num_tiles)
        # On rajoute au dico
        tile_lines.append(joined_line)
    return tile_lines

num_rows = 5

print_horizontal_line()
for i in range(num_rows):
    i+=1 #J'ajoute un c'est plus parlant que de commencer à 0
    left_row_top = f" ___ "
    left_row_middle = f"| {i} |"
    left_row_bottom = f"|___|"
    
    tile_lines = print_row_of_grid()
    
    print(left_row_top + " " + tile_lines[0])
    print(left_row_middle + " " + tile_lines[1])
    print(left_row_bottom + " " + tile_lines[2])
