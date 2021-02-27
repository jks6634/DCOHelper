from DCOHelper.src.rollers.RollDie import RollDie

Die = RollDie()
diceSize = 8
numberOfBoons = 4
maxNumberOfDice = 4


class AdvantageRoller:
    def RollDice(numberOfDice=1):
        numDice = numberOfDice
        numBoonsRolled = 0

        if numDice > maxNumberOfDice:
            numDice = 4

        for i in range(numDice):
            if (Die.Roll(diceSize, numberOfBoons)):
                numBoonsRolled = numBoonsRolled + 1

        return ("Rolled " + str(numDice) + ", and got " + str(numBoonsRolled) + " boons")
