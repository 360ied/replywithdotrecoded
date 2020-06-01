import os

import autoaction


class InviteManagerDelete(autoaction.AutoAction):

    async def run(self, message, client):
        invitemanagerid = int(os.environ.get("INVITE_MANAGER_BOT_ID"))
        if not message.author.id == invitemanagerid: return
        if not len(message.embeds) > 0: return
        # print (message.embeds[0].title)
        triggerupon = ["InviteManager is missing the permissions", "premium subscribers"]
        # print(message.embeds[0].description)
        for i in triggerupon:
            # print(i)
            if i in message.embeds[0].description:
                # print("yeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
                await message.delete()
                return

        return
