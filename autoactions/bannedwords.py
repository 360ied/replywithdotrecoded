import autoaction
from persistentstorage import PersistentStorage
import os

from unidecode import unidecode

class BannedWords(autoaction.AutoAction):

	async def run(self, message, client):
		chid = int(os.environ.get("BANNED_WORDS_CHANNEL_ID"))
		bw = PersistentStorage("Banned Words", chid, client, ".")
		bwl = [i.casefold().replace(" ", "") for i in await bw.read()]
		for i in bwl:
			if i in unidecode(message.content).casefold().replace(" ", ""): # 2020-05-09 now filters special characters
				try:
					await message.delete()
				except:
					return False
				return True