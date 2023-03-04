# Kryds og bolle

class Game():
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # 1 = O, 2 = X
    action_space = [str(i) for i in range(9)]
    X_turn = True # player turn

    def __init__(self) -> None:
        self.show()

    def reset(self):
        """Reset game"""
        self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.action_space = [str(i) for i in range(9)]
        self.X_turn = True
        self.show()

    def play(self):
        action = self.get_input()
        if action == "r":
            self.reset()
            return
        
        if self.step(int(action)):
            print(f"{'X' if not self.X_turn else 'O'} won!")  # TODO Error: forget not
            self.show()
            print("Press enter to restart")
            input(">")
            self.reset()
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
        """Return valid action str input from user"""
        print(f"{'X' if self.X_turn else 'O'}'s turn")
        user = ""
        while True:
            user = input(">")
            if user in ["q", "quit", "exit"]:
                quit()
            if user in self.action_space + ["r"]:
                return user
            print("Invalid action! - Try again")
    
    def step(self, action):
        """Place a mark on the grid at coordinate and switch player"""
        # self.action_space.pop(str(action))
        self.action_space.remove(str(action))  # TODO Error: pop bad indexing
        self.grid[action // 3][action % 3] = int(self.X_turn) + 1  # TODO Hack: Typecast bool to int
        self.X_turn = not self.X_turn                              # TODO Error: forget +1
        return self.game_over()            
    
    def game_over(self):
        """Return True if game over"""
        # Check rows
        for row in self.grid:
            if row[0] == row[1] == row[2] and row[0] != 0:                
                return True
        # Check columns
        for i in range(3):
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] and self.grid[0][i] != 0:                
                return True
        # Check diagonals
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] != 0:            
            return True
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] != 0:            
            return True
        # Check draw
        if len(self.action_space) == 0:
            print("Draw!")
            return True
    
if __name__ == "__main__":
    game = Game()
    while True:
        game.play()

