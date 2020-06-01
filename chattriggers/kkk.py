import chattrigger


class Kkk(chattrigger.ChatTrigger):

    async def run(self, message, trigger, client):
        await message.channel.send(
            "OMG " + message.author.mention + " you homophobic facist white supremacistic racist!!!!!!!")
