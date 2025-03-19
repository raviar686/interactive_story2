from constants import COMMAND_STOP, COMMAND_INVENTORY, COMMAND_HELP
from inventory import show_inventory

def introduction():
    print("""This is my interactive story, 'Escape The Woods'. In it, you will embark on an adventure in the woods.
    You will make decisions that change the course of your journey.
    Please freely type 'help' to see your list of commands.
    If you ever want to quit, just type 'stop'. Good Luck!\n""")

def get_choice(prompt, options):
    while True:
        choice = input(prompt).strip().lower()
        if choice == COMMAND_STOP:
            print("You have chosen to leave. Goodbye!")
            exit()
        elif choice == COMMAND_INVENTORY:
            show_inventory()
        elif choice == COMMAND_HELP:
            print("\nHelp - List of Commands:")
            print("- 'stop' to quit the game.")
            print("- 'inventory' to view your current supplies.")
            print("- 'yes' or 'no' to answer yes/no questions.")
            print("- 'help' to view this list of commands again.")
            print("- Type your choice to proceed in the story.")
            print("\nUse these commands to navigate the game.")
        elif choice in options:
            return choice
        else:
            print("Invalid choice. Please try again.")
