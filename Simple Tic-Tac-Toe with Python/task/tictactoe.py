class TicTacToe_Game():
    def __init__(self, ):
        self.game = ["_" for _ in range(9)]
        self.all_rows = []
        self.symbols_count = {"X": 0, "O": 0, "_": 0}
        self.active_player = "X"

    def count_symbols(self):
        # reset count
        for key in self.symbols_count:
            self.symbols_count[key] = 0
        # count symbols
        for symbol in self.game:
            self.symbols_count[symbol] += 1

    def draw_grid(self):
        grid = ""
        for i in range(0, 9, 3):
            grid += f"\n| {" ".join(self.game[i:i + 3])} |"
        print("---------", grid, "\n---------", sep=None)

    def get_all_rows(self):
        self.all_rows = []
        g = self.game
        for i in range(0, 9, 3):
            self.all_rows.append(g[i:i + 3])
        for i in range(3):
            self.all_rows.append([g[i], g[i + 3], g[i + 6]])
        self.all_rows.append([g[0], g[4], g[8]])
        self.all_rows.append([g[2], g[4], g[6]])

    def get_game_state(self):
        self.count_symbols()
        self.get_all_rows()
        if (["X", "X", "X"] in self.all_rows and ["O", "O", "O"] in self.all_rows or
                abs(self.symbols_count["X"] - self.symbols_count["O"]) >= 2):
            return "Impossible"
        elif ["X", "X", "X"] in self.all_rows:
            return "X wins"
        elif ["O", "O", "O"] in self.all_rows:
            return "O wins"
        elif self.symbols_count["_"] > 0:
            return "Game not finished"
        else:
            return "Draw"

    def make_a_move(self):
        while True:
            # c = coordinates
            c = input().strip().split()
            if len(c) != 2:
                print("Coordinates should be from 1 to 3!")
            elif not (c[0].isdigit() or c[1].isdigit()):
                print("You should enter numbers!")
            elif int(c[0]) < 1 or int(c[0]) > 3 or int(c[1]) < 1 or int(c[1]) > 3:
                print("Coordinates should be from 1 to 3!")
            elif self.game[(int(c[0]) - 1) * 3 + int(c[1]) - 1] != "_":
                print("This cell is occupied! Choose another one!")
            else:
                self.game[(int(c[0]) - 1) * 3 + int(c[1]) - 1] = self.active_player
                self.draw_grid()
                # switch player
                if self.active_player == "X":
                    self.active_player = "O"
                else:
                    self.active_player = "X"
                break

    def start(self):
        self.draw_grid()
        while True:
            self.make_a_move()
            state = self.get_game_state()
            if state != "Game not finished":
                break
        print(state)


if __name__ == "__main__":
    game = TicTacToe_Game()
    game.start()
