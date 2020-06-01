import os

import autoaction


class AutoShadowLugia(autoaction.AutoAction):

    async def run(self, message, client):
        pokeassistantid = int(os.environ.get("POKEASSISTANT_ID"))
        if not message.author.id == pokeassistantid:
            return
        await message.channel.send(f"sl!spawnrate {message.content}")
