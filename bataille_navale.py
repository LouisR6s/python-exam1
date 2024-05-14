import string
import emoji
def print_horizontal_line(num_tiles=6):
    # Ici j'ai déconstruit le cube en plusieurs parties pour formatter avec les lettres
    top_part = " --- "
    middle_part_to_format = "| {} |"
    bottom_part = " --- "
    
    # Ici on peut générer avec les lettres voulues (il y a un espace avant les lettres sinon les lettres ne sont pas bien alignées)
    alphabet = "  ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    middle_parts = []
    for i in range(num_tiles):
        letter = alphabet[i + 1]
        middle_part = middle_part_to_format.format(letter)
        middle_parts.append(middle_part)
    
    # Pour définir l'espace entre les tiles
    space_between_tiles = " "
    
    # Maintenant on peut construire chaque ligne en joignant les parties entre elles
    top_line = space_between_tiles.join([top_part] * num_tiles)
    middle_line = space_between_tiles.join(middle_parts)
    bottom_line = space_between_tiles.join([bottom_part] * num_tiles)
    print(top_line)
    print(middle_line)
    print(bottom_line)

def print_row_of_grid(chars):
    # Remplacer chaque caractère donné dans le modèle de tile
    top_part = " --- "
    bottom_part = " --- "
    middle_parts = [f"| {char} |" for char in chars]
    
    space_between_tiles = " "
    
    top_line = space_between_tiles.join([top_part] * len(chars))
    middle_line = space_between_tiles.join(middle_parts)
    bottom_line = space_between_tiles.join([bottom_part] * len(chars))
    
    return [top_line, middle_line, bottom_line]

def print_grid_with_rows(num_rows, num_tiles, grid):
    print_horizontal_line(num_tiles+1)
    
    for i in range(num_rows):
        row_index = i + 1  # J'ajoute un c'est plus parlant que de commencer à 0
        left_row_top = f" ___ "
        left_row_middle = f"| {row_index} |"
        left_row_bottom = f"|___|"
        
        tile_lines = print_row_of_grid(grid[i])
        
        print(left_row_top + " " + tile_lines[0])
        print(left_row_middle + " " + tile_lines[1])
        print(left_row_bottom + " " + tile_lines[2])

num_rows = 5
num_tiles = 6
grid = []
for i in range(num_rows):
    row = [" "] * num_tiles
    grid.append(row)

print_grid_with_rows(num_rows, num_tiles, grid)

def create_grid(position,value):
    try:
        # Ici on as besoin d'obtenir la position basé sur la lettre de la columne
        column = string.ascii_uppercase.index(position[0].upper())
        
        # Convertir le chiffre du row en index (1=0, 2=1, etc.)
        row = int(position[1]) - 1
        
        #On vérifie si tout ici est valide
        if 0 <= row < num_rows and 0 <= column < num_tiles:
            # Et enfin on update le grid
            grid[row][column] = value
        else:
            print("Position invalide, essayez encore.")
    except ValueError:
        print("Entrée invalide, essayez encore.")
    
    print_grid_with_rows(num_rows, num_tiles, grid)

count = 5
while True:
    if count == 0:
        print("Tu as posé tout tes bateaux")
        break
    else:
        print(f"Il te reste {count} bateaux à poser")  
    user_input = input("Ou veux tu poser tes bateaux ? (par exemple, A1): ")
    count = count - 1  
    create_grid(user_input,"🚤")
