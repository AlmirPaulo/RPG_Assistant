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

     # Help message
     if message.content.startswith('!help'): 
      await message.channel.send('Take a look here: https://almirpaulo.github.io/Diceroller_discord/')

# Diceroller
    if message.content[0] == '!':
        dices = message.content[1]
        results = []
        while int(dices) > 0: 

            if message.content[2:5] == 'd3':
                results.append(random.randint(1,3))

            elif message.content[2:5] == 'd4':
                results.append(random.randint(1,4))
        
            elif message.content[2:5] == 'd6':
                results.append(random.randint(1,6))
            elif message.content[2:5] == 'd8':
                results.append(random.randint(1,8))

            elif message.content[2:5]== 'd%':
                results.append(random.randint(1,100))
            
            elif message.content[2:5] == 'd10':
                results.append(random.randint(1,10))

            elif message.content[2:5] == 'd12':
                results.append(random.randint(1,12))

            elif message.content[2:5] == 'd20':
                results.append(random.randint(1,20))

            
            dices = int(dices) -1
        
        roll = []
        for i in results:
            roll.append(str(i))
            
        if message.content[2:5]== 'd%':
            out = f"you rolled: {'%, '.join(roll)}%."
        else:
            out = f"you rolled: {', '.join(roll)}."
        await message.channel.send(out)
        



# Run bot
client.run(token.strip())