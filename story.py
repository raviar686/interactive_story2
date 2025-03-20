from utils import get_choice
from inventory import add_item, remove_item, show_inventory
import random

def start_adventure():
    print("As you enter the woods, you see three paths. Which do you choose?")
    choice = get_choice("Path 1, 2, or 3: ", ["1", "2", "3"])

    if choice == "1":
        tunnel_path()
    elif choice == "2":
        house_path()
    else:
        bridge_path()

def tunnel_path():
    print("\nYou have chosen the straight path.")
    print("As you continue, you see a dark tunnel that may be a shortcut.")
    choice = get_choice("Do you wish to go through the tunnel? (yes/no): ", ["yes", "no"])

    if choice == "yes":
        print("You step into the tunnel, and begin your trek through the long dark tunnel...")
        blocked_path()
    else:
        print("You decide to take the safer route around the tunnel.")
        print("The path gets hilly, but after descending the last hill, you exit the forest!!")
        around_tunnel_choice()


