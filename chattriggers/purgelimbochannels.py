import chattrigger


class PurgeLimboChannels(chattrigger.ChatTrigger):

    async def run(self, message, trigger, client):
        return False
