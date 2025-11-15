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

startNewCuntshitter()