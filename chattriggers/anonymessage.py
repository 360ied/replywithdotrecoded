import os

import chattrigger


class AnonyMessage(chattrigger.ChatTrigger):

    async def run(self, message, trigger, client):
        # amc = int(os.environ("ANONYMOUS_MESSAGE_CHANNEL"))
        amsg = message.clean_content[len(trigger):]
        await client.get_channel(int(os.environ.get("ANONYMOUS_MESSAGE_CHANNEL"))).send("Anonymous Message: " + amsg)
        await client.get_channel(int(os.environ.get("ANONLOG"))).send(str(message.author) + ": " + amsg)
