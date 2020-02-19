import chattrigger
from googletrans import Translator

class Translate(chattrigger.ChatTrigger):
	
	async def run(self, message, trigger, client):
		translator = Translator()
		totranslate = message.content[len(trigger):]
		try:
			translated = translator.translate(totranslate, dest = "en")
			await message.channel.send(f"From [{translated.src}]: {translated.text}")
		except:
			await message.channel.send("An error occured! IP address might be banned.")
		