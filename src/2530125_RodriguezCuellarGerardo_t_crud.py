#                               TITLE PAGE
"""
    Title: CRUD in Python
    Student name: Gerardo Rodríguez Cuéllar
    Student ID: 2530125
    Group: 1-1
"""

#                           EXECUTIVE SUMMARY

"""
    This program implements a basic CRUD system 
    (Create, Read, Update, Delete) entirely in 
    memory using Python. A CRUD allows users to 
    add, view, modify, and remove items in a 
    structured data collection. For this assignment, 
    I chose to use a dictionary where each key 
    is an item_id and the value is another dictionary 
    containing name, price, and quantity. Using 
    functions keeps the code organized, avoids 
    repetition, and separates responsibilities 
    clearly. The program includes a main menu, 
    input validation, individual CRUD functions, 
    and a simple listing feature.
"""

#                       PROBLEM CRUD

""" 
    Description:
    This program manages a simple inventory in memory. It 
    allows the user to Create new items, Read an item by ID, 
    Update an item, Delete an item, and List all items. 
    It uses a main menu inside a loop.

    Inputs:
    - Menu option (0 to 5).
        - For Create/Update: ID, name, price, quantity.
        - For Read/Delete: ID.

    Outputs:
    - Success messages: "Item created", "Item updated", etc.
        - Error messages: "Item not found", "Error: invalid input".
        - A list of all items when requested.

    Validations:
    - Menu option must be 0-5.
        - ID cannot be empty.
        - Price must be float >= 0.
        - Quantity must be int >= 0.
        - Cannot create an item if the ID already exists.

    Test cases:
    1) Normal case:
        Action: Create item -> ID: "A1", Name: "Apple", Price: 10.5, Qty: 100
        Expected output:
        Item created

    2) Border case:
        Action: Create item -> ID: "B2", Name: "Dust", Price: 0.0, Qty: 0
        Expected output:
        Item created (0 is a valid number for price/qty)

    3) Error case:
        Action: Create item -> ID: "C3", Name: "Error", Price: "Five", Qty: 1
        Expected output:
        Error: invalid input
"""

print()
print("                     CRUD")
print()

#                   CODE

# Global dictionary to store items
# Key: item_id, Value: dict with name, price, quantity
inventory = {}

def create_item(item_id, name, price, quantity):
    if item_id in inventory:
        print("Error: ID already exists")
    else:
        inventory[item_id] = {"name": name, "price": price, "quantity": quantity}
        print("Item created")

def read_item(item_id):
    if item_id in inventory:
        item = inventory[item_id]
        print(f"Found: Name: {item['name']}, Price: {item['price']}, Qty: {item['quantity']}")
    else:
        print("Item not found")

def update_item(item_id, name, price, quantity):
    if item_id in inventory:
        inventory[item_id] = {"name": name, "price": price, "quantity": quantity}
        print("Item updated")
    else:
        print("Item not found")

def delete_item(item_id):
    if item_id in inventory:
        del inventory[item_id]
        print("Item deleted")
    else:
        print("Item not found")

def list_items():
    print("Items list:")
    if not inventory:
        print("  (Empty)")
    else:
        for key, val in inventory.items():
            print(f"  ID: {key} | Name: {val['name']} | Price: {val['price']} | Qty: {val['quantity']}")

# Main Program Loop
while True:
    print("\n--- Menu ---")
    print("1. Create item")
    print("2. Read item")
    print("3. Update item")
    print("4. Delete item")
    print("5. List items")
    print("0. Exit")
    print()
    
    option = input("Select option: ")

    if option == '0':
        print("Goodbye!")
        break

    elif option == '5':
        list_items()

    elif option == '1':
        # Create
        i_id = input("ID: ").strip()
        i_name = input("Name: ")
        i_price = input("Price: ")
        i_qty = input("Quantity: ")

        if i_id == "":
            print("Error: invalid input")
        else:
            try:
                price_f = float(i_price)
                qty_i = int(i_qty)
                if price_f >= 0 and qty_i >= 0:
                    create_item(i_id, i_name, price_f, qty_i)
                else:
                    print("Error: invalid input")
            except ValueError:
                print("Error: invalid input")

    elif option == '2':
        # Read
        i_id = input("ID to read: ").strip()
        if i_id:
            read_item(i_id)
        else:
            print("Error: invalid input")

    elif option == '3':
        # Update
        i_id = input("ID to update: ").strip()
        # Check existence first to avoid asking for data if not needed
        if i_id not in inventory:
             print("Item not found")
        else:
            i_name = input("New Name: ")
            i_price = input("New Price: ")
            i_qty = input("New Quantity: ")
            try:
                price_f = float(i_price)
                qty_i = int(i_qty)
                if price_f >= 0 and qty_i >= 0:
                    update_item(i_id, i_name, price_f, qty_i)
                else:
                    print("Error: invalid input")
            except ValueError:
                print("Error: invalid input")

    elif option == '4':
        # Delete
        i_id = input("ID to delete: ").strip()
        if i_id:
            delete_item(i_id)
        else:
             print("Error: invalid input")

    else:
        print("Error: invalid input")

#                           CONCLUSIONS

"""
    This program helped me understand how to structure 
    data using dictionaries in Python. I learned that 
    separating logic into functions makes the code easier 
    to read and debug. 
    
    Validating inputs is very important; using try-except 
    blocks prevents the program from crashing if the user 
    types text instead of numbers. This CRUD logic is the 
    base for many larger applications.
"""

#                           REFERENCES
"""
    1) https://docs.python.org/3/tutorial/datastructures.html
    2) https://www.w3schools.com/python/python_dictionaries.asp
    3) https://www.programiz.com/python-programming/function
"""