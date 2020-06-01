import os
import random
import sys

import chattrigger


class KillBot(chattrigger.ChatTrigger):

    async def run(self, message, trigger, client):
        ownerid = int(os.environ.get("OWNER_ID"))
        if not message.author.id == ownerid:
            await message.channel.send(f"{message.author.mention}, :joy_cat: nice try buddy.")
            return
        responses = ["See you on the other side.", "I'll be back.", "Bye bye.", "Goodbye, cruel world.",
                     "REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"]
        await message.channel.send(f"{message.author.mention}, {random.choice(responses)}")
        print("Shutting down...")
        sys.exit(0)
