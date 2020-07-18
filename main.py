import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'Logged in as {client}')

@bot.command(name='list')
async def list_command(ctx, arg):
    pass

with open('token.txt', 'r') as f:
	token = f.read().strip()

client.run(token)