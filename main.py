import time
import os

def epsteinList():
    return [d for d in os.listdir("/Volumes") if d not in ("Macintosh HD",)]

alreadySeen = set(epsteinList())

print("waiting for drive to start the game")

while True:
    time.sleep(1)
    current_drives = set(epsteinList())
    new_drives = current_drives - alreadySeen
    if new_drives:
        usb_name = new_drives.pop()
        usb_path = f"/Volumes/{usb_name}"
        game_folder = os.path.join(usb_path, "taggie_data")
        os.makedirs(game_folder, exist_ok=True)
        print(f"Game started! USB {usb_name} detected.")
        with open(os.path.join(game_folder, ".taggie"), "w") as f:
            f.write("X")
        break
