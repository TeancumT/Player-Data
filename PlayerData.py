import string
import random as ra
import json


def id_generator(
    size=16, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
):
    return "".join(ra.choice(chars) for _ in range(size))


def add_user(
    username,
    data,
    health=100,
    level=0,
    items=eval("{" + "}"),
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
        }


if __name__ == "__main__":
    data = {}
    add_user("Tim", data)
    add_user("Joe", data)
    add_user("James", data)
    add_user("GreenDog", data)
    print(json.dumps(data, indent=4, sort_keys=True))
