from io import BytesIO

import discord
import requests

import chattrigger


class GetWebFile(chattrigger.ChatTrigger):

    async def run(self, message, trigger, client):
        query = message.content[len(trigger):]
        queryfilerequest = requests.get(query)
        queryfilename = query.split("/")[-1]
        queryfile = BytesIO(queryfilerequest.content)
        querydiscordfile = discord.File(queryfile, filename=queryfilename)
        try:
            await message.channel.send(file=querydiscordfile)
        except:
            await message.channel.send("Probably file too large.")
