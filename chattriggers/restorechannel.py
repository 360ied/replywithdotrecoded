import chattrigger

import discord

import os

class RestoreChannel(chattrigger.ChatTrigger): # fuck you elizabeth
	
	async def run(self, message: discord.Message, trigger: str, client: discord.Client):

		if not message.author.id == int(os.environ.get("OWNER_ID")):
			await message.channel.send("This command is meant for others.")
			return

		restorechannelname = message.content[len(trigger):]
		print(restorechannelname)
		#return
		messagelogchannelid = int(os.environ.get("MSG_LOG_CHANNEL_ID"))
		messagelogchannel = client.get_channel(messagelogchannelid)

		async for i in messagelogchannel.history(limit = None, oldest_first = True):
			try:
				msgembed = i.embeds[0]
			except:
				print("MESSAGE DIDNT HAVE EMBED")
				print(i.content)
				continue

			titleparse = msgembed.title.split(" in ") # name#0000 in channel in server
			print(titleparse)

			print(titleparse[1] == restorechannelname)
			print(titleparse[2] == message.guild.name)
			if all((titleparse[1] == restorechannelname, titleparse[2] == message.guild.name)):

				await message.channel.send(embed = msgembed) # resend the archival message
				print("Restoring!")
