# Jessie Jenkins

# CMIT-135

# Week 5 - Character Picture Grid

# Grid matrix to be used for image.
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Prints matrix
for x in range(6):
    for y in range(9):
        if y < 8:
            print(grid[y][x], end="")
        else:
            print(grid[y][x])
