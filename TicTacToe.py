
import random

class Board():

    def __init__(self, width, height, cell2str, label=''):
        self.label = label
        self.cell2str = cell2str

        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.number_coords = [str(x) for x in range(height)]
        self.letter_coords = [chr(x + 65) for x in range(width)]

        self.letters = '   ' + '  '.join(self.letter_coords)
        self.X_turn = True

        self.action_space = [(x, y) for x in range(width) for y in range(height)]


    def show(self):
        print(self.label)
        print(self.letters)
        for i, row in enumerate(self.grid):
            txt = f'{i} '
            for cell in row:
                txt += self.cell2str[cell]
            print(txt)

    def step(self, x, y):
        """Change grid value at <xy> and removes <xy> from action_space"""        
        self.grid[y][x] = int(self.X_turn) + 1
        self.X_turn = not self.X_turn
        self.action_space.remove((x, y))

    def get_input(self):
        """Get user input and return"""

        while True:
            print("Type action <xy>")
            user = input('>').upper()

            if user in ['QUIT', 'Q', 'FUK OFF']:
                quit()

            if len(user) != 2:
                continue 
            x, y = user   # x = 'A'

            if x not in self.letter_coords or y not in self.number_coords:
                continue

            x, y = int(ord(x) - 65), int(y)
            if (x, y) in self.action_space:
                return x, y

    def random_step(self):
        x, y = random.choice(self.action_space)
        self.step(x, y)


class TicTacToe(Board):

    def __init__(self):
        cell2str = {0 : '[ ]', 1 : ' X ', 2 : ' O '}
        super().__init__(3, 3, cell2str)

    def check_win(self):
        """Determine if game over"""
        for i in range(3):
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != 0:
                return self.grid[0][i]
        
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != 0:
                return self.grid[i][0]
        
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != 0:
            return self.grid[1][1]
        
        if self.grid[2][0] == self.grid[1][1] == self.grid[0][2] != 0:
            return self.grid[1][1]

        if self.action_space == []:
            print("DRAW")
            quit()

        return 0



if __name__ == '__main__':
    game = TicTacToe()
    # game.random_step()
    # quit()
    game.show()
    while True:
        # x, y = game.get_input()
        # game.step(x, y)
        game.random_step()
        game.show()
        if game.check_win():
            print("GAME OVER")
            quit()
