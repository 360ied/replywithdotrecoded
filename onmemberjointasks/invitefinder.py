import onmemberjointask

class InviteFinder(onmemberjointask.OnMemberJoinTask):

	async def run(self, member, client):
		print("do something") # i have decided to simply add the InviteManager bot to do this for me, unfortunately, the InviteManager bot is a bloated mess that WONT SHUT UP
		# an implementation of this would most likely be quite resource intensive and would have to be loaded upon a seperate bot dedicated to the job