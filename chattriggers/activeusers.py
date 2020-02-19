import chattrigger
import time
#from utils import persistentstorage
import os

class ActiveUsers(chattrigger.ChatTrigger):
	
	async def run(self, message, trigger, client):
		users = []

		#activetimereader = persistentstorage.PersistentStorage("Active Time Reader", int(os.getenv("ACTIVE_TIME_CHANNEL_ID")), client, ".")
		activetime = 180 # WHAT THE FUCK WAS I DOING WHY DDID THIS NEED TO BE ADJUSTABLE

		for i in message.guild.text_channels:
			async for j in i.history():
				#print(j.created_at.timestamp() - 300)
				if j.created_at.timestamp() > int(time.time()) - activetime:
					if not j.author in users and not j.author.bot:
						users.append(j.author)
		
		usernames = f"{len(users)} users: "

		for i in users:
			nextuser = f"{i.display_name} | "
			if len(usernames + nextuser) > 2000:
				await message.channel.send(usernames)
				usernames = ""
			usernames += nextuser
		
		usernames = usernames[:-3] # 3 = len(" | ")


		try:
			await message.channel.send(usernames)
		except:
			await message.channel.send("No Active Users found.")