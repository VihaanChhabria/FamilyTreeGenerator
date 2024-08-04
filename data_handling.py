import os

from simple_term_menu import TerminalMenu

import constants


def getData():
    def askData():
        def createMenu(options):
            options.append("EXIT")
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()
            if (menu_entry_index == None):
                selected = "EXIT"
            else:
                selected = options[menu_entry_index]
            return selected
            
        
        types = []
        for type in constants.RelationshipTypes:
            types.append(type.value)
        relationshipTypeSelected = createMenu(types)
        done = False
        if relationshipTypeSelected == "EXIT":
            done = True
            return {
                    "relationship" : None, 
                    "person1" : None, 
                    "person2" : None
                }, done
        else:
            relationshipTypeSelected = constants.RelationshipTypes(relationshipTypeSelected)
            person1Selected = input("Select who is person 1 in the relationship. (person 1 is the 'relationship' to person 2): ")
            person2Selected = input("Select who is person 2 in the relationship. (person 1 is the 'relationship' to person 2): ")

            return {
                    "relationship" : relationshipTypeSelected, 
                    "person1" : person1Selected, 
                    "person2" : person2Selected
                }, done
    
    relationships = []
    done = False
    while not done:
        data, done = askData()
        relationships.append(data)
        os.system("cls || clear")

    print(relationships)

getData()