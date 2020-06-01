import sys
import time

import chattrigger


class GuildMessageCount(chattrigger.ChatTrigger):

    async def run(self, message, trigger, client):
        await message.channel.send("Warning: This command may take several minutes to complete! Please be patient.")
        messagecount = 0
        start = time.time()  # time.clock()
        for i in message.guild.text_channels:
            await message.channel.send(f"Reading {i.mention}")
            async for j in message.channel.history(limit=sys.maxsize):
                messagecount += 1
        end = time.time()  # time.clock()
        elapsed = end - start
        await message.channel.send(f"Counted {messagecount} messages. Took {elapsed} seconds.")
