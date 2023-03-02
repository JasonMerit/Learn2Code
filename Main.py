# Kryds og bolle

board = [[1, 2, 0], [0, 0, 0], [1, 0, 0]]
letters = ["a ", "b ", "c "]

valid_first = ["a", "b", "c"]
valid_second = ["0", "1", "2"]

# letter / number
def show():
    print("   0  1  2 ")
    for i, b in enumerate(board):
        row = letters[i]
        for v in b:
            row += " x " if v == 1 else " o " if v == 2 else "[ ]"
        print(row)
    print()

show()

def get_input():
    print("X's turn - Type coordinate <xy>")
    user = input(">")
    while len(user) != 2 or user[0] not in valid_first or user[1] not in valid_second:
        print("Invalid input - Type coordinate <xy>")
        user = input(">")
    return user

x, y = get_input()
print("GREAT SUCCESS")
