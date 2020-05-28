import startuptask

import discord

import os

import asyncio

import traceback

class LockNickname(startuptask.StartUpTask):

	async def run(self, client: discord.Client):
		
		targetsid = [int(x) for x in os.environ.get("SETNICKNAMETARGETS").split(",")]
		serversid = [int(x) for x in os.environ.get("SETNICKNAMESERVERS").split(",")]
		results = os.environ.get("SETNICKNAMERESULTS").split(",")

		errorlogchannel = client.get_channel(int(os.environ.get("ERRORLOGCHANNELID")))

		#servers = []
		targets = []

		for c, i in enumerate(serversid):

			targets.append(client.get_guild(i).get_member(targetsid[c]))


		delay = 10

		while not await asyncio.sleep(delay):

			#print(f"locknickname targets = {[str(x) for x in targets]}")
			
			#print(f"locknickname len(targets) = {len(targets)}")
			
			for i in range(len(targets)):

				#print(f"locknickname i = {i}")

				try:

					await targets[i].edit(nick = results[i])
				
				except:
					
					traceback.print_exc()
					await errorlogchannel.send(f"**Error!**\n{traceback.format_exc()}")

