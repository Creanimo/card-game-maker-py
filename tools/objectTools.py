import shortuuid

def generateID() -> str:
    return str(shortuuid.uuid())