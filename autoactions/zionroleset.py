import autoaction
from utils import persistentstorage
import os

class ZionRoleSet(autoaction.AutoAction):

	async def run(self, message, client):
		if not message.guild.id == int(os.environ.get("Z8GUILD")): return
		rolesreader = persistentstorage.PersistentStorage("Roles Reader", int(os.environ.get("ZIONROLES_CHANNEL_ID")), client, ".")
		roles = [int(i) for i in (await rolesreader.read())]
		print(roles)
		print("Asdf")
		if any(i in message.author.roles for i in roles):
			print("asdf")
			await message.author.add_roles(message.guild.get_role(int(os.environ.get("ZION_STUDENTS_ROLE_ID"))))