import chattrigger

import discord

#import os

import allowuselimited

class SayChannel(chattrigger.ChatTrigger):
	
	async def run(self, message: discord.Message, trigger: str, client: discord.Client):

		#ownerid = int(os.environ.get("OWNER_ID")) # 2020-05-06, i discovered why you need to have this\
		#if not message.author.id == ownerid: # only owner can use command
			#return
		
		if not allowuselimited.allowuselimited(message.author.id, client): # 2020-05-07 only allow people from z8 to use command, to stop 7th graders from taking advantage
			return

		args = message.content.split(" ")

		targetchannel = client.get_channel(int(args[1]))

		if targetchannel == None: # 2020-05-07 allow for use of dmchannels
			targetchannel = client.get_user(int(args[1])) # discord.py allows sending directly to member objects

		tosay = " ".join(args[2:])

		await targetchannel.send(tosay)

		#try:
		#	await message.delete()
		#except:
		#	print("failed delete message in ,sayc command")