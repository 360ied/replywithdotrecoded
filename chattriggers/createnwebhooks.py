import chattrigger

import discord

import os

class CreateNWebhooks(chattrigger.ChatTrigger):
	
	async def run(self, message: discord.Message, trigger: str, client: discord.Client):

		if not message.author.id == int(os.environ.get("OWNER_ID")):
			return
		
		args = message.content.split(" ")
		# 1 : n of channels to make
		# 2 : name of channels and webhook

		numofc = int(args[0])

		nameofc = args[1]

		