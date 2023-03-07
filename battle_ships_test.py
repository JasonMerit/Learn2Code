from battle_ships import BattleShips


if __name__ == "__main__":
    game = BattleShips()
    done = False
    while not done:
        done = game.random_step()