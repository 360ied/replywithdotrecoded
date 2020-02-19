import startuptask

import asyncio

import os

import discord

import time

#import IndexError

class VoiceChannelTimeCounter(startuptask.StartUpTask): # ExceedinglyExtensiveModuleDefinitions

	async def run(self, client: discord.Client):
		print("VoiceChannelTimeCounter")
		delay = 10

		instr = os.environ.get("VOICE_CHANNEL_TIME_COUNTER_SERVERS")

		servers = [client.get_guild(int(x.split(":")[0])) for x in instr.split(",")]
		channels = [client.get_guild(int(x.split(":")[1])) for x in instr.split(",")]
		
		previnvoice = [] # [c][cc][1] time
		nextinvoice = []

		while not await asyncio.sleep(delay):
			for c, i in enumerate(servers):
				print(c)
				members = i.members
				invoice = []
				for cc, ii in enumerate(members):
					if not ii.voice == None:
						try:
							if ii.id not in [x[0] for x in previnvoice]:
								try:
									invoice.append((ii.id, time.time()))
								except: pass
						except: pass

						else:
							try:
								for j in previnvoice[c]:
									try:
										if j[0] == ii.id:
											invoice.append(j)
									except: pass
							except: pass
						
					#else:
					#	for j in previnvoice[c]:
					#		if j[0] == ii.id:
				print(invoice)
				nextinvoice.append(invoice)
			previnvoice = nextinvoice
			nextinvoice = []

				