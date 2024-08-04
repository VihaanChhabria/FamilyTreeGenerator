from enum import Enum as _Enum

class RelationshipTypes(_Enum):
    SIBLING = "Sibling"
    COUSIN = "Cousin"

    MARRIED = "Married"
    
    GREAT_GRANDPARENT = "Great Grandparent"
    GRANDPARENT = "Grandparent"
    PARENT = "Parent"

    GREAT_PIBLING = "Great Pibling"
    AUNT_UNCLE = "Pibling" 

    CHILD = "Child"