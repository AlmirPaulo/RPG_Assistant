# Software: RPG Diceroller
# Description: A Discord bot that simulate RPG dice rolls. 
# Info Page: https://github.com/AlmirPaulo/Diceroller_discord

# Author: Almir Paulo
# Github: https://github.com/AlmirPaulo/
# Website: https://almirpaulo.github.io/
# Email: ap.freelas@gmail.com

import discord, random, os

# Variables
token = open('note_token', 'r').read()
client = discord.Client()

# Default - Recognize user messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return

# Diceroller
    if message.content[0] == '!':
        dices = message.content[1]
        while int(dices) > 0: 

            if message.content[2:5] == 'd3':
                await message.channel.send(f"Your d3 rolled a {random.randint(1,3)}")

            elif message.content[2:5] == 'd4':
                await message.channel.send(f"Your d4 rolled a {random.randint(1,4)}")
        
            elif message.content[2:5] == 'd6':
                await message.channel.send(f"Your d6 rolled a {random.randint(1,6)}")

            elif message.content[2:5] == 'd8':
                await message.channel.send(f"Your d8 rolled a {random.randint(1,8)}")

            elif message.content[2:5]== 'd%':
                await message.channel.send(f"Your d% rolled a {random.randint(1,100)}%")
            
            elif message.content[2:5] == 'd10':
                await message.channel.send(f"Your d10 rolled a {random.randint(1,10)}")

            elif message.content[2:5] == 'd12':
                await message.channel.send(f"Your d12 rolled a {random.randint(1,12)}")

            elif message.content[2:5] == 'd20':
                await message.channel.send(f"Your d20 rolled a {random.randint(1,20)}")

            
            dices = int(dices) -1

# Run bot
client.run(token.strip())