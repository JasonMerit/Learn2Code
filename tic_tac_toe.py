# Kryds og bolle
import random

class Game():

    def __init__(self, size, cell_strings):
        self.size = size
        self.cell_strings = cell_strings

        self.width, self.height = size
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.letters = [chr(i) for i in range(65, 65 + self.width)]
        self.numbers = [str(i) for i in range(self.height)]
        self.letter_coords = "   " + "  ".join(self.letters)
        self.action_space = list(range(self.width*self.height))
        self.turn = True

        self.show()
    
    def show(self):
        print(self.letter_coords)
        for i, b in enumerate(self.grid):
            row = f"{i} "
            for v in b:
                row += self.cell_strings[v]
            print(row)
        print()
    
    def get_input(self):
        """Input from user (>1) or quit"""
        print(f"{'X' if self.turn else 'O'}'s turn")
        
        while True:
            user = input(">")
            if user in ["q", "quit", "exit"]:
                quit()
            if len(user) > 1:
                return user
    
    def random_step(self):
        """Step in random action. Return True if game over"""
        action = random.choice(self.action_space)
        x, y = int(action) % self.width, int(action) // self.height  # TODO: Forget to generalize width and height
        print(f'Random step: ({x}, {y})')
        return self.step(x, y)

    def step(self):
        """Step in action. Return True if game over"""
        raise NotImplementedError


class TicTacToe(Game):

    def __init__(self):
        super().__init__((3, 3), ["[ ]", " O ", " X "])

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
            print(f"{'X' if not self.turn else 'O'} won!")  # TODO Error: forget not
            print("Press enter to quit")
            input(">")
            # self.reset()
    
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
        self.turn = not self.turn           # TODO Error: forget +1
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
    while True:
        game.play()

