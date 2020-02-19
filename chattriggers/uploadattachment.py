import chattrigger
import requests

class UploadAttachment(chattrigger.ChatTrigger):
	
	async def run(self, message, trigger, client):
		if not len(message.attachments) > 0:
			await message.channel.send("FileNotFoundError")
			return
		attachment = message.attachments[0]
		attachmentfile = await attachment.read()
		print(attachmentfile)
		print(1)
		sending = requests.post("https://safe.fiery.me/api/upload", data = {"file" : attachmentfile}) # {attachment.filename: attachmentfile}
		print(2)
		print(sending.content)
		await message.channel.send(sending.content)