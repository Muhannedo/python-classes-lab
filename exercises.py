class Game:
    def __init__(
        self,
        turn="X",
        tie=False,
        winner=None,
        board={
            "a1": None,
            "b1": None,
            "c1": None,
            "a2": None,
            "b2": None,
            "c2": None,
            "a3": None,
            "b3": None,
            "c3": None,
        },
    ):
        self.turn = turn
        self.tie = tie
        self.winner = winner
        self.board = board


class Play_game(Game):
    print("Welcome to Tic Tac Toe!")
