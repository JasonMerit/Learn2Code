


class BattleShips(Board):
    
        def __init__(self, rows, cols):
            super().__init__(rows, cols)
            self.ships = [5, 4, 3, 3, 2]
            self.ships_left = len(self.ships)
            self.place_ships()
    
        def place_ships(self):
            """Place ships randomly on the grid"""
            for ship in self.ships:
                while True:
                    x, y = random.randint(0, self.cols - 1), random.randint(0, self.rows - 1)
                    direction = random.choice(['h', 'v'])
                    if self.check_ship(x, y, ship, direction):
                        self.place_ship(x, y, ship, direction)
                        break
    
        def check_ship(self, x, y, ship, direction):
            """Check if a ship can be placed at x, y with a given direction"""
            if direction == 'h':
                if x + ship > self.cols:
                    return False
                for i in range(ship):
                    if self.grid[y][x + i] != 0:
                        return False
            elif direction == 'v':
                if y + ship > self.rows:
                    return False
                for i in range(ship):
                    if self.grid[y + i][x] != 0:
                        return False
            return True
    
        def place_ship(self, x, y, ship, direction):
            """Place a ship at x, y with a given direction"""
            if direction == 'h':
                for i in range(ship):
                    self.grid[y][x + i] = ship
            elif direction == 'v':
                for i in range(ship):
                    self.grid[y + i][x] = ship
    
        def step(self, x, y):
            """Get input from user, update grid and remove action from action_space"""
            if self.grid[y][x] == 0:
                self.grid[y][x] = 3
            elif self.grid[y][x] > 1:
                self.grid[y][x] = 4
                self.ships_left -= 1
            self.action_space.remove((x, y))
    
        def check_win(self):
            """Check if there is a winner. 
            Returns -1 : Draw, 0 : No winner, 1 : O wins, 2 : X wins"""
            if not self.action_space:
                return -1



if __name__ == "__main__":
    game = BattleShips(10, 10)
    game.show()
    while True:
        x, y = game.get_input()
        game.step(x, y)
        game.show()