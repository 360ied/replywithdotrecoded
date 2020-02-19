import onmemberjointask

import os

class Template(onmemberjointask.OnMemberJoinTask):

	async def run(self, member, client):
		if not member.guild.id == int(os.environ.get("Z8GUILD")): return # avoid execution in foreign guilds
		print("do something")