import discord

import startuptask


class Template(startuptask.StartUpTask):

    async def run(self, client: discord.Client):
        print("do something")
