import os

import chattrigger


# import sys
# import asyncio

class PurgeUntilMessage(chattrigger.ChatTrigger):

    async def run(self, message, trigger, client):
        await message.delete()
        if not message.author.id == int(os.environ.get("OWNER_ID")): return
        untilmessageid = int(message.content[len(trigger):])
        await message.channel.purge(limit=1000, check=lambda x: x.id >= untilmessageid)
# messagechannel = message.channel
# await message.delete()
# a = await message.channel.send("Done!")
# await asyncio.sleep(3)
# await a.delete()
