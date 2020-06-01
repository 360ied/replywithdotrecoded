class OnMemberJoinTask:
    def __init__(self, name):
        self.name = name

        print(
            f"Loaded {self.name}")  # 2020-05-04, imported from https://repl.it/@unknownkone/bot <3 old but gold. less powerful but super simple, elegant, and flexible code from january 2020

    def run(self, member, client):  # return false if non destructive
        return False
