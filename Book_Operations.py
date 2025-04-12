import numpy as np
import pandas as pd #creating and updating database
import json as js
from fuzzywuzzy import fuzz #for checking closeness of two strings
from Book import *


### --- ADD A BOOK --- ###

name = None
author = None
read = False
owned = False
lent = False
lent_to = None
borrowed_from = None

with open("Inventory.json", "r") as Inv:
    Inv_str = Inv.read()
    Inv_Dict = js.loads(Inv_str)





def create_book():

    name = str(input("Enter name of the book : "))
    author = str(input("Enter author's name : "))
    print("")

    match = "N"

    for bookitem in Inv_Dict.keys():
        if fuzz.ratio(name, Inv_Dict[bookitem]['name']) + fuzz.ratio(author, Inv_Dict[bookitem]['author']) >= 100:
            while True:
                try:
                    match = str(input("Is this the same book as '" + Inv_Dict[bookitem]['name'] + "' by " + Inv_Dict[bookitem]['author'] + "? (Y/N) : "))
                    if match in ["Y", "N"]:
                        break
                    else:
                        raise ValueError
                except:
                    print("Please enter a valid input.")
            if match == "Y":
                break
        else:
            pass

    print("")

    if match == "N":

        read = False
        while True:
            read_str = str(input("Is it read (T/F): "))

            if read_str == "T":
                read = True
                break
            elif read_str == "F":
                break
            else:
                print("Please enter 'T' or 'F'")

        owned = True
        while True:
            owned_str = str(input("Is it yours (T/F): "))

            if owned_str == "T":
                break
            elif owned_str == "F":
                owned = False
                break
            else:
                print("Please enter 'T' or 'F'")


        lent = False
        lent_to = None
        if owned == False:
            lent = None
        else:
            while True:
                lent_str = str(input("Have you lent it (T/F): "))
                if lent_str == "T":
                    lent = True
                    lent_to = str(input("To whom? : "))
                    break
                elif lent_str == "F":
                    break
                else:
                    print("Please enter 'T' or 'F'")

        borrowed_from = None
        if owned == True:
            borrowed_from = None
        else:
            borrowed_from = str(input("Whom have you borrowed it from: "))


        book_obj = book(name,author,read,owned,lent,lent_to,borrowed_from)
        return book_obj

    else:
        print("This book is already in the inventory.")


### --- Update a book --- ###
