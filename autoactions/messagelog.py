import autoaction
import os
import discord

class MessageLog(autoaction.AutoAction):

	async def run(self, message, client):
		#print("loggingtriggered")
		excludedChannels = [int(x) for x in os.environ.get("CHATLOG_EXCLUSION").split(",")]
		if message.channel.id in excludedChannels: return
		#try: 
		print(f"{str(message.author)} in {str(message.channel)} in {str(message.guild)}: {message.content}")
		embed = discord.Embed(title = f"{str(message.author)} in {str(message.channel)} in {str(message.guild)}", description = f"{message.content}")
		embed.set_footer(text = f"Message id: {message.id}\nDate and Time: {str(message.created_at)}")
		await client.get_channel(int(os.environ.get("MSG_LOG_CHANNEL_ID"))).send(embed = embed)
		#except: passt