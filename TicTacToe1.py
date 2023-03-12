"""SCRIPT"""
import random

grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# grid = [[0, 1, 0], [1, 2, 2], [1, 0, 0]]
cell2str = {-1: 'DRAW', 0: '[ ]', 1: ' O ', 2: ' X '}
action_space = [(x, y) for x in range(3) for y in range(3)]
X_turn = True


def show():
    print('\n   A  B  C')
    for i, row in enumerate(grid):
        txt = f'{i} '
        for cell in row:
            txt += cell2str[cell]
        print(txt)


def get_input():
    """Get input from user and return it as grid coordinates"""
    while True:
        print("Type input <xy>")
        user = input("> ").upper()
        if user in ['Q', 'QUIT', 'EXIT', 'BYE']:
            quit()
        
        if len(user) != 2:
            continue
        x, y = int(ord(user[0])) - 65, int(user[1])
        
        if (x, y) in action_space:
            return x, y


def step(x, y):
    """Get input from user, update grid and remove action from action_space"""
    global X_turn
    grid[y][x] = int(X_turn) + 1
    action_space.remove((x, y))
    X_turn = not X_turn

def check_win():
    """Check if there is a winner. 
    Returns -1 : Draw, 0 : No winner, 1 : O wins, 2 : X wins"""

    if not action_space:
        return -1

    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != 0:
            return grid[i][0]  # Column
        if grid[0][i] == grid[1][i] == grid[2][i] != 0:
            return grid[0][i]  # Row
        
    # Diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] != 0:
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] != 0:
        return grid[0][2]
    
    return 0  # No winner

def random_step():
    """Randomly choose an action from action_space and step"""
    x, y = random.choice(action_space)
    step(x, y)


if __name__ == '__main__':
    show()
    while True:
        # x, y = get_input()
        # step(x, y)
        random_step()
        show()
        if k := check_win():
            print(f'{cell2str[k]} wins!')
            break