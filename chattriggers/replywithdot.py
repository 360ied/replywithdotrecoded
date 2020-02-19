import chattrigger

class ReplyWithDot(chattrigger.ChatTrigger):
	
	async def run(self, message, trigger, client):
		if message.content == ".": await message.channel.send(".")