from morpion import Morpion
from player import Player
from bot import Bot

if __name__ == '__main__':
    game = Morpion(Player("X"), Bot("O"))
    game.start()

