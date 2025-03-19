inventory = ["food", "knife", "first aid kit"]

def add_item(item):
    inventory.append(item)
    print(f"You received: {item}!")

def remove_item(item):
    if item in inventory:
        inventory.remove(item)
        print(f"You lost your {item}!")
    else:
        print(f"You don't have {item} to lose.")

def show_inventory():
    if inventory:
        print("\nYour current supplies: " + ", ".join(inventory))
    else:
        print("\nYou have no supplies left!")
