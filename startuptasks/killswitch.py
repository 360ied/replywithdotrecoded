import startuptask
import persistentstorage
import os
import sys

class KillSwitch(startuptask.StartUpTask):

	async def run(self, client):
		killswitchchannelid = int(os.environ.get("KILL_SWITCH_CHANNEL_ID"))
		reader = persistentstorage.PersistentStorage("KillSwitchReader", killswitchchannelid, client, ".")
		ksstr = (await reader.read())[0] # shortened
		#ksstr = ksstr[0] # to avoid the courotine error
		if ksstr:
			print("Kill Switch Activated!")
			await client.get_channel(int(os.environ.get("LOG_CHANNEL"))).send("Kill Switch Activated, Shutting Down...")
			sys.exit(0)
		else:
			print("Kill Switch is not Activated")