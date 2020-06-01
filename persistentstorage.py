class PersistentStorage:
    def __init__(self, name, channelid, client, separator):
        self.name = name
        self.channel = client.get_channel(channelid)
        self.separator = separator

    async def read(self):
        a = await self.channel.history(limit=1).flatten()
        b = a[0].content[1:].replace("\n", "").split(
            self.separator)  # first item in channel history, substring from char 1, removes nextlines, splits in seperator to create list
        return b

    async def write(self, towrite):
        # a = self.separator.join([str(i) for i in towrite])

        print("write triggered")

        await self.channel.send(towrite)

    async def nwrite(self, towrite):  # new function for backwards compatibility

        await self.channel.send(f"{self.seperator}{self.separator.join([str(i) for i in towrite])}")

    # we have to keep in mind the (stupid) 2000 character limit for messages

    async def add(self, toadd):
        current = await self.read()
        current.append(toadd)
        await self.nwrite(current)
