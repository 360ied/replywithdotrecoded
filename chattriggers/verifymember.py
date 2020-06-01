import os

import chattrigger


class VerifyMember(chattrigger.ChatTrigger):

    async def run(self, message, trigger, client):  # allows users to verify members currently in limbo
        persontoverify = message.mentions[0]
        limboroleid = int(os.environ.get("LIMBO_ROLE_ID"))
        guildid = int(os.environ.get("Z8GUILD"))
        guild = client.get_guild(guildid)
        limborole = guild.get_role(limboroleid)
        if not message.author.guild_permissions.administrator:  # to stop self verification
            await message.channel.send(f"{message.author.mention}, you do not have permission to verify members.")
            return
        await persontoverify.remove_roles(limborole, reason=f"Verified by {str(message.author)} ({message.author.id}).")
        await message.channel.send(f"Verified {persontoverify.mention}.")
