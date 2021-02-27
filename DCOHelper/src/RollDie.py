from numpy import random

class RollDice():
    def Roll(self, diceSize=1, numberOfHits=0):
        roll = random.random_integers(1, diceSize)
        if roll <= numberOfHits:
            return True
        return False
