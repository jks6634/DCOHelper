import numpy as np

class RollDie():
    def Roll(diceSize=1, numberOfHits=0):
        roll = np.random_integers(1, diceSize)
        if roll <= numberOfHits:
            return True
        return False
