import os

import autoaction
import persistentstorage


class UserImageDelete(autoaction.AutoAction):

    async def run(self, message, client):
        persistentstoragechannelid = int(os.environ.get("IMAGE_LESS_USERS"))
        userreader = persistentstorage.PersistentStorage("Image-less Users", persistentstoragechannelid, client, ".")
        usersread = await userreader.read()
        users = []
        for i in usersread:
            i = i.split(",")
            users.append((int(i[0]), i[1]))
        for i in users:
            j = i[0]
            # print(j)
            if not message.author.id == j: continue
            # print(1)
            if not len(message.attachments) > 0: continue
            # print(2)
            # if not len(message.embeds) > 0: continue
            # print(3)
            await message.delete()
            try:
                await message.channel.send(i[1])
            except:
                return
