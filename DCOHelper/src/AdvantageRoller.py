import RollDie

Die = RollDie.RollDice()
diceSize = 8
numberOfBoons = 4
maxNumberOfDice = 4


class AdvantageRollerObj:
    def RollDice(self, numberOfDice=1):
        numDice = numberOfDice
        numBoonsRolled = 0

        if numDice > maxNumberOfDice:
            numDice = 4

        for i in range(numDice):
            if (Die.Roll(diceSize, numberOfBoons)):
                numBoonsRolled = numBoonsRolled + 1

        return ("Rolled " + str(numDice) + ", and got " + str(numBoonsRolled) + " boons")
