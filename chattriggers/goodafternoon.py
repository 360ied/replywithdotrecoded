import chattrigger


class GoodAfternoon(chattrigger.ChatTrigger):

    async def run(self, message, trigger, client):
        await message.channel.send("good afternoon")
