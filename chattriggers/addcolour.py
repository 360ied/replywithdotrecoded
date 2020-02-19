import chattrigger

import discord

#from utils import persistentstorage
import os

#import requests

from json_store_client import *

class AddColour(chattrigger.ChatTrigger):
	
	async def run(self, message, trigger, client):
		cmdarguments = message.content.split(" ")
		colourcode = int(cmdarguments[1][1:], 16) # ex: #FFFFFF
		colourname = " ".join(cmdarguments[2:])
		rolecolour = discord.Colour(colourcode)

		colourrole = await message.guild.create_role(name = colourname, colour = rolecolour, reason = str(message.author))

		await message.channel.send(f"Successfully created {colourname}")

		jsonclient = Client(os.environ.get("COLOUR_ROLES_JSONSTORE_TOKEN")) # unfortunately asyncclient doesnt work

		jsonclient.store(f"{message.guild.id}{colourname}", str(colourrole.id))
		print (colourrole.id)

		#print(requests.get(f"https://www.jsonstore.io/{os.environ.get('COLOUR_ROLES_JSONSTORE_TOKEN')}").content)


		#rcwriter = persistentstorage.PersistentStorage("rcwriter", 653727023264432158, client, ".")
		#rcwriter.write