import constants

from simple_term_menu import TerminalMenu
import os

def getData():
    def createMenu(options):
        options.append("EXIT")
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(menu_entry_index)

        if (menu_entry_index == None) or (options[menu_entry_index] == "EXIT"):
            selected = "EXIT"
            print("Exiting...")
            exit()

        else:
            selected = options[menu_entry_index]
            print(f"You have selected {selected}.")
            return selected

    types = []
    for type in constants.RelationshipTypes:
        types.append(type.value)
    relationshipTypeSelected = constants.RelationshipTypes(createMenu(types))

getData()