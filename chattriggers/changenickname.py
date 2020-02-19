import chattrigger
import os

class ChangeNickname(chattrigger.ChatTrigger):
	
	async def run(self, message, trigger, client):
		ownerid = int(os.environ.get("OWNER_ID"))
		if not message.author.id == ownerid:
			print("notownerid")
			await message.channel.send(f"{message.author.mention}, you do not have permission to use this command.")
			return
		guildid = int(os.environ.get("Z8GUILD"))
		guild = client.get_guild(guildid)
		tonick = message.content[len(trigger):]
		try:
			await guild.me.edit(nick = tonick)
			await message.channel.send(f"{message.author.mention}, I have changed my nickname to: {tonick}.")
		except:
			await message.channel.send(f"{message.author.mention}, Command Failed! Nickname must be 32 or fewer characters in length.")