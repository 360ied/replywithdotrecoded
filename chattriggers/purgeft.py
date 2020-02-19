import chattrigger
import os
#import sys
#import asyncio

class PurgeFT(chattrigger.ChatTrigger):
	
	async def run(self, message, trigger, client):
		await message.delete()
		if not message.author.id == int(os.environ.get("OWNER_ID")): return
		args = message.content.split(" ")
		frommessageid = int(args[1])
		tomessageid = int(args[2])
		await message.channel.purge(limit = 1000, check = lambda x : all((x.id >= frommessageid, x.id <= tomessageid)))
		#messagechannel = message.channel
		#await message.delete()
		#a = await message.channel.send("Done!")
		#await asyncio.sleep(3)
		#await a.delete()