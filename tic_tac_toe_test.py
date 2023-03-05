from tic_tac_toe import Game




if __name__ == "__main__":
    game = Game()
    while not game.random_step():
        game.show()
    game.show()