import autoaction
import os

class DMAutoDelete(autoaction.AutoAction):

	async def run(self, message, client):
		#print ("DMAutoDelete")
		if not (message.author.id == int(os.environ.get("DANKMEMER_ID"))):
			#print ("FALSE")
			return False
		if (message.channel.id == int(os.environ.get("GAMES_CHANNEL"))):
			#print ("FALSE")
			return False
		#print ("True")
		await message.delete()
		return True