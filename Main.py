import os
clear = lambda: os.system('cls')

grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # X : 2, O : 1
action_space = [str(x) for x in range(9)]
X_turn = True

def show():
    i = 0
    for b in grid:
        row = ""
        for v in b:
            row += " X " if v == 2 else " O " if v == 1 else f"[{i}]"
            i += 1
        print(row)
    print()

clear()
show()
print("type cell number to place piece")

def get_input():
    """Return valid input and quits"""
    while True:
        action = input('>')
        if action in ['quit', 'q', 'the russians are coming']:
            quit()
        if action in action_space:
            return action

def step(action):
    """Update grid at action with player symbol. Flips player turn"""
    global X_turn
    y = action // 3
    x = action % 3
    grid[y][x] = 2 if X_turn else 1

    X_turn = not X_turn
    
while True: 
    action = get_input()
    step(int(action))
    
    clear()
    show()





    