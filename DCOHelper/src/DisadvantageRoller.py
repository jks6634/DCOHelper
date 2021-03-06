import RollDie

Die = RollDie.RollDice()
diceSize = 10
numberOfDuds = 6
maxNumberOfDice = 4


class DisadvantageRollerObj:
    def RollDice(self, numberOfDice = 1):
        numDice = numberOfDice
        numDudsRolled = 0

        if numDice > maxNumberOfDice:
            numDice = 4

        for i in range(numDice):
            if(Die.Roll(diceSize, numberOfDuds)):
                numDudsRolled = numDudsRolled + 1

        return ("Rolled " + str(numDice) + ", and got " + str(numDudsRolled) + " busts")