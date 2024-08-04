from enum import Enum as _Enum

class RelationshipTypes(_Enum):
    SIBLING = "SIBLING"
    COUSIN = "COUSIN"

    MARRIED = "MARRIED"
    
    GREAT_GRANDPARENT = "GREAT_GRANDPARENT"
    GRANDPARENT = "GRANDPARENT"
    PARENT = "PARENT"

    GREAT_PIBLING = "GREAT_PIBLING"
    AUNT_UNCLE = "PIBLING" 

    CHILD = "CHILD"