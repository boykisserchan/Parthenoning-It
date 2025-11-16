from getmac import get_mac_address as gma
mac = gma()
# print(mac)


import dotenv
import os
from pyairtable import Table, Api
import socket
import time

dotenv.load_dotenv()

key = os.getenv("SHIT")
id = os.getenv("TBID")
tbl = os.getenv("TBNM")

api = Api(key)
table = api.table(id, tbl)

def startNewCuntshitter():
    table.create({"MAC A":mac})

def checkForGame():
    records = table.all()

    for i in records:
        if i["fields"].get("MAC A") is not None:
            if i["fields"].get("MAC A") == mac:
                #TODO: stop games happening from that device.
                pass
            elif i["fields"].get("MAC A") :


# startNewCuntshitter()