class OnMemberJoinTask:
	def __init__(self, name):
		self.name = name
	
	def run(self, member, client): # return false if non destructive
		return False
	