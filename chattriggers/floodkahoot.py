# 2020-05-26

import asyncio
import os

import discord

import chattrigger
import klib


class FloodKahoot(chattrigger.ChatTrigger):

    async def run(self, message: discord.Message, trigger: str, client: discord.Client):

        args = message.content.split(" ")

        code = args[1]

        nofbots = int(args[2])

        name = " ".join(args[3:])

        khuser = os.environ.get("KAHOOT_EMAIL")
        # print(khuser)
        khpass = os.environ.get("KAHOOT_PASSWORD")
        # print(khpass)

        # loop = client.loop
        namesuffixes = list(range(nofbots))
        namesuffixes[0] = ""
        print(namesuffixes)

        bots = [klib.Kahoot(code, f"{name}{x}", client.loop) for x in namesuffixes]

        # [client.loop.run_in_executor(None, x.authenticate, khuser, khpass) for x in bots] # i love list comprehension
        auth = bots[0].authenticate(khuser, khpass)
        for i in bots: i.authToken = auth

        [client.loop.run_in_executor(None, x.checkPin) for x in bots]
        # now start
        flag = True
        while 1:
            for i in bots:
                try:
                    i.sessionID
                    i.authToken
                except AttributeError:
                    flag = False
                    break
            if flag:
                break
            flag = True
            await asyncio.sleep(.1)
        # [client.loop.run_in_executor(None, x.startGame) for x in bots]
        # [client.loop.create_task(x._play()) for x in bots] # skip the crap
        for i in bots:
            try:
                client.loop.create_task(i._play())
            except asyncio.CancelledError:
                print("CancelledError")

        await message.channel.send("Done")
