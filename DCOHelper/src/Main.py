import discord

import rollers.DisadvantageRoller
import rollers.AdvantageRoller

from DCOHelper.src.rollers.AdvantageRoller import AdvantageRoller
from DCOHelper.src.rollers.DisadvantageRoller import DisadvantageRoller

client = discord.Client()

TokenFileName = "Token.txt"
Token = (open(TokenFileName,"r").read())
boonRoller = AdvantageRoller()
bustRoller = DisadvantageRoller()
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

    if '$hello' in message.content:
        await message.channel.send('Hello!')
    if "$bacon" in message.content:
        await message.channel.send("Heck yeah I want some bacon!")
    if "$boon" in message.content:
        await message.channel.send(boonRoller.RollDice(1))
    if "$bust" in message.content:
        await message.channel.send(bustRoller.RollDice(2))
    if "$help" in message.content:
        await message.channel.send(helpMessage)


client.run(Token)
if __name__ == "__main__":
    AdvantageRoller.run(main)
    DisadvantageRoller.run(main)