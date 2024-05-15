text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse consectetur augue augue. Curabitur tortor ante, tempus sit amet massa non, consequat faucibus ipsum. Mauris ornare vel sapien in vulputate. Aliquam erat volutpat. Vestibulum gravida libero vitae ligula tempus suscipit. Aenean facilisis bibendum ligula at ultrices. Aliquam finibus lectus luctus leo mollis, malesuada sagittis elit iaculis. Sed porttitor libero a enim feugiat, quis tristique erat malesuada. Aenean non convallis sem, in eleifend libero. Curabitur vitae mi ut sapien faucibus venenatis. Vestibulum vel blandit augue. In vel mauris lorem. Quisque tincidunt urna porttitor velit porttitor porta. Nam accumsan accumsan nisi, ac posuere ante semper eu. Fusce tincidunt semper mi et feugiat."

letter_counts = {}

for char in text:
    char = char.lower()
    if char.isalpha():
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

# Ici on cherche la valeur maximum pour l'utiliser en tant que 100%
max_count = max(letter_counts.values())

for letter, count in sorted(letter_counts.items()):
    num_blocks = (count * 10) // max_count
    print(f"{letter} {'■' * num_blocks}")