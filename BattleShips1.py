from TicTacToe import Board
import random


class BattleShips():
    def __init__(self, rows, cols):
        # 0: Empty, 1: Ship, 2: Hit, 3: Splash
        self.rows, self.cols = rows, cols
        self.player = Board(rows, cols, {0: '[ ]', 1: '[B]', 2: ' X ', 3 : '   '}, label="==== PLAYER BOARD ==== ")  # Player shoots player
        self.computer = Board(rows, cols, {0: '[ ]', 1: '[ ]', 2: ' X ', 3 : '   '}, label = "==== COMPUTER BOARD ==== " )

        self.player.ship_count = self.computer.ship_count = 10
        self.player.name = "PLAYER"
        self.computer.name = "COMPUTER"
    
    def get_input(self):
        return self.player.get_input()

    def play(self):
        self.place_ships()
        self.player.show()
        self.computer.show()

        while True:
            self.step()
        
    def place_ships(self):
        """Place ships on grid randomly"""
        for board in [self.player, self.computer]:
            spots = board.sample(board.ship_count)
            for x, y in spots:
                board.grid[y][x] = 1
        
    def step(self):
        """Player shoots by input, and computer shoots randomly"""
        # Player shoots
        hit = True
        while hit:
            x, y = self.computer.get_input()
            # print("PLAYER SHOOTS AT ", x, y)
            hit = self.shoot(x, y, self.computer)
            if hit:
                self.computer.show()
                print("HIT!")

        # Computer shoots
        hit = True
        while hit:
            x, y = self.player.sample()[0]
            # print("COMPUTER SHOOTS AT ", x, y)
            hit = self.shoot(x, y, self.player)

        self.player.show()
        self.computer.show()
    
    def shoot(self, x, y, board: Board):
        """Return True if ship is hit, False if splash"""
        board.action_space.remove((x, y))
        if board.grid[y][x] == 1:
            board.grid[y][x] = 2
            board.ship_count -= 1
            if board.ship_count == 0:
                board.show()
                print(f"{board.name} LOOSES!")
                quit()
            return True
        else:
            board.grid[y][x] = 3
            return False
        
    def random(self):
        """Randomly choose an action from action_space and step"""
        # Player shoots
        hit = True
        while hit:
            x, y = self.computer.sample()[0]
            print("PLAYER SHOT AT ", x, y)
            hit = self.shoot(x, y, self.computer)

        # Computer shoots
        hit = True
        while hit:
            x, y = self.player.sample()[0]
            print("COMPUTER SHOT AT ", x, y)
            hit = self.shoot(x, y, self.player)

        self.player.show()
        self.computer.show()


if __name__ == "__main__":
    game = BattleShips(10, 10)  
    game.play()


    # game.place_ships()
    # while True:
    #     # input("> ")
    #     game.random()