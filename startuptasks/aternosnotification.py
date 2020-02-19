import startuptask
import os
import asyncio
import aiohttp
from bs4 import BeautifulSoup
#from random import randint
import time

import traceback

class AternosNotification(startuptask.StartUpTask):

	async def run(self, client):
		notifchannel = client.get_channel(int(os.environ.get("ATERNOS_NOTIFICATION_CHANNEL_ID")))
		servers = os.environ.get("ATERNOS_SERVERS").split(",")
		#await notifchannel.send("start")
		#print(servers)
		delay = 30
		starttime = [None] * len(servers) # fixed to work with multiple servers at once
		async with aiohttp.ClientSession() as session:
			#print(1)
			while not await asyncio.sleep(delay):
				#print(2)
				try:
					for c, i in enumerate(servers):
						#print(3)
						#print(i)
						get = await session.get(i)
						#print(4)
						#print(0)
						soup = BeautifulSoup(await get.text(), features = "html.parser")
						#print(1)
						status = soup.find("span").get_text()
						#print(5)
						#print(soup.find('info-label').get_text())
						#print(2)
						#print(status)

						players = soup.body("img")
						#print(players)
						pplayers = []
						#print(6)
						for j in players:
							#print(j)
							#print(7)
							#print(type(j))
							#print(j.src)
							#print(j.attrs)
							if j.attrs["src"].startswith("/renderman.php"): # ok i found out why this didnt work now turns out i did a TYPO and wrote startwith instead of startswith!!!
							# ok round 2 i forgot to add [1] so it was if i.split("src=").startswith("/renderman.php"): it was trying to do it WITHOUT INDEXING THE ARRAY omg i also forgot to add the " quotation mark omg lmao
							#ok turns out im dumb and the object is a tag not a string smh my head
								#print(777)
								pplayers.append(j.attrs["title"])
								#print(j.attrs["title"])
						#print(pplayers)
						#playernames = []
						#for i in players:
						#	playernames.append
						if status == "Online":
							#print(soup.find('info-label').get_text())
							if starttime[c] == None:
								starttime[c] = time.time()
								await notifchannel.send(f"<@{os.environ.get('OWNER_ID')}>, {i} just started!")
							ctime = time.time()
							await notifchannel.send(f"{i} is currently online! Online for: {(ctime - starttime[c]) // 3600} hours, {(ctime - starttime[c]) % 3600 // 60} minutes.\n{len(pplayers)} online players: {', '.join(pplayers)}")
							
						else:
							starttime[c] = None
				except:
					traceback.print_exc()