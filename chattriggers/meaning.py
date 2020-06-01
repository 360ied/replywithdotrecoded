import discord
from PyDictionary import PyDictionary

import chattrigger


class Meaning(chattrigger.ChatTrigger):

    async def run(self, message, trigger, client):
        dictionary = PyDictionary()
        word = message.content[len(trigger):]
        definitionary = dictionary.meaning(word)
        definition = f"**{word}**:"
        if definitionary == None:
            definition += "\nNo Definition Found."
        else:
            for key, value in definitionary.items():
                toadd = f"\n*{key}*:\n"
                defs = ", ".join(value)
                toadd += discord.utils.escape_markdown(defs)
                if len(definition) + len(toadd) > 2000:
                    await message.channel.send(definition)
                    definition = ""
                definition += toadd
        await message.channel.send(definition)
