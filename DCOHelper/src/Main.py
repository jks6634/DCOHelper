import discord

import AdvantageRoller
import DisadvantageRoller

client = discord.Client()

TokenFileName = "Token.txt"
Token = (open(TokenFileName, "r").read())
boonRoller = AdvantageRoller.AdvantageRollerObj()
bustRoller = DisadvantageRoller.DisadvantageRollerObj()
helpMessage = "The available commands are: \n" \
              "$hello\n" \
              "$boon: to roll an advantage die\n" \
              "$bust: to roll a disadvantage die"


def main():
    pass


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    commands = message.content.split("$")

    for command in commands:
        if 'hello' in command:
            await message.channel.send('Hello!')
        if "bacon" in command:
            await message.channel.send("Heck yeah I want some bacon!")
        if "boon" in command:
            numDice = getNumDice(command, 4)
            await message.channel.send(boonRoller.RollDice(numberOfDice=numDice))
        if "bust" in command:
            numDice = getNumDice(command, 4)
            await message.channel.send(bustRoller.RollDice(numberOfDice=numDice))
        if "help" in command:
            await message.channel.send(helpMessage)


def getNumDice(string, commandLength):
    number = 1
    character = ""

    if len(string) > commandLength:
        # this index will be the character after the command
        character = string[commandLength]
        if(RepresentsInt(character)):
            number = int(character)

    return number

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


client.run(Token)
if __name__ == "__main__":
    AdvantageRoller.run(main)
    DisadvantageRoller.run(main)
