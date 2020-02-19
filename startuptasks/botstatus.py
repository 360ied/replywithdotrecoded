import startuptask
import discord

class BotStatus(startuptask.StartUpTask):

	async def run(self, client):
		await client.change_presence(activity = discord.Activity(name = "matthew screaming", type = 2))