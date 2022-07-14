from lib import greet

def handler(event = {}, context = {}):
    return greet(event.get("name") or "SociVolta")