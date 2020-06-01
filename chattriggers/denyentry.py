import os

import chattrigger


class DenyEntry(chattrigger.ChatTrigger):

    async def run(self, message, trigger, client):  # allows users to verify members currently in limbo
        persontoverify = message.mentions[0]
        reason = message.content.split(" ")[2]
        limboroleid = int(os.environ.get("LIMBO_ROLE_ID"))
        guildid = int(os.environ.get("Z8GUILD"))
        guild = client.get_guild(guildid)
        limborole = guild.get_role(limboroleid)
        if not message.author.guild_permissions.administrator:  # to stop self verification
            await message.channel.send(f"{message.author.mention}, you do not have permission to deny entry to guests.")
            return
        if not limborole in persontoverify.roles:
            await message.channel.send(f"{message.author.mention}, {persontoverify.mention} is not a guest.")
            return
        await persontoverify.create_dm()
        await persontoverify.dm_channel.send(f"You have been removed from the server. Reason: {reason}")
        await guild.kick(persontoverify)
        await message.channel.send(f"{message.author.mention}, done.")
