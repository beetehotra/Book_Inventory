import Inventory_Management_Functions as InvMan
import time

print("")
print("Welcome to inventory management.")
print("")
time.sleep(1)

try:
    with open("Inventory.json", "x") as Inv:
        print("New inventory file created!")
except FileExistsError:
    print("Inventory File already exists.")

print("")
time.sleep(1)

InvMan.manager()
