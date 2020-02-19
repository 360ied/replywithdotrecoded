import chattrigger
import duckduckgo

class DuckSearch(chattrigger.ChatTrigger):
	
	async def run(self, message, trigger, client):
		searchquery = message.content[len(trigger):]
		duckquery = duckduckgo.get_zci(searchquery) # get_zci is basically auto select best result
		await message.channel.send(duckquery)
		return False