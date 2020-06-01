import asyncio
import itertools
import os
# from random import randint
import time
import traceback

import aiohttp

import startuptask


class MinehutNotification(startuptask.StartUpTask):

    async def run(self, client):
        notifchannel = client.get_channel(int(os.environ.get("MINEHUT_NOTIFICATION_CHANNEL_ID")))
        servers = [x.split(".")[0] for x in os.environ.get("MINEHUT_SERVERS").split(",")]
        print(servers[0])
        # await notifchannel.send("start")
        print(servers)
        delay = 90

        wasonline = [False] * len(servers)

        lastonlineiteration = [-2] * len(servers)

        async with aiohttp.ClientSession() as session:
            # print(1)
            # while not await asyncio.sleep(delay):
            for citeration in itertools.count():  # current iteration

                await asyncio.sleep(delay)

                # print(2)
                try:
                    get = await session.get("https://api.minehut.com/servers")
                    response = await get.json()

                    cservs = response["servers"]
                    # print(3)

                    for i in cservs:

                        # print(4)

                        if i["name"] in servers:

                            # print(5)

                            if not i[
                                       "status"] == "ONLINE":  # prob not needed as only online servers are shown in the serverlist anyways
                                continue

                            servname = i["name"]

                            servindex = servers.index(servname)

                            print(f"CIteration: {citeration}")
                            print(f"LOIteration: {lastonlineiteration[servindex]}")

                            print(f"EEEEEEE: {citeration - lastonlineiteration[servindex]}")
                            if citeration - lastonlineiteration[servindex] != 1:
                                await notifchannel.send(
                                    f"<@{os.environ.get('OWNER_ID')}>, {servname}.minehut.gg just started!")

                            lastonlineiteration[servindex] = citeration

                            wasonline[servindex] = True

                            startedat = i["startedAt"]  # seconds since epoch

                            startedat /= 1000

                            ctime = time.time()

                            ptime = ctime - startedat  # passed time
                            # print(f"ctime: {ctime}")
                            # print(f"startedat: {startedat}")
                            # print(f"ptime: {ptime}")

                            players = sorted(i["players"])

                            await notifchannel.send(
                                f"{servname}.minehut.gg is currently online! Online for: {ptime // 3600} hours, {ptime % 3600 // 60} minutes, {ptime % 60 // 1} seconds.\n{len(players)} online players: {', '.join(players)}")

                except:

                    # traceback.print_exc()
                    await notifchannel.send(f"**Error!**\n{traceback.format_exc()}")
