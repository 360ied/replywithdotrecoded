import onmemberjointask
import os
import discord

class AutoLimboChannel(onmemberjointask.OnMemberJoinTask):

	async def run(self, member, client):
		z8guildid = int(os.environ.get("Z8GUILD"))
		if not member.guild.id == z8guildid: return
		#z8guild = client.get_guild(z8guildid)
		rm = client.get_channel(int(os.environ.get("LIMBO_CATEGORY_CHANNEL_ID")))
		limbocategory = rm.category
		channels = limbocategory.text_channels

		slowmodetime = 5

		overwrite = discord.PermissionOverwrite(read_messages = True, send_messages = True, read_message_history = True)

		for i in channels:
			if str(member.id) == i.name:
				await i.set_permissions(member, overwrite = overwrite)
				await i.edit(position = rm.position + 1)
				await self.greet(member, i)
				return
		overwrites = {
			member: overwrite
		}
		lchannel = await limbocategory.create_text_channel(member.id, overwrites = overwrites, position = rm.position + 1, topic = f"Verification Channel for {str(member)} ({member.id})", slowmode_delay = slowmodetime, reason = f"Verification Channel for {str(member)} ({member.id})")
		#await limbocategory.create_text_channel(f"{member.id}", position = 1, overwrites = overwrites)
		print(lchannel.position)
		#await lchannel.edit(position = 1)
		print(lchannel.position)
		await self.greet(member, lchannel)
	
	async def greet(self, member, channel):
		await channel.send(f"{member.mention}, Welcome to the server. Please wait until someone verifys you.")
