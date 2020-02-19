import autoaction
from persistentstorage import PersistentStorage
import os

class BannedWords(autoaction.AutoAction):

	async def run(self, message, client):
		chid = int(os.environ.get("BANNED_WORDS_CHANNEL_ID"))
		bw = PersistentStorage("Banned Words", chid, client, ".")
		bwl = [i.casefold().replace(" ", "") for i in await bw.read()]
		for i in bwl:
			if i in message.content.casefold().replace(" ", ""):
				try:
					await message.delete()
				except:
					return False
				return True