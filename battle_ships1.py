from tic_tac_toe import Board
import random 

class BattleShips(Board):
    def __init__(self):
        super().__init__((10, 10), ["[ ]", "[B]", " O ", " X "])  # 0 = empty, 1 = boat, 2 = splash, 3 = hit
        # self.boats = [5, 4, 3, 3, 2]
        
        self.show()
    
    def play(self):
        self.place_boats()  # 1st phase

        x, y = self.get_input()
        
        done = self.step(x, y)
        self.show()
        
        if done:
            print(f"{'X' if not self.turn else 'O'} won!")  # TODO Error: forget not
            print("Press enter to quit")
            input(">")
    
    def place_boats(self):
        """Place boats on the grid"""
        for _ in range(10):
            action = random.choice(self.action_space)
            y, x = int(action) % 10, int(action) // 10
            self.grid[y][x] = 1
    
    def step(self, x, y):
        """Shoot at coordinate and switch player turn.
        Return True if game over"""
        if self.grid[y][x] == 1:
            self.grid[y][x] = 3  # HIT!
        else:
            self.grid[y][x] = 2  # SPLASH!
        self.action_space.remove(y * self.height + x)  # TODO Error: forget to generalize height
        self.turn = not self.turn
        return self.game_over()

    def game_over(self):
        """Return True if game over"""
        # Check if all boats are hit
        for row in self.grid:
            if 1 in row:
                return False
        return True

if __name__ == "__main__":
    game = BattleShips()
    # while True:
    #     game.play()