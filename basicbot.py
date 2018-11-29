import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands

client = Bot(description="^help", command_prefix="^", pm_help = False) 

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+'')
	print('--------')
	print('--------')
	print('Started <BackBon>') 
	return await client.change_presence(game=discord.Game(name='<Nøøb Gamer || ^help>')) 

@client.command()
async def welcome(*args):
	await client.say("☆Welcome to my first BackBon Bot☆") 

@client.command()
async def invite(*args):
	await client.say("☆ https://discord.gg/bYjScDG ☆") 
	
@client.command()
async def invitebot(*args):
	await client.say('♡ https://discordapp.com/api/oauth2/authorize?client_id=516927859063914497&permissions=8&redirect_uri=https%3A%2F%2Fdiscordapp.com%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3D516927859063914497%26permissions%3D8%26scope%3Dbot&scope=bot ♡')
	
@client.command()
async def helppy(*args):
    await client.say('▪We Will Contact  @Nøøb Gamer#3762 Sum More Information For This Bot.▪ ')
    
    
  
client.run('NTE2OTI3ODU5MDYzOTE0NDk3.DuACwQ.xd0jh10J6NNJFo56OHVlfSxEni0') 