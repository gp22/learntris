import sys

GRID_X = 10 # X dimension for game grid
GRID_Y = 22 # Y dimension for game grid
game_grid = []
score = 0
cleared_lines = 0

def newGrid(X, Y):
    '''Input: int. X, int, Y
       Output: list. Y lists, each containing X '.'s
    '''
    new_grid = [['.' for x in range(X)] for y in range(Y)]
    return new_grid

def printGrid(grid_to_print): # print out the current game grid
    for row in grid_to_print:
        for cell in row:    
            print(cell, end=' ')
        print('')

def given(Y):
    '''Input: reads from standard input
       Output: list of Y lists. elements are read from standard input,
       split at spaces, each newline creates a new list.
    '''
    new_grid = [input().split() for _ in range(Y)]
    return new_grid
    
def main(): # main game loop

    game_grid = newGrid(GRID_X, GRID_Y)

    while True:
        desired_action = input()

        if desired_action == 'q':
            sys.exit()
        elif desired_action == 'p':
            printGrid(game_grid)
        elif desired_action == 'g':
            game_grid =given(GRID_Y)
        elif desired_action == 'c':
            game_grid = newGrid(GRID_X, GRID_Y)
        elif desired_action == '?s':
            print(score)
        elif desired_action == '?n':
            print(cleared_lines)

if __name__ == '__main__':
    main()