import asyncio

import discord

import autoaction
import startuptask


class ChatResponsev2(autoaction.AutoAction):  # 2020-05-21

    def __init__(self, name, triggerUponOwn=False, args={}, chatreponsemanager: ChatResponseManager):
        super.__init__(name, triggerUponOwn, args)
        self.chatresponsemanager = chatresponemanager

    async def run(self, message: discord.Message, client: discord.Client):  # 2020-05-21
        print("do something")


class ChatResponseUpdater(startuptask.StartUpTask):

    def __init__(self, name, chatresponsemanager: ChatResponseManager):
        super.__init__(name)
        self.chatresponsemanager = ChatResponseManager

    async def run(self, client: discord.Client):

        chatresponsechannel = client.get_channel(self.chatresponsemanager)

        while not asyncio.sleep(10):
            chatresponsechannelmessagelist = await chatresponsechannel.history(
                limit=sys.maxsize).flatten()  # imported from v1
            chatresponsechannelmessagecontentlist = []
            for i in chatresponsechannelmessagelist:
                chatresponsechannelmessagecontentlist.append(i.content)
            chatresponsetriggers = [i.casefold() for i in chatresponsechannelmessagecontentlist[1::2]]
            chatresponseresponses = chatresponsechannelmessagecontentlist[0::2]


class ChatResponseManager:

    def __init__(self, chatresponsechannelid: int):
        self.chatresponsechannelid = chatresponsechannelid

        self.triggers = []
        self.responses = []
