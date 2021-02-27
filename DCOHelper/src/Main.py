import discord
from DCOHelper.src.AdvantageRoller import AdvantageRoller
from DCOHelper.src.DisadvantageRoller import DisadvantageRoller

client = discord.Client()

TokenFileName = "Token.txt"
Token = (open(TokenFileName,"r").read())
boonRoller = AdvantageRoller()
bustRoller = DisadvantageRoller()

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


client.run(Token)