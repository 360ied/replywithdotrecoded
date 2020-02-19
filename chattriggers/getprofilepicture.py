import chattrigger

class GetProfilePicture(chattrigger.ChatTrigger):
	
	async def run(self, message, trigger, client):
		try:
			member = message.mentions[0]
		except: # wonderful alternative to the if statement i know
			try:
				member = client.get_user(int(message.content[len(trigger):]))
			except:
				await message.channel.send("Member not found!")
				return
		memberprofilepicture = member.avatar_url
		await message.channel.send(memberprofilepicture)