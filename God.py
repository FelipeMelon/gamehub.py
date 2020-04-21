import discord
import os
import random
import string


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event

async def on_message(message):

    if message.content.startswith("!poll"):
      channel = client.get_channel(701806262844653678)
      await channel.send(message.content[5:])
    if(message.channel.id == 701806262844653678):
      await message.add_reaction("✅")
      await message.add_reaction('❌')

    if message.content.startswith('!help'):
      await message.channel.send("""*Useful Commands:*\n!poll <something you want to ask>\n!count (to see how many users are on the server)\n!countbots (to see how many bots are there)\n\n*Fun commands:*\nSpamrundie\nM yoda\nFelipe\nAlcoholic""")

    elif message.content.startswith('Spamrundie'or 'spamrundie'):
       await message.channel.send('He is gay as ||fuck||')

    elif message.content.startswith('M yoda' or 'M_yoda'):
        await message.channel.send('*There can only be one god: ME!!*')

    elif message.content.startswith('Felipe'):
        await message.channel.send('Me master')

    elif message.content.startswith('Alcoholic'):
        await message.channel.send('When he is drunk instead of sweat he releases *vodka*')

    elif message.content.startswith('!ready'):
        await client.change_presence(activity=discord.Game(name=message.content[7:]))

    if message.content.startswith('!count'):
            membersInServer = message.guild.members
            # Filter to the list, returns a list of bot-members
            botsInServer = list(filter(filterOnlyBots, membersInServer))

            botsInServerCount = len(botsInServer)
            # (Total Member count - bot count) = Total user count
            usersInServerCount = message.guild.member_count - botsInServerCount


            if message.content == '!count':
              await message.channel.send(usersInServerCount)



    elif message.content.startswith('!countbots'):
        membersInServer = message.guild.members
        botsInServer = list(filter(filterOnlyBots, membersInServer))

        botsInServerCount = len(botsInServer)
        await message.channel.send(membersInServer)

    # Filter the member list to only bots
def filterOnlyBots(member):
        return member.bot





async def on_member_join(member):
    newUserMessage = 'Welcome on our server! Feel free to explore everything. ||I am a god BTW||'
    print("Recognised that a member called " + member.name + " joined")
    try:
      await message.channel.send(newUserMessage)
      print("Sent message to " + member.name)
    except:
        print("Couldn't message " + member.name)






client.run(os.environ['Disc_Token'])
