import discord
import random
import time
import asyncio
from discord.ext import commands
from Bobo import BoethiusToken
from Bobo import quotes

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('&hello'):
        await message.channel.send('Hello!')
    
    if message.content.lower().startswith('&joke'):
        await message.channel.send("Sorry I'm not very funny at the moment if I'm being honest. Open to requests though")
    
    if message.content.lower().startswith('&hewwo'):
        await message.channel.send('OwO')
        
    if message.content.lower().startswith('&shush'):
        await message.channel.send("<a:okbottom:683091370327670813>")
        
    # if message.content.startswith('&shush') or message.content.startswith('&Shush'):
    #     await message.channel.send("<a:okbottom:683091370327670813>")
        
    if "minecraft" in message.content.lower():
        await message.add_reaction("<a:pikaMine:653443963608629249>")
        
    if message.content.lower().startswith("&rps"):
        
        await message.channel.send("Do you want to play rock paper scissors? [!y , !n]")
        
        def play_request(m):
            return m.author == message.author and m.content == "!y" or m.content == "!n"
        
        try:
            response = await client.wait_for('message', check=play_request, timeout = 20.0)
            
        except asyncio.TimeoutError:
            await message.channel.send('shame')

        response = response.content
        
        if response == "!y":
            
            stopper = 1
            while stopper == 1:
                
                await message.channel.send("rock, paper, or scissors? Type 'quit' to quit")
        
                def play_time(m):
                    return m.author == message.author
        
                try:
                    userRPS = await client.wait_for('message', check=play_time, timeout = 20.0)
                
                except asyncio.TimeoutError:
                    await message.channel.send('shame')
                
                userRPS = userRPS.content
                print(userRPS)
                
                options = ['rock', 'paper', 'scissors']
                cpuRPS = random.choice(options)
    
                if userRPS == cpuRPS:
                    await message.channel.send("Tie Game")
                    
                elif userRPS.lower() == 'quit':
                    await message.channel.send("Okie doke")
                    stopper = 0
                    
                elif userRPS in options and userRPS != cpuRPS:
                    await message.channel.send("Computer chose " +cpuRPS+".")
                
                else:
                    await message.channel.send("Input valid term next time.")
                time.sleep(1.5)
        else:
            await message.channel.send("smh my head")

    if message.content.lower().startswith('&quote'):
        inspiration = random.choice(quotes)
        print(inspiration)
        await message.channel.send(inspiration +"\n"  "-Me")
    
    if message.content.lower().startswith('&dice'):
        await message.channel.send("How many dice? (max: 15)")

        def dice_num_request(m):
            return m.author == message.author

        try:
            response1 = await client.wait_for('message', check=dice_num_request, timeout = 20.0)

        except asyncio.TimeoutError:
            await message.channel.send('shame')
        
        response1 = int(response1.content)
        await message.channel.send("How many sides?")

        def dice_request(m):
            return m.author == message.author

        try:
            response2 = await client.wait_for('message', check=dice_request, timeout = 20.0)

        except asyncio.TimeoutError:
            await message.channel.send('shame')
        response2 = int(response2.content)

        if response2 > 0 and 0 < response1 <= 15:
            diceT = 0
            for x in range(response1):
                dice1 = random.randrange(1, response2)
                await message.channel.send("Dice # "+str(x+1)+": "+str(dice1))
                print("Dice # "+str(x+1)+": "+str(dice1))
                diceT += dice1 
            await message.channel.send("Total: "+str(diceT))
            print("Total: "+str(diceT))
        else:
            await message.channel.send("Not a valid number of sides or too many dice")
    
    if message.content.lower().startswith('&coin'):
        coinS = ["Heads", "Tails"]
        flip = random.choice(coinS)
        await message.channel.send(flip)
    if message.content.lower().startswith('&help'):
        await message.channel.send("&rps : plays rock paper scissors\n"
                                  +"&coin : flips a coin\n"
                                  +"&dice : rolls chosen number of dice with chosen number of sides\n"
                                  +"&hewwo : does something stupid\n"
                                  +"&shush : does something else stupid\n")
            
client.run(BoethiusToken)