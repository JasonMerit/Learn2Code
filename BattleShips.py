import random
from TicTacToe import Board

class BattleShips():
    
    def __init__(self, ship_count):
        cell2str = {0 : '[ ]', 1 : '[B]', 2 : ' X ', 3 : ' + '}
        self.player = Board(5, 4, cell2str, label="=== PLAYER ===")
        self.computer = Board(5, 4, cell2str, label="=== COMPUTER ===")

        self.player.ship_count = self.computer.ship_count = ship_count

        self.place_ships()
        self.player.show()
        self.computer.show()

    
    def play(self):
        i = 0
        while True:
            print(f"======| STEP {i} |=======")
            self.step()
            self.player.show()
            self.computer.show()
            i += 1
    
    def auto_play(self):
        i = 0
        while True:
            print(f"======| STEP {i} |=======")
            self.auto_step()
            self.player.show()
            self.computer.show()
            i += 1

    
    def step(self):
        """Player shoot, then computer shoots"""

        # Player
        hit = True
        while hit:
            x, y = self.computer.get_input()
            hit = self.shoot(self.computer, x, y)
            if hit:
                self.computer.show()
                if self.computer.ship_count == 0:
                    print("GAMEOVER")
                    quit()

        # Computer
        hit = True
        while hit:
            hit = self.random_shoot(self.player)
            if self.player.ship_count == 0:
                print("GAMEOVER")
                quit()
    
    def auto_step(self):
        for board in [self.player, self.computer]:
            hit = True
            while hit:
                hit = self.random_shoot(board)
                if board.ship_count == 0:
                    print("GAMEOVER")
                    quit()

    def place_ships(self):
        """Randomly place 1x1 ships"""
        for board in [self.player, self.computer]:
            ships = random.sample(board.action_space, self.player.ship_count)

            for x, y in ships:
                board.grid[y][x] = 1

    def shoot(self, board: Board, x, y):
        """
        Board board shot at x, y.
        If hit, return True
        """
        board.action_space.remove((x, y))
        print(board.label, " WAS SHOT AT ", x, y)
        if board.grid[y][x] == 1:
            board.grid[y][x] = 2
            board.ship_count -= 1
            return True
        else:
            board.grid[y][x] = 3
            return False
    
    def random_shoot(self, board: Board):
        try:
            x, y = random.choice(board.action_space) 
        except IndexError:
            print(board.action_space)
            quit()
        return self.shoot(board, x, y)




if __name__ == '__main__':
    game = BattleShips(10)
    # game.play()
    game.auto_play()