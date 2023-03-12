from TicTacToe import Board
import random


class BattleShips():
    def __init__(self, rows, cols):
        # 0: Empty, 1: Ship, 2: Hit, 3: Splash
        self.rows, self.cols = rows, cols
        self.player = Board(rows, cols, {0: '[ ]', 1: '[B]', 2: ' X ', 3 : '   '}, label="==== PLAYER BOARD ==== ")  # Player shoots player
        self.computer = Board(rows, cols, {0: '[ ]', 1: '[ ]', 2: ' X ', 3 : '   '}, label = "==== COMPUTER BOARD ==== " )

        self.player.name = "PLAYER"
        self.computer.name = "COMPUTER"
        self.ships = [5, 4, 3, 3, 2]
        self.player.ship_count = self.computer.ship_count = sum(self.ships)
    
    def play(self):
        self.place_ships()
        self.player.show()
        self.computer.show()

        while True:
            self.step()
        
    def place_ships(self):
        """Place ships on grid randomly"""
        for board in [self.player, self.computer]:
            for ship in self.ships:
                while True:
                    x0, y0 = random.randrange(self.cols), random.randrange(self.rows)
                    direction = random.choice(['h', 'v'])
                    if self.check_ship(board, x0, y0, ship, direction):
                        self.place_ship(board, x0, y0, ship, direction)
                        break                    

    def check_ship(self, board: Board, x0, y0, ship, direction):
        """Check if a ship can be placed at x0, y0 with a given direction and ship size"""
        if direction == 'h':
            if x0 + ship > self.cols:
                return False
            for i in range(ship):
                if board.grid[y0][x0 + i] != 0:
                    return False
                
        elif direction == 'v':
            if y0 + ship > self.rows:
                return False
            for i in range(ship):
                if board.grid[y0 + i][x0] != 0:
                    return False
        return True

    def place_ship(self, board: Board, x0, y0, ship, direction):
        """Place a ship at x0, y0 with a given direction"""
        if direction == 'h':
            for i in range(ship):
                board.grid[y0][x0 + i] = 1

        elif direction == 'v':
            for i in range(ship):
                board.grid[y0 + i][x0] = 1
        
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
    # game.play()

    game.place_ships()
    game.player.show()
    game.computer.show()
    while True:
        # input("> ")
        game.random()