inventory = {}  # Dictionary to store inventory items (name as key, quantity as value)

def add_item(name, quantity):
  """Adds an item to the inventory.

  Args:
    name: The name of the item.
    quantity: The quantity of the item to add.
  """
  if name in inventory:
    inventory[name] += quantity
  else:
    inventory[name] = quantity
  print(f"Added {quantity} {name} to inventory.")

def update_item(name, quantity):
  """Updates the quantity of an existing item in the inventory.

  Args:
    name: The name of the item to update.
    quantity: The new quantity for the item.
  """
  if name in inventory:
    inventory[name] = quantity
    print(f"Updated {name} quantity to {quantity}.")
  else:
    print(f"{name} not found in inventory.")

def search_item(name):
  """Searches for an item in the inventory and displays its information.

  Args:
    name: The name of the item to search for.
  """
  if name in inventory:
    print(f"{name}: {inventory[name]}")
  else:
    print(f"{name} not found in inventory.")

def list_inventory():
  """Prints a list of all items in the inventory with their names and quantities."""
  if inventory:
    print("Inventory:")
    for item, quantity in inventory.items():
      print(f"{item}: {quantity}")
  else:
    print("Inventory is empty.")

while True:
  # Display menu options
  print("\nInventory System")
  print("1. Add item")
  print("2. Update item quantity")
  print("3. Search for item")
  print("4. List inventory")
  print("5. Exit")

  # Get user choice
  choice = input("Enter your choice (1-5): ")

  # Handle user choice
  if choice == '1':
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    add_item(name, quantity)
  elif choice == '2':
    name = input("Enter item name to update: ")
    quantity = int(input("Enter new quantity: "))
    update_item(name, quantity)
  elif choice == '3':
    name = input("Enter item name to search: ")
    search_item(name)
  elif choice == '4':
    list_inventory()
  elif choice == '5':
    print("Exiting inventory system.")
    break
  else:
    print("Invalid choice. Please enter a number between 1 and 5.")
