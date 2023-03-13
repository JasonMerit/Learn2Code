
import random



class Board:
    def __init__(self, rows, cols, cell2str, label=""):
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.cell2str = cell2str
        self.action_space = [(x, y) for x in range(cols) for y in range(rows)]
        self.X_turn = True

        self.letter_coords = [chr(i) for i in range(65, 65 + cols)]
        self.number_coords = [str(i) for i in range(rows)]
        self.label = label


    def show(self):
        print(self.label)
        print('   ' + '  '.join(self.letter_coords))
        for i, row in enumerate(self.grid):
            txt = f'{i} '
            for cell in row:
                txt += self.cell2str[cell]
            print(txt)


    def get_input(self):
        """Get input from user and return it as grid coordinates"""
        while True:
            print("Type input <xy>")
            user = input("> ").upper()
            if user in ['Q', 'QUIT', 'EXIT', 'BYE']:
                quit()
            
            if len(user) != 2:
                continue
            x, y = user
            if x not in self.letter_coords or y not in self.number_coords:
                continue
            x, y = int(ord(user[0])) - 65, int(user[1])
            
            if (x, y) in self.action_space:
                return x, y
    
    def sample(self, n=1):
        """Return list of n actions from action_space"""
        return random.sample(self.action_space, n)


class TicTacToe(Board):

    def __init__(self, rows, cols):
        super().__init__(rows, cols, {-1: 'DRAW', 0: '[ ]', 1: ' O ', 2: ' X '})

    def play(self):
        """Play the game"""
        self.show()
        while True:
            x, y = self.get_input()
            self.step(x, y)
            # self.random_step()
            self.show()
            if k := self.check_win():
                print(f'{self.cell2str[k]} wins!')
                break

    def step(self, x, y):
        """Get input from user, update grid and remove action from action_space"""
        self.grid[y][x] = int(self.X_turn) + 1
        self.action_space.remove((x, y))
        self.X_turn = not self.X_turn

    def check_win(self):
        """Check if there is a winner. 
        Returns -1 : Draw, 0 : No winner, 1 : O wins, 2 : X wins"""

        if not self.action_space:
            return -1

        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != 0:
                return self.grid[i][0]  # Column
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != 0:
                return self.grid[0][i]  # Row
            
        # Diagonals
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != 0:
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != 0:
            return self.grid[0][2]
        
        return 0  # No winner

    def random_step(self):
        """Randomly choose an action from action_space and step"""
        x, y = random.choice(self.action_space)
        self.step(x, y)
    
    


if __name__ == '__main__':
    game = TicTacToe(3, 3)
    game.play()