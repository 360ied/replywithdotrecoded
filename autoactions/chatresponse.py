import os
import sys

import autoaction


class ChatResponse(autoaction.AutoAction):

    async def run(self, message, client):
        chatresponsechannel = client.get_channel(int(os.environ.get("CHATRESPONSE_CHANNEL_ID")))
        chatresponsechannelmessagelist = await chatresponsechannel.history(limit=sys.maxsize).flatten()
        chatresponsechannelmessagecontentlist = []
        for i in chatresponsechannelmessagelist:
            chatresponsechannelmessagecontentlist.append(i.content)
        chatresponsetriggers = [i.casefold() for i in chatresponsechannelmessagecontentlist[1::2]]
        chatresponseresponses = chatresponsechannelmessagecontentlist[0::2]
        # print(chatresponsetriggers)
        # print(chatresponseresponses)
        for c, i in enumerate(chatresponsetriggers):
            # print(i)
            if message.content.casefold() == i.casefold():
                await message.channel.send(chatresponseresponses[c])
                return
