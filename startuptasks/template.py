import startuptask

import discord

class Template(startuptask.StartUpTask):

	async def run(self, client: discord.Client):
		print("do something")