import chattrigger


class IsAternosServerOnline(chattrigger.ChatTrigger):

    async def run(self, message, trigger, client):
        return False
