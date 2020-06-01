import os

import aiohttp
import discord

import chattrigger


class GetColour(chattrigger.ChatTrigger):

    async def run(self, message: discord.Message, trigger, client):
        roles = message.guild.roles  # starts from lowest and ends at highest

        colourrolename = message.content[len(trigger):]

        async with aiohttp.ClientSession() as session:
            get = await session.get(f"https://www.jsonstore.io/{os.environ.get('COLOUR_ROLES_JSONSTORE_TOKEN')}")

        gjson = (await get.json())["result"]

        try:
            colourroleid = int(gjson[f"{message.guild.id}{colourrolename.replace(' ', '%20')}"])
            print(colourroleid)
        except:
            await message.channel.send("Couldnt find colour!")
            return

        colourroles = [message.guild.get_role(int(x)) for x in gjson.values()]

        await message.author.remove_roles(*colourroles)

        await message.author.add_roles(message.guild.get_role(colourroleid))
        await message.channel.send("Done")
