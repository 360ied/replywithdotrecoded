import os
from collections import Counter
from string import punctuation

import requests
from bs4 import BeautifulSoup
from unidecode import unidecode

import autoaction


# import aiohttp


class PokeManiaTeller(autoaction.AutoAction):

    async def run(self, message, client):
        # print("ran")
        pokemaniaid = 627952266455941121
        ownerid = int(os.environ.get("OWNER_ID"))
        testing = 0
        if not testing:  # testing is a bit hard, cus pokecord only spawns pokemon when you dont want it to

            if not (message.author.id == pokemaniaid) and not testing:  # if message is from pokecord
                return False
            if not (len(message.embeds) > 0) and not testing:  # if message has embeds
                return False
            print(message.embeds[
                      0].title)  # actually really useful, and hella cool, tells you when users are blacklisted, when people catch stuff, etc
            if not (message.embeds[0].description.startswith(
                    "**A wild Pokémon has appeared!")):  # ok we actually only want to respond to a wild pokemon stuff so
                return False
        if not testing:

            imageurl = message.embeds[0].image.url
        elif message.author.id == ownerid:
            print("owner trigger")
            imageurl = message.content
        else:
            return
        print(imageurl)
        self.imageurl = imageurl

        # result = await self.getPoke(imageurl)
        result = await client.loop.run_in_executor(None, self.getpoke)  # makes blocking functions non blocking
        print(result)
        # await message.channel.send(result)
        # 2020-05-13
        await message.channel.send(f",.catch p!catch {result}")

    def getpoke(self):  # be warned, this is a bit slow to function, ~ 10 seconds?

        filepath = self.imageurl
        searchUrl = 'http://www.google.com/searchbyimage?image_url='
        headers = {}
        headers[
            'User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
        url = searchUrl + filepath
        print(url)
        r = requests.get(url, headers=headers, allow_redirects=True)
        # async with aiohttp.ClientSession() as session: # discord.py asyncronous, so no reason this shouldnt be # nvm fucking doesnt work
        # r = await session.get(url, headers = headers, allow_redirects = True)
        print(r.url)
        soup = BeautifulSoup(r.content, "html.parser")
        # print(0)
        # print(await r.text("utf-8"))
        # soup = BeautifulSoup(await r.text("utf-8"), "html.parser")
        # print(1)
        text = (''.join(s.findAll(text=True)) for s in soup.findAll('div'))

        # print(2)

        c = Counter((x.rstrip(punctuation).casefold() for y in text for x in y.split()))
        # print(3)
        pokehashes = self.getpokemonnames()
        for i, j in c.most_common():
            print(i)
            if i in pokehashes:  # not really pokehashes, just a name of all pokemen
                result = i
                return (result)

        # no pokemon has been found, this should never trigger (in theory)
        return None

    def getpokemonnames(self):

        # dynamic, auto updating
        link = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_name"
        get = requests.get(link)
        soup = BeautifulSoup(get.content, features="html.parser")

        return [
            unidecode(x.getText()).casefold()
            # removes non ascii characters, also casefolds for case insensitive matching
            for x in soup.find_all("a")
            if x.has_attr("href") and x.has_attr("title") and "(Pokémon)" in x["title"]
        ]
