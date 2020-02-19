import startuptask
import persistentstorage
import os

class ZionRoleSet(startuptask.StartUpTask):

	async def run(self, client):
		z8guild = client.get_guild(int(os.environ.get("Z8GUILD")))
		rolesreader = persistentstorage.PersistentStorage("Roles Reader", int(os.environ.get("ZIONROLES_CHANNEL_ID")), client, ".")
		roles = [int(i) for i in (await rolesreader.read())]
		for i in z8guild.members:
			if any(j in [l.id for l in i.roles] for j in roles):
				#print(i.name)
				await i.add_roles(z8guild.get_role(int(os.environ.get("ZION_STUDENTS_ROLE_ID"))))
