import string
import random as ra


def id_generator(
    size=16, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
):
    return "".join(ra.choice(chars) for _ in range(size))


def addUser(
    username,
    data,
    health=100,
    level=0,
    items=eval("{" + "}"),
    friends=[],
):
    truthy = True
    if not ("players" in data):
        data["players"] = {}
    else:
        for i in data["players"]:
            if data["players"][i]["username"] == username:
                truthy = False
    if truthy:
        id = id_generator()
        while id in data["players"]:
            id = id_generator()
        data["players"][id] = {
            "username": username,
            "health": health,
            "level": level,
            "items": items,
            "friends": friends,
        }
