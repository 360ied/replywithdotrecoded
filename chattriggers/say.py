import chattrigger
import os

class Say(chattrigger.ChatTrigger):
	
	async def run(self, message, trigger, client):
		#ownerid = int(os.environ.get("OWNER_ID"))
		#if not message.author.id == ownerid: # only owner can use command
		#	return
		tosay = message.content[len(trigger):]
		await message.channel.send(tosay)
		await message.delete()