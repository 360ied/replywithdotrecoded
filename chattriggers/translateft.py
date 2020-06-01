from googletrans import Translator

import chattrigger


class TranslateFT(chattrigger.ChatTrigger):

    async def run(self, message, trigger, client):
        translator = Translator()
        messagesplit = message.content.split(" ")
        totranslatelng = messagesplit[2]
        msglng = messagesplit[1]
        totranslate = message.content[len(trigger) + len(totranslatelng) + len(msglng) + 2:]
        try:
            translated = translator.translate(totranslate, totranslatelng, msglng)
        except:
            print("translation failed")
            await message.channel.send("Translation Failed! IP address might be banned or invalid language(s).")
            return
        await message.channel.send("From [" + msglng + "] To [" + totranslatelng + "]: " + translated.text)
