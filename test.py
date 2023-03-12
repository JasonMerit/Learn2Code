import os
import time

def clear():
    os.system("cls || clear")


print("Hello world!")
time.sleep(4.2)
clear()



# r = 3; c = 10
# grid = [[0 for _ in range(c)] for _ in range(r)]  # 1 : X hit, 2 : . miss
# grid[1][2] = 1
# grid[1][7] = 2

# # charcast A 
# A = chr(65)

# letters = [chr(i) for i in range(65, 65 + c)]
# letters = "   " + "  ".join(letters)


# def show():
#     print(letters)
#     for i, b in enumerate(grid):
#         row = f"{i} "
#         for v in b:
#             row += "[X]" if v == 2 else "[O]" if v == 1 else "[ ]"
#         print(row)
#     print()

# import random
# action = 3
# x, y = int(action) % 3, int(action) // 3
# print(x, y)


