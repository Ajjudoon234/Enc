import hashlib

CREATOR = "@CREATIVEYDV"
BotCode = "fc9dc7b267c90ad8c07501172bc15e0f10b2eb572b088096fb8cc9b196caea97"

def verify():
    current_hash = hashlib.sha256(CREATOR.encode()).hexdigest()
    if current_hash != BotCode:
        raise Exception("File verification failed. Unauthorized use.")
