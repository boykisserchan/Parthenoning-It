# from getmac import get_mac_address as gma
# mac = gma()
# print(mac)


import dotenv
import airtable
import socket
import time

def findHost(timeout=1):
    socky = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socky.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socky.bind(("", port))