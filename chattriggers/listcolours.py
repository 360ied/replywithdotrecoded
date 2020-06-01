import os

import aiohttp
import discord

import chattrigger


class ListColours(chattrigger.ChatTrigger):

    async def run(self, message: discord.Message, trigger: str, client: discord.Client):
        async with aiohttp.ClientSession() as session:
            get = await session.get(f"https://www.jsonstore.io/{os.environ.get('COLOUR_ROLES_JSONSTORE_TOKEN')}")
        # print(await get.text())
        gjson = (await get.json())["result"]
        print(gjson)
        print(gjson.items())

        colourroles = [message.guild.get_role(int(x)) for x in gjson.values()]

        for i in colourroles:
            embed = discord.Embed(title=i.name, description=str(i.colour), colour=i.colour)
            await message.channel.send(embed=embed)
