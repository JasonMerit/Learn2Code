# Kryds og bolle
import random

class Board():

    def __init__(self, size, cell_strings, valid_cells=[0], label=""):
        self.size = size
        self.cell_strings = cell_strings
        self.valid_cells = valid_cells  # TODO: Forget to generalize valid cells
        self.label = label

        self.width, self.height = size
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.letters = [chr(i) for i in range(65, 65 + self.width)]
        self.numbers = [str(i) for i in range(self.height)]
        self.letter_coords = "   " + "  ".join(self.letters)
        self.action_space = list(range(self.width*self.height))

    def show(self):
        """Print grid with label"""
        if self.label:
            print(self.label)
        print(self.letter_coords)
        for i, b in enumerate(self.grid):
            row = f"{i} "
            for v in b:
                row += self.cell_strings[v]
            print(row)
        print()
    
    def get_input(self):
        """Returns valid action from user (>1) or quit"""        
        
        while True:
            user = input(">")

            if user in ["q", "quit", "exit"]:
                quit()

            if len(user) == 2:
                x, y = user[0].upper(), user[1]          
                if x in self.letters and y in self.numbers:  # valid input
                    x, y = ord(x) - 65, int(y)       
                    if self.grid[y][x] in self.valid_cells:     # valid action                         
                        return x,  y
                    
            print("Invalid action! - Try again")
    
    def get_random_action(self):
        """Step in random action. Return True if game over"""
        action = random.choice(self.action_space)
        x, y = int(action) % self.width, int(action) // self.height  # TODO: Forget to generalize width and height
        print(f'Random action: ({x}, {y})')
        return x, y


class TicTacToe(Board):
    turn = True

    def __init__(self):
        super().__init__((3, 3), ["[ ]", " O ", " X "])

    def play(self):
        print(f"{'X' if self.turn else 'O'}'s turn")
        x, y = self.get_input()
        done = self.step(x, y)
        self.show()
        
        if done:
            print(f"{'X' if not self.turn else 'O'} won!")  # TODO Error: forget not
            print("Press enter to quit")
            input(">")
            quit()
    
    # def reset(self):
    #     """Reset game"""
    #     self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    #     self.action_space = [str(i) for i in range(9)]
    #     self.X_turn = True
    #     self.show()
    
    def step(self, x, y):
        """Place a mark on the grid at coordinate and switch player turn.
        Return True if game over"""
        self.grid[y][x] = int(self.turn) + 1  # TODO Hack: Typecast bool to int
        self.turn = not self.turn             # TODO Error: forget +1
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
    
    
    
if __name__ == "__main__":
    game = TicTacToe()
    game.show()
    while True:
        game.play()

