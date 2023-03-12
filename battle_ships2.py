from tic_tac_toe import Board
import random 

class BattleShips():
    steps = 0
    def __init__(self, ship_count=1):
        self.player = Board((10, 10), ["[ ]", "[B]", " O ", " X "], [0, 1], "===== Player board ====")  # empty, boat, splash, hit
        self.computer = Board((10, 10), ["[ ]", "[B]", " O ", " X "], [0, 1], "===== Computer board ====")  # empty, boat, splash, hit
        self.ship_count = ship_count
        self.player_ships = ship_count
        self.computer_ships = ship_count
        
        # self.boats = [5, 4, 3, 3, 2]
        
        # self.player.show()
        self.place_boats()  # 1st phase
    
    def play(self):
        """Play game"""
        self.steps += 1
        print("===== Step", self.steps, "=====")
        done = self.step()
        
        if done:
            print("Press enter to quit")
            input(">")
            quit()
    
    def place_boats(self):
        """Place boats on the grid. Player shoots in player, so layout is on computer grid"""
        for board in [self.player, self.computer]:
            for _ in range(self.ship_count):
                action = random.choice(board.action_space)
                board.action_space.remove(action)
                y, x = int(action) % 10, int(action) // 10
                board.grid[y][x] = 1
            board.action_space = list(range(board.width*board.height))
            # board.show()
    
    def step(self):
        """Shoot at coordinate x, y and computer step.
        Return True if game over"""
        # Player step
        hit = True
        while hit:
            self.player.show()
            x, y = self.player.get_input()
            hit = self.shoot(self.player, x, y)

            if hit:
                self.computer_ships -= 1
                if self.computer_ships == 0:
                    print("You won!")
                    return True
        
        # Computer step
        hit = True
        while hit:
            action = random.choice(self.computer.action_space)
            x, y = int(action) % 10, int(action) // 10
            print(f'Computer action: ({x}, {y})')
            hit = self.shoot(self.computer, x, y)
            
            if hit:     # Check for game over
                self.player_ships -= 1
                if self.player_ships == 0:
                    print("Computer won!")
                    return True
                
        self.computer.show()

    def shoot(self, board: Board, x, y):
        """Shoot at coordinate x, y and return True if hit"""
        board.action_space.remove(y * self.player.height + x)  # TODO Error: forget to generalize height
        if board.grid[y][x] == 1:  # HIT!
            print("Hit!")
            board.grid[y][x] = 3
            return True
        else:                         # SPLASH!
            print("Splash!")
            board.grid[y][x] = 2
            return False

    def random_step(self):
        """Random step and return True if game over"""
        self.steps += 1

        for board in [self.player, self.computer]:
            hit = True
            while hit:
                action = random.choice(board.action_space)
                x, y = int(action) % 10, int(action) // 10
                print(f'Action: ({x}, {y})')
                hit = self.shoot(board, x, y)
            board.show()

        game_over = self.game_over(board)
        if game_over:
            print("game_over!")
            return True

if __name__ == "__main__":
    game = BattleShips()
    
    while True:
        game.play()