# import sys
import asyncio
import os

import discord

import chattrigger


class PurgeChannel(chattrigger.ChatTrigger):

    async def run(self, message: discord.Message, trigger: str, client: discord.Client):
        # ownerid = int(os.environ.get("OWNER_ID"))
        allowids = [int(x) for x in os.environ.get("PURGECHANNELALLOW").split(",")]
        if not message.author.id in allowids: return
        # await message.channel.purge(limit = sys.maxsize)
        async for i in message.channel.history(limit=None):
            await i.delete()
            print(f'''Deleted: <{i.author.name}> {i.clean_content}''')
        # response = await message.channel.send("Purged Channel.")
        response = await message.channel.send("Purged Channel.")
        await asyncio.sleep(5)
        await response.delete()
