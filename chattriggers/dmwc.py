import os

import chattrigger


class DMWC(chattrigger.ChatTrigger):

    async def run(self, message, trigger, client):
        gc = int(os.environ.get("GAMES_CHANNEL"))
        if not (message.channel.id == gc):
            await message.channel.send(f"{message.author.mention} WRONG CHANNEL")
