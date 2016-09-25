

GRID_X = 10
GRID_Y = 22
grid = []

grid = [['.' for x in range(GRID_X)] for y in range(GRID_Y)]
    
for row in grid:
    for cell in row:    
        print(cell, end=' ')
    print('')