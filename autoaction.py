class AutoAction:
	def __init__(self, name, triggerUponOwn = False):
		self.name = name
		self.triggerUponOwn = triggerUponOwn
	
	def run(self, message, client): # return false if non destructive
		return False
	