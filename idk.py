import time
import os

print("skibidi")

def epsteinList():
    return [d for d in os.listdir("/Volumes") if d not in ("Macintosh HD",)]


def blegh():
    alreadySeen = set(epsteinList())

    while True:
        time.sleep(1)
        current_drives = set(epsteinList())
        new_drives = current_drives - alreadySeen
        if new_drives:
            try:
                usb_name = new_drives.pop()
                usb_path = f"/Volumes/{usb_name}"
                game_folder = os.path.join(usb_path, "taggie_data")
                os.makedirs(game_folder, exist_ok=True)
                print(f"{usb_name} detected.")

                if open(os.path.join(game_folder, ".taggie"), "rt").read() == "X":
                    print("yay")
                    print("deleting file")
                    os.remove(os.path.join(game_folder, ".taggie"))
                    return True
                else:
                    print("kms")
            except FileNotFoundError:
                print("kmser")
            except PermissionError:
                print("fuckass")


blegh()