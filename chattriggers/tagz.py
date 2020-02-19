import chattrigger
import os
import time

class TagZ(chattrigger.ChatTrigger):
	
	async def run(self, message, trigger, client):
		print("tagz triggered")
		a = message.content[len(trigger):]
		if not (a.isdigit()):
			await message.channel.send("Command aborted! n(" + a + ") is not a valid number!")
			return
		n = int(a)
		limit = 10
		if n > limit:
			await message.channel.send("Command aborted! n(" + a + ") is larger than limit(" + str(limit) + ")!")
			return
		z = int(os.environ.get("Z"))
		for i in range(n):
			await message.channel.send("<@" + str(z) + ">") # alternative solution to avoid circular import
			time.sleep(2)