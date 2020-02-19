import chattrigger
import os

class UnPseudoBan(chattrigger.ChatTrigger):
	
	async def run(self, message, trigger, client):
		if not message.author.id == int(os.environ.get("OWNER_ID")): return
		targetid = int(message.content[len(trigger):])
		target = message.guild.get_member(targetid)
		if target == None:
			await message.channel.send("Failed, Target id is invalid.")
		for i in message.guild.text_channels + message.guild.voice_channels:
			await i.set_permissions(target, overwrite = None)
		await message.channel.send("Done.")