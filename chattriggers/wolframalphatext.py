# from io import BytesIO
# import discord
import os

import requests

import chattrigger


class WolframAlpha(chattrigger.ChatTrigger):

    async def run(self, message, trigger, client):
        query = message.content[len(trigger):]
        apirequest = requests.get(
            f"https://api.wolframalpha.com/v1/result?appid={os.environ.get('WOLFRAM_ALPHA_APP_ID')}&i={query}")
        # print(imgrequest.content)
        # if str(imgrequest.content) == "b'Wolfram|Alpha did not understand your input'":
        #	await message.channel.send("Wolfram|Alpha did not understand your input.")
        #	return
        # print(f"https://api.wolframalpha.com/v1/simple?i={query}&width=800&appid=DEMO")
        # imgfile = BytesIO(imgrequest.content)
        # discordimgfile = discord.File(imgfile, filename = "result.png")
        # await message.channel.send(file = discordimgfile)
        await message.channel.send(apirequest.text)
