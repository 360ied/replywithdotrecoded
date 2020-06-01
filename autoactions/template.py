import autoaction


class Template(autoaction.AutoAction):

    async def run(self, message, client):
        print("do something")
