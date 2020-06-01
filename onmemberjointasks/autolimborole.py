import os

import onmemberjointask


class AutoLimboRole(onmemberjointask.OnMemberJoinTask):

    async def run(self, member, client):
        if not member.guild.id == int(os.environ.get("Z8GUILD")): return  # avoid execution in foreign guilds
        guildid = int(os.environ.get("Z8GUILD"))
        limboroleid = int(os.environ.get("LIMBO_ROLE_ID"))
        guild = client.get_guild(guildid)
        limborole = guild.get_role(limboroleid)
        await member.add_roles(limborole)

        print("given limbo role")
