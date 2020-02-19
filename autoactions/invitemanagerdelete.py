import autoaction
import os

class InviteManagerDelete(autoaction.AutoAction):

	async def run(self, message, client):
		invitemanagerid = int(os.environ.get("INVITE_MANAGER_BOT_ID"))
		if not message.author.id == invitemanagerid: return
		if not len(message.embeds) > 0: return
		#print (message.embeds[0].title)
		if not "InviteManager is missing the permissions" in message.embeds[0].description:
			return
		await message.delete()
		return True