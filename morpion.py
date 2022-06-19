from random import choice

class Morpion:
    def __init__(self, p1, p2):
        p1.game = self
        p1.opponent = p2
        p2.game = self
        p2.opponent = p1
        self.p1 = p1
        self.p2 = p2
        self.turn = choice([False, True])
        self.plateau = [
            ["1","2","3"],
            ["4","5","6"],
            ["7","8","9"]
        ]

    def play(self):
        if self.turn:
            return self.p1.play()
        else:
            return self.p2.play()

    def current(self):
        if self.turn:
            return self.p1
        else:
            return self.p2

    def is_finished(self):
        plateau = self.plateau
        if plateau[0][0] == plateau[0][1] == plateau[0][2]:
            return plateau[0][0]
        elif plateau[1][0] == plateau[1][1] == plateau[1][2]:
            return plateau[1][0]
        elif plateau[2][0] == plateau[2][1] == plateau[2][2]:
            return plateau[2][0]
        elif plateau[0][0] == plateau[1][0] == plateau[2][0]:
            return plateau[0][0]
        elif plateau[0][1] == plateau[1][1] == plateau[2][1]:
            return plateau[0][1]
        elif plateau[0][2] == plateau[1][2] == plateau[2][2]:
            return plateau[0][2]
        elif plateau[0][0] == plateau[1][1] == plateau[2][2]:
            return plateau[0][0]
        elif plateau[0][2] == plateau[1][1] == plateau[2][0]:
            return plateau[0][2]
        elif all(all(self.plateau[i][j] in ("O", "X") for j in range(3)) for i in range(3)):
            return 1
        else:
            return 0

    def win(self, p):
        if p is None:
            print("égalité")
        else:
            print(p, "a gagné")

    def paint(self):
        for a in self.plateau:
            print("|".join(a))
        print()

    def start(self):
        self.paint()
        while self.is_finished() == 0:
            x, y = self.play()
            self.plateau[x][y] = self.current().sign
            self.paint()
            self.turn = not self.turn
        else:
            if self.is_finished() == 1:
                self.win(None)
            else:
                self.win(self.is_finished())