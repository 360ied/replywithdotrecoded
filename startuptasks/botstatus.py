import discord

import startuptask


# import asyncio

class BotStatus(startuptask.StartUpTask):

    async def run(self, client):
        # await client.change_presence(activity = discord.Activity(name = "hook, line, and sinker", type = 0))
        # 2020-05-08

        # status = "hook, line, and sinker. "
        status = "ANGER DANIEL :joy:"  # 2020-05-16

        # while 1:

        await client.change_presence(activity=discord.Activity(name=status, type=0))
# print(status)
# status = status[-1] + status[:-1]
# print(status)

# await asyncio.sleep(5)
