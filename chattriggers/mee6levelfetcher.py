#import requests
import chattrigger
import discord
#import ranking
import aiohttp

class Mee6LevelFetcher(chattrigger.ChatTrigger):
	
	async def run(self, message, trigger, client):
		#r = requests.get(f"https://mee6.xyz/api/plugins/levels/leaderboard/{message.guild.id}")
		async with aiohttp.ClientSession() as session:
			get = await session.get(f"https://mee6.xyz/api/plugins/levels/leaderboard/{message.guild.id}")



		data = await get.json()

		emdescription = ""

		partcount = 1
		
		#try:
		if True:
			footer = "Note: Statistics only date back to the 17th of October 2019, with data from a short period of time in mid September of 2019."
			for c, i in enumerate(sorted(data["players"], key = lambda x: x["message_count"], reverse = True)):
				#try:
				#	username = message.guild.get_member(int(i["id"])).display_name
				#except:
				#	username = i["username"]
				nextplayer = f"#{c + 1} | <@{i['id']}> | Level {i['level']} | {i['message_count'] // 1440} days {i['message_count'] // 60 % 24} hours {i['message_count'] % 60} minutes chatting\n"
				if int(i["id"]) == message.author.id:
					#nextplayer = f"⬇️⬇️⬇️ **YOU** ⬇️⬇️⬇️\n{nextplayer}⬆️⬆️⬆️ **YOU** ⬆️⬆️⬆️\n"
					nextplayer = f"**{nextplayer}**"
				if len(emdescription) + len(nextplayer) > 2048:
					embed = discord.Embed(title = f"{message.guild.name} Leaderboards Part {partcount}:", description = emdescription, colour = discord.Colour.gold())
					embed.set_footer(text = footer)
					await message.channel.send(embed = embed)
					partcount += 1
					emdescription = ""
				emdescription += nextplayer
			embed = discord.Embed(title = f"{message.guild.name} Leaderboards Part {partcount}:", description = emdescription, colour = discord.Colour.gold())
			embed.set_footer(text = footer)
			await message.channel.send(embed = embed)
		#except:
		else:
			await message.channel.send("Error: Server might not have a Mee6 Leaderboard.")

