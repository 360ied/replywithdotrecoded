import os

import chattrigger


class PurgeChannel(chattrigger.ChatTrigger):

    async def run(self, message, trigger, client):
        ownerid = int(os.environ.get("OWNER_ID"))
        if not message.author.id == ownerid: return
        for i
