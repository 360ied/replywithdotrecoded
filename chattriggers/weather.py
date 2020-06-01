import pyowm

import chattrigger


class Template(chattrigger.ChatTrigger):

    async def run(self, message, trigger, client):
        owm = pyowm.OWN()
        city = message.content[len(trigger):]
