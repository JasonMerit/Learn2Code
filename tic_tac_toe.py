# Kryds og bolle
import random

class TicTacToe():
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # 1 = O, 2 = X
    letters = [chr(i) for i in range(65, 65 + 3)]
    numbers = [str(i) for i in range(3)]
    letter_coords = "   " + "  ".join(letters)
    action_space = list(range(9))
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
        while True:
            user = self.get_input()
            x, y = user[0].upper(), user[1:]          
            if y in self.numbers and x in self.letters:
                x, y = ord(x) - 65, int(y)       
                if self.grid[y][x] == 0:                              
                    break
            print("Invalid action! - Try again")
        
        done = self.step(x, y)
        self.show()
        
        if done:
            print(f"{'X' if not self.X_turn else 'O'} won!")  # TODO Error: forget not
            print("Press enter to restart")
            input(">")
            self.reset()
        

    def show(self):
        print(self.letter_coords)
        for i, b in enumerate(self.grid):
            row = f"{i} "
            for v in b:
                row += " X " if v == 2 else " O " if v == 1 else "[ ]"
            print(row)
        print()

    def get_input(self):
        """Input from user (>1) or quit"""
        print(f"{'X' if self.X_turn else 'O'}'s turn")
        
        while True:
            user = input(">")
            if user in ["q", "quit", "exit"]:
                quit()
            if len(user) > 1:
                return user
    
    def step(self, x, y):
        """Place a mark on the grid at coordinate and switch player"""
        self.grid[y][x] = int(self.X_turn) + 1  # TODO Hack: Typecast bool to int
        self.X_turn = not self.X_turn           # TODO Error: forget +1
        self.action_space.remove(y * 3 + x)
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
    
    def random_step(self):
        """Take a random action"""
        action = random.choice(self.action_space)
        x, y = int(action) % 3, int(action) // 3
        print(x, y)
        return self.step(x, y)
    
if __name__ == "__main__":
    game = TicTacToe()
    while True:
        game.play()

