import chattrigger
import os

class PurgeLimboChannels(chattrigger.ChatTrigger):
	
	async def run(self, message, trigger, client):
		return False