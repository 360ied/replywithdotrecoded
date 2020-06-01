import discord
from wiktionaryparser import WiktionaryParser

import chattrigger


class MeaningWiktionary(chattrigger.ChatTrigger):

    async def run(self, message: discord.Message, trigger: str, client: discord.Client):
        word = message.content[len(trigger):]  # string
        parser = WiktionaryParser()
        fetched = parser.fetch("word", language="english")  # default could also be used as default is english
        print(fetched)
