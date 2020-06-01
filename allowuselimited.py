import os


def allowuselimited(userid, client):  #

    return userid in [x.id for x in client.get_guild(int(os.environ.get("Z8GUILD"))).members]
