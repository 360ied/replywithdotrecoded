import chattrigger
import os
import sys
import asyncio

class PurgeChannel(chattrigger.ChatTrigger):
	
	async def run(self, message, trigger, client):
		ownerid = int(os.environ.get("OWNER_ID"))
		if not message.author.id == ownerid: return
		await message.channel.purge(limit = sys.maxsize)
		response = await message.channel.send("Purged Channel.")
		await asyncio.sleep(5)
		await response.delete()