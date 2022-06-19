from copy import deepcopy
from random import uniform, choice


class Bot:
    def __init__(self, sign):
        self.sign = sign
        self.game = None
        self.opponent = None

    def play(self):
        best_moves, best_score = [], -float("inf")
        for a in self.free(self.game.plateau):  # on essaye toutes les actions possibles
            plot = deepcopy(self.game.plateau)
            plot[a[0]][a[1]] = self.sign
            score = self.point(plot, False)
            if score > best_score:
                best_moves, best_score = [a], score
            elif score == best_score and uniform(0, 1) < 1:
                best_moves.append(a)
                best_score = score
        result = choice(best_moves)  # on selectionne une action au hasard parmi les meilleures actions
        return result[0], result[1]

    def free(self,t):
        r = []
        for a in range(len(t)):
            for b in range(len(t[a])):
                if t[a][b] != self.game.p1.sign and t[a][b] != self.game.p2.sign:
                    r.append([a,b])
        return r

    def point(self, plot, turn, max_depth=6):  # fonction pour noter une partie
        if max_depth <= 0: return 0
        win = self.win(plot)
        if win != 0:  # si la partie est terminée on retourne le score correspondant
            if win == 1:
                return 0
            elif win == self.sign:
                return 2**len(self.free(plot))
            else:
                return -2**len(self.free(plot))
        else:  # sinon on retourne la somme des scores correspondant à toutes les actions possibles
            r = 0
            for a in self.free(plot):
                p = deepcopy(plot)
                p[a[0]][a[1]] = (self.sign if turn else self.opponent.sign)
                r += self.point(p, not turn, max_depth-1)
            return r

    def win(self, plateau):
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
        elif all(all(self.game.plateau[i][j] in ("O", "X") for j in range(3)) for i in range(3)):
            return 1
        else:
            return 0