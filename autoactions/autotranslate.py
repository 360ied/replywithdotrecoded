import autoaction
import os
from utils.yantran import Yantranslator

class AutoTranslate(autoaction.AutoAction):

	async def run(self, message, client):
		if (message.content == None):
			return
		translator = Yantranslator(os.environ.get("YANDEX_TRANSLATE_API_KEY"))
		msglanguage = translator.indentify_language(message.content)
		print (msglanguage)
		if (msglanguage == ""):
			print("none")
			return False
		if (msglanguage == "en"):
			print("english")
			return False
		translatedmessage = translator.tran_sentence(msglanguage, "en", message.content)
		await message.channel.send("From [" + msglanguage + "]: " + translatedmessage)