import discord

import chattrigger


class ChatTriggersHelpCommand(chattrigger.ChatTrigger):

    def __init__(self, name, triggers, chattriggers, dispatchTyping=True):
        self.name = name
        self.triggers = [i.casefold() for i in triggers]  # so that links work
        self.chattriggers = chattriggers
        self.dispatchTyping = dispatchTyping

    async def run(self, message, trigger, client):
        emdescription = ""
        partcount = 1
        for i in self.chattriggers:
            toadd = f"{i.name}: {' | '.join(i.triggers)}\n"
            if len(emdescription) + len(toadd) > 2048:
                embed = discord.Embed(title=f"Help Command Part {partcount}", description=emdescription,
                                      colour=discord.Colour.gold())
                await message.channel.send(embed=embed)
                emdescription = ""
                partcount += 1
            emdescription += toadd
        embed = discord.Embed(title=f"Help Command Part {partcount}", description=emdescription,
                              colour=discord.Colour.gold())
        await message.channel.send(embed=embed)
