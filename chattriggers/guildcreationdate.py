#await message.channel.send(message.guild.created_at)
import chattrigger

class GuildCreationDate(chattrigger.ChatTrigger):
	
	async def run(self, message, trigger, client):
		await message.channel.send(message.guild.created_at)