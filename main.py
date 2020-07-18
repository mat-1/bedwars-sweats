import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'Logged in as {client}')

@bot.command(name='ping')
async def ping_command(ctx):
    await ctx.send('Pong!')

with open('token.txt', 'r') as f:
	token = f.read().strip()

client.run(token)