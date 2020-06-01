import os
import time

import onmemberjointask


class LimboChannelAutoGreet(onmemberjointask.OnMemberJoinTask):

    async def run(self, member, client):
        if not member.guild.id == int(os.environ.get("Z8GUILD")): return  # avoid execution in foreign guilds
        limbochannelid = int(os.environ.get("LIMBO_CHANNEL_ID"))
        limbochannel = client.get_channel(limbochannelid)
        time.sleep(1)
        await limbochannel.send(
            f"Welcome to the Immigration Center {member.mention}. Please stand by shortly while one of our staff members review your documents.")
