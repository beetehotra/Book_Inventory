import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz
import json as js
import time
from objdict import ObjDict
from Book_Operations import *
from helper_functions import *


### --- GENERATE THE DYNAMIC INVENTORY FROM JSON --- ###

with open("Inventory.json", "r") as Inv:
    Inv_str = Inv.read()
    Inv_Dict = js.loads(Inv_str)
    #Inv_oDict = ObjDict(Inv_Dict)



### --- MAIN MANAGER FUNCTION --- ###

def manager():
    print(60*"-") 
    print(60*"-") 
    print("")
    print("Please select one of the following options :")
    print("")
    print("1 : Add a book")
    print("2 : Update a book")
    print("3 : Get full list")
    print("4 : Search for a book")
    print("5 : Delete a book")
    print("6 : Exit")
    print("")


    while True:
        try:
            choice = int(input("Please enter an integer (1-6) : "))
            if (choice <= 6) and (choice >= 1):
                break
            else:
                raise ValueError
        except:
            print("Please enter a valid input.")



    # Add a book
    if choice == 1:
        book_obj = create_book()
        
        if book_obj == None:
            pass
        else:
            book_id = gen_acro(book_obj.name) + "_" + gen_acro(book_obj.author)
            Inv_Dict[book_id] = ObjDict(book_obj.__dict__)
    
            update_inventory()
            print("")
            print("Book : '" + book_obj.name + "' by " + book_obj.author + " added to inventory.")
        
        print("")
        print(60*"-") 
        print(60*"-") 
        time.sleep(1)

        main_menu()



    # Update a book
    if choice == 2:
        print("")
        print("NOT YET IMPLEMENTED.")
        print("")
        print(60*"-") 
        print(60*"-") 
        print("")
        time.sleep(1)

        main_menu()



    # Get full list
    if choice == 3:
        print("")
        time.sleep(1)
        print("")
        get_full_list()
        print("")
        print(60*"-") 
        print(60*"-") 
        print("")
        time.sleep(1)

        main_menu()



    # Search a book
    if choice == 4:
        print("")
        time.sleep(1)
        print("")
        search_book()
        print(60*"-") 
        print(60*"-") 
        print("")
        time.sleep(1)

        main_menu()



    # Delete a book
    if choice == 5:
        print("")
        time.sleep(1)
        print("")
        delete_book()
        update_inventory()
        print("")
        print(60*"-") 
        print(60*"-") 
        print("")
        time.sleep(1)

        main_menu()



    # Exit
    if choice == 6:
        print("")
        exit_inventory()





### --- EXIT INVENTORY FUNCTION --- ###

def exit_inventory():
    update_inventory()
    print("Bye!")
    print("")
    time.sleep(1)




### --- GET FULL LIST FUNCTION --- ###

def get_full_list():
    with open("Inventory.json", "r") as Inv:
        Inv_str = Inv.read()
        Inv_Dict = js.loads(Inv_str)
    
    print("1. Get human readable list (Title, author)")
    print("2. Get full json data.")
    print("3. Save to dataframe format.")
    print("")

    while True:
        try:
            choice_data = int(input("Please enter an integer (1-3) : "))
            if (choice_data <= 3) and (choice_data >= 1):
                break
            else:
                raise ValueError
        except:
            print("Please enter a valid input.")

    print("")
    time.sleep(1)

    if choice_data == 2:
        Inv_str_formatted = js.dumps(Inv_Dict, indent=4)
        print(Inv_str_formatted)
        print("")
        time.sleep(1)
    elif choice_data == 3:
        with open("Inventory.df", "w") as Inv_df:
            print(pd.DataFrame.from_dict(Inv_Dict, orient='index'), file=Inv_df)
        print("A dataframe file of the inventory has been saved to 'Inventory.df'.")
        time.sleep(1)
    else:
        with open("Inventory.txt", "w") as Inv_txt:
            print(100*"-")
            print("{:<5} {:<60} {:<30}".format('INDEX', 'NAME', 'AUTHOR'))
            print(100*"-")
            print("")
       
            print(100*"-", file=Inv_txt)
            print("{:<5} {:<60} {:<30}".format('INDEX', 'NAME', 'AUTHOR'), file=Inv_txt)
            print(100*"-", file=Inv_txt)
            print("", file=Inv_txt)

            i = 1
            for book in Inv_Dict.keys():
                print("{:<5} {:<60} {:<30}".format(i, Inv_Dict[book]['name'], Inv_Dict[book]['author']))
                print("")
                print("{:<5} {:<60} {:<30}".format(i, Inv_Dict[book]['name'], Inv_Dict[book]['author']),file=Inv_txt)
                print("", file=Inv_txt)
                i += 1
              
            print(100*"-")
            print(100*"-", file=Inv_txt)
            

        print("")
        print("A text file of the inventory has been saved to 'Inventory.txt'.")
        print("")
        time.sleep(1)




### --- UPDATE INVENTORY FUNCTION --- ###

def update_inventory():
    sorted_Inv_str = js.dumps({k: Inv_Dict[k] for k in sorted(Inv_Dict)})
    with open("Inventory.json", "w") as Inv:
        print(sorted_Inv_str, file=Inv)




### --- RETURN TO MAIN MENU --- ###
def main_menu():
    print("Do you want to continue editing the inventory ?")
    print("")
    print("Press Enter to continue editing")
    print("Type 'x' to exit")
    print("")

    while True:
        try:
            choice3 = str(input("Please press Enter or type 'x' : "))
            if choice3 in ["", "x"]:
                break
            else:
                raise ValueError
        except:
            print("Please enter a valid input.")
    
    print("")

    if choice3 == "":
        time.sleep(1)
        manager()
    else:
        exit_inventory()




### --- DELETE A BOOK --- ###
def delete_book():
    title_str = str(input("Type a few characters in the beginning of the title of the book you want to delete : "))

    matchlist = []

    for bookitem in Inv_Dict.keys():
        #print(Inv_Dict[bookitem]['name'][:len(title_str)])
        if fuzz.ratio(title_str, Inv_Dict[bookitem]['name'][:len(title_str)]) > 70:
            matchlist.append(bookitem)

    time.sleep(1)

    if len(matchlist) == 0:
        print("There is no book starting with '" + title_str + "'")

    elif len(matchlist) == 1:
        print("")
        print("There is 1 book starting with '" + title_str + "'")
        print("")

        print("Are you certain you want to delete '" + Inv_Dict[matchlist[0]]['name'] + "' by " + Inv_Dict[matchlist[0]]['author'] + "?")
        
        time.sleep(1)

        print("")
        confirmation = str(input("Type 'DELETE' to confirm : "))
        print("")

        if confirmation == "DELETE":
            print(matchlist[0])
            Inv_Dict.pop(matchlist[0])
            print(Inv_Dict)
            print("Deleted.")
        else:
            print("Deletion aborted.")


    else:
        print("")
        print("Here is the list of books starting with '" + title_str + "'") 
        print("")
        print("{:<5} {:<60} {:<30}".format("NO.", "NAME", "AUTHOR"))

        counter = 1
        for item in matchlist:
            print("{:<5} {:<60} {:<30}".format(counter, Inv_Dict[item]['name'], Inv_Dict[item]['author']))
            counter +=1

        print("")
        
        time.sleep(1)
        delete_number = int(input("Please enter the number of the book you want to delete : "))
        print("")

        print("Are you certain you want to delete '" + Inv_Dict[matchlist[delete_number-1]]['name'] + "' by " + Inv_Dict[matchlist[delete_number-1]]['author'] + "?")
        
        print("")
        confirmation = str(input("Type 'DELETE' to confirm : "))
        print("")

        time.sleep(1)
        if confirmation == "DELETE":
            Inv_Dict.pop(matchlist[delete_number-1])
            print("Deleted.")
        else:
            print("Deletion aborted.")




### --- SEARCH FOR A BOOK --- ###
def search_book():
    title_str = str(input("Type a few characters in the beginning of the title of the book you want to search for : "))

    matchlist = []

    for bookitem in Inv_Dict.keys():
        #print(Inv_Dict[bookitem]['name'][:len(title_str)])
        if fuzz.ratio(title_str, Inv_Dict[bookitem]['name'][:len(title_str)]) > 70:
            matchlist.append(bookitem)

    time.sleep(1)

    if len(matchlist) == 0:
        print("There is no book starting with '" + title_str + "'")

    elif len(matchlist) == 1:
        print("")
        print("There is 1 book starting with '" + title_str + "'")
        print("")
        print("{:<5} {:<60} {:<30}".format("NO.", "NAME", "AUTHOR"))
        
        while True:
            try:
                detailed = str(input("Do you want to see detailed json data? (Y/N) : "))
                if detailed in ["Y", "N"]:
                    break
                else:
                    raise ValueError
            except:
                print("Please enter a valid input.")

        if detailed == "Y":
            matchdict = {}
            for bookitem in matchlist:
                matchdict[bookitem] = Inv_Dict[bookitem]
            matchdict_formatted = js.dumps(matchdict, indent=4)
            print(matchdict_formatted)
            print("")
            time.sleep(1)
        else:
            pass
    
    else:
        print("")
        print("Here is the list of books starting with '" + title_str + "'") 
        print("")
        print("{:<5} {:<60} {:<30}".format("NO.", "NAME", "AUTHOR"))

        counter = 1
        for bookitem in matchlist:
            print("{:<5} {:<60} {:<30}".format(counter, Inv_Dict[bookitem]['name'], Inv_Dict[bookitem]['author']))
            counter +=1

        print("")
        while True:
            try:
                detailed = str(input("Do you want to see detailed json data? (Y/N) : "))
                if detailed in ["Y", "N"]:
                    break
                else:
                    raise ValueError
            except:
                print("Please enter a valid input.")

        if detailed == "Y":
            matchdict = {}
            for bookitem in matchlist:
                matchdict[bookitem] = Inv_Dict[bookitem]
            matchdict_formatted = js.dumps(matchdict, indent=4)
            print(matchdict_formatted)
            print("")
            time.sleep(1)
        else:
            pass
