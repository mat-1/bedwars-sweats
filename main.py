import json
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

# sets config to the contents of config.json
with open('config.json', 'r') as f:
	config = json.loads(f.read())

@bot.event
async def on_ready():
    print(f'Logged in as {bot}')


@bot.command(name='lfg')
async def lfg_command(ctx, game):
	'Looks for voice channels that the user can join, and moves them to it'

	# The user must be in the waiting room channel, otherwise give them an error and stop
	if not ctx.author.voice or ctx.author.voice.channel.id != config['waiting']:
		await ctx.send('You must be in the waiting room to use this command.')
		return


	# Makes the game case insensitive
	game = game.lower()

	# If the game the user chose doesn't exist, tell them the list of possible games, and stop
	if game not in config['lfg']:
		lfg_games_list = list(config['lfg'])
		await ctx.send(f'Invalid game. Possible LFG games: {lfg_modes_list}')
		return

	# lfg_channels is a list of channel ids that the user will be moved to
	lfg_channels = config['lfg'][game]

	# Searches for the channel with the highest amount of people (but not full)
	lfg_fullest_channel = None
	lfg_fullest_channel_members = -1
	for lfg_channel_id in lfg_channels:
		lfg_channel = bot.get_channel(lfg_channel_id)

		lfg_channel_members = len(lfg_channel.members)
		lfg_channel_max_members = lfg_channel.user_limit or 2

		if lfg_channel_members >= lfg_channel_max_members:
			# Channel is full, skip it
			continue

		# This channel is more full than the previous known fullest channel, so replace it with this one
		if lfg_channel_members > lfg_fullest_channel_members:
			lfg_fullest_channel = lfg_channel
			lfg_fullest_channel_members = lfg_channel_members

	# If no available channel was found, send an error to the user and stop
	if lfg_fullest_channel is None:
		await ctx.send('No channel was found :(')
		return

	await ctx.author.move_to(lfg_fullest_channel, reason='lfg')
	await ctx.send(f'You have been moved into <#{lfg_fullest_channel.id}>')


    

with open('token.txt', 'r') as f:
	token = f.read().strip()

bot.run(token)