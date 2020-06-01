import os

import discord

import onmemberjointask


class AutoLimboChannel(onmemberjointask.OnMemberJoinTask):

    async def run(self, member: discord.Member, client: discord.Client):

        # i dont want this on all servers

        if not member.guild.id in [int(x) for x in os.environ.get("LIMBOCHANNELSERVERS").split(",")]: return

        # z8guildid = int(os.environ.get("Z8GUILD"))
        # if not member.guild.id == z8guildid: return
        # z8guild = client.get_guild(z8guildid)
        # rm = client.get_channel(int(os.environ.get("LIMBO_CATEGORY_CHANNEL_ID")))
        # limbocategory = rm.category

        # channels = limbocategory.text_channels
        channels = member.guild.text_channels

        slowmodetime = 5  # to avoid spamming and conversations in verification channels

        overwrite = discord.PermissionOverwrite(read_messages=True, send_messages=True, read_message_history=True)

        for i in channels:
            if str(member.id) == i.name:
                await i.set_permissions(member, overwrite=overwrite)
                # await i.edit(position = rm.position + 1)
                await i.edit(position=0)
                await self.greet(member, i)
                return

        limbocategory = await self.findlimbocategory(member, client)

        overwrites = {
            member: overwrite
        }
        # lchannel = await limbocategory.create_text_channel(member.id, overwrites = overwrites, position = rm.position, topic = f"Verification Channel for {str(member)} ({member.id})", slowmode_delay = slowmodetime, reason = f"Verification Channel for {str(member)} ({member.id})")
        lchannel = await limbocategory.create_text_channel(member.id, overwrites=overwrites, position=0,
                                                           topic=f"Verification Channel for {str(member)} ({member.id})",
                                                           slowmode_delay=slowmodetime,
                                                           reason=f"Verification Channel for {str(member)} ({member.id})")
        await lchannel.edit(position=0)  # fsr, doesnt work on channel creation
        # await limbocategory.create_text_channel(f"{member.id}", position = 1, overwrites = overwrites)
        print(lchannel.position)
        # await lchannel.edit(position = 1)
        print(lchannel.position)
        await self.greet(member, lchannel)

    async def greet(self, member, channel):  # to let the new user know what the hell is going on
        # await channel.send(f"{member.mention}, Welcome to the server. Please wait until someone verifys you.")
        # await channel.send(f"{member.mention}, Welcome to the server. Please wait until someone gives you a role.")
        await channel.send(
            f"{member.mention}, Welcome to {member.guild.name}. Please ask for someone to give you a role.")  # 2020-05-06, the previous message just had users sitting around for a few minutes and then leaving

    # new addition

    async def findlimbocategory(self, member: discord.Member,
                                client: discord.Client):  # i dont want to overcomplicate the main function
        allcategorychannels = member.guild.categories

        for i in allcategorychannels:
            if i.name == "limbo":
                # return i
                if len(i.channels) == 50:  # discord has a 50 channel limit within categories, so skip over it
                    continue
                else:  # found a viable category
                    return i

        # no viable categories found, creating a new one

        return await member.guild.create_category("limbo")
