class AutoAction:
	def __init__(self, name, triggerUponOwn = False, args = {}): # 2020-05-04 added args so that whoops wrong bot but ill keep it anyways
		self.name = name
		self.triggerUponOwn = triggerUponOwn

		print(f"Loaded {self.name}") # 2020-05-04, imported from https://repl.it/@unknownkone/bot <3 old but gold. less powerful but super simple, elegant, and flexible code from january 2020
	
	def run(self, message, client): # return false if non destructive
		return False
	