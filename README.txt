---------------------------------------------
BOOK INVENTORY MANAGEMENT SYSTEM
---------------------------------------------

An inventory management system for collection of books.

Before getting started, this system relies on the python packages numpy,
pandas, objdict, fuzzywuzzy, and python-levenshtein. Install these packages by running the
followin commands.

$pip install numpy
$pip install pandas
$pip install objdict
$pip install fuzzywuzzy
$pip install python-levenshtein

This is required only once.

---------------------------------------------

Once the dependencies are taken care of, the system is ready to be used.

Run the 'edit_inventory.py' file to get started.

$python edit_inventory.py

It supports addition, alteration, and deletion of books, and has option to
provide a list of the books.

The system automatically updates the 'Inventory.json' file each time it is
altered. To update the 'Inventory.txt' file, select the 'Get all files' option
(option 3) in main menu, and then ask for Human readable formal (option 2) in
the following menu.

---------------------------------------------

Book.py : Introduces the book class

Book_Operations.py : Defines the functions to create and alter book objects.

Inventory_Management_Functions.py : defines the functions for adding and
altering the inventory.

helper_functions.py : Some helper functions like acronym generator, distance
between two strings etc.

---------------------------------------------

