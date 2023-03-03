# Kryds og bolle


class Game1:
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    letters = ["a ", "b ", "c "]

    valid_first = ["a", "b", "c"]
    valid_second = ["0", "1", "2"]
    letter2num = {"a": 0, "b": 1, "c": 2}

    player = 1 # 0 = O, 1 = X
    
    def show(self):
        print("   0  1  2 ")
        for i, b in enumerate(self.grid):
            row = self.letters[i]
            for v in b:
                row += " x " if v == 1 else " o " if v == 2 else "[ ]"
            print(row)
        print()

    def get_input(self):
        """Get input from user and return it as a tuple (str, str)"""
        print("X's turn - Type coordinate >AN")
        user = ""
        while True:
            user = input(">")
            if user in ["q", "quit", "exit"]:
                quit()
            if len(user) == 2 and user[0] in self.valid_first and user[1] in self.valid_second:
                return user[0], user[1]
            print("Invalid input - Type coordinate >AN")


    def play(self):    
        y, x = self.get_input()  # TODO: Flip y and x or forget int(y)
        self.step(y, x)
        self.show()
        
    
    def step(self, y, x):
        """Place a mark on the grid at coordinate (y, x) (str, str) and switch player"""
        self.grid[self.letter2num[y]][int(x)] = self.player % 2
        self.player += 1

class Game():
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    action_space = [str(i) for i in range(9)]
    X_turn = True # player turn

    def __init__(self) -> None:
        self.show()
    
    def show(self):
        i = 0
        for b in self.grid:
            row = ""
            for v in b:
                row += " X " if v == 2 else " O " if v == 1 else f"[{i}]"
                i += 1
            print(row)
        print()

    def get_input(self):
        """Return valid action int input from user"""
        print(f"{'X' if self.X_turn else 'O'}'s turn")
        user = ""
        while True:
            user = input(">")
            if user in ["q", "quit", "exit"]:
                quit()
            if user in self.action_space:
                return int(user)
            print("Invalid action! - Try again")

    def play(self):    
        action = self.get_input()
        self.step(action)
        self.show()
    
    def step(self, action):
        """Place a mark on the grid at coordinate and switch player"""
        self.action_space.remove(str(action))  # TODO Error: pop bad indexing
        self.grid[action // 3][action % 3] = int(self.X_turn) + 1  # TODO Hack: Typecast bool to int
        self.X_turn = not self.X_turn                              # TODO Error: forget +1

if __name__ == "__main__":
    game = Game()
    while True:
        game.play()

