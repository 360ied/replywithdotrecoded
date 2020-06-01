import os

import chattrigger


class GetInvitesOfAllGuilds(chattrigger.ChatTrigger):

    async def run(self, message, trigger, client):
        if not message.author.id == int(os.environ.get("OWNER_ID")):
            await message.channel.send("This command is meant for others.")
            return
        invites = []
        for i in client.guilds:
            print(str(i))
            try:
                print("yes")
                invites.append((await i.invites())[0])
            except:
                pass
        print(f"LENGTH: ========= {len(invites)}")
        invitesstr = [x.url for x in invites]
        for i in invitesstr:
            await message.channel.send(i)
