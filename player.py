class Player:
    def __init__(self, sign):
        self.sign = sign
        self.game = None
        self.opponent = None

    def play(self):
        while True:
            try:
                x = int(input(""))-1
            except:
                continue
            if 0 <= x <= 8 and self.game.plateau[x//3][x%3] not in (self.game.p1.sign, self.game.p2.sign):
                return x//3, x%3
            else:
                print("case déjà remplie")
        
