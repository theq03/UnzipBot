import os


class Config:
    API_ID = int(os.environ.get("2572163", 0))  # Change 12345 to your API_ID
    API_HASH = os.environ.get("deede80ddff7842db6c90b5715635142", None)  # Change None to your API_HASH
    BOT_TOKEN = os.environ.get("1629412971:AAEdl1_xmnuR3dC3jZ3uW-kwlms9J19FmeE", None)  # Change None to your BOT_TOKEN
    OWNER_ID = int(os.environ.get("1292898087", 0))  # Change 0 to your OWNER_ID
    OWNER_NAME = os.environ.get("The Q", None)  # Change None to your OWNER_NAME

    # For Local Deploys edit above 5 lines.
    # Put your API_ID and OWNER_ID (without comma) and API_HASH,BOT_TOKEN n OWNER_NAME (with commas) below.
    # If got any problem ask in @MysteryBotsChat.
