class ChatTrigger: # base class for when someone say something bot say something else
	def __init__(self, name, triggers, dispatchTyping = True):
		self.name = name
		self.triggers = [i.casefold() for i in triggers] # so that links work
		self.dispatchTyping = dispatchTyping

		print(f"Loaded {self.name}") # 2020-05-04, imported from https://repl.it/@unknownkone/bot <3 old but gold. less powerful but super simple, elegant, and flexible code from january 2020
	
	def run(self, message, trigger, client):
		message.channel.send("default")


	def get_name(self):
		return self.name