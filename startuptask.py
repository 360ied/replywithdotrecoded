class StartUpTask:
	def __init__(self, name):
		self.name = name
	
	def run(self, client): # return false if non destructive
		return False
	