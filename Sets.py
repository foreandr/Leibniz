class Set:
    '''CLASSIFICATION OF SETS:
    equivalnece relationships
        - reflexivity
        - symmetry
        - transitivity

    set is infinite if it has a proper subset that is isopmorphic to a
        - countably infinite 
            isomorphic to Natural numbers
        uncountabley infinite
            - 

    clasification of spaces, and maps bvetween spaces
    a space is some set equipped wiht some structure

    MAP CLASS
        - structrue preserving maps?
        - INJECTIVE,SURJECTIV, BIJECTIVE

            a map is a relation from a set a to b, such that for every A in be there is one element in b   
        - injection?, eats 2 objects and produces a truth value

        map from A to B
            - A domain, B Target/ Range

    TWO SETS ARE ISOMPRHIC IF THERE EXISTS A BIJECTION FORM A TO BE (composition)
        - given 2 maps we can build a new map
            a->b
            b->c 
            a->c
        - associative, and range in one set, is adomain in other
        - need associative to define inverse map to idenitiy

    THE SET (PREIMAGE) of a set, is a subset of the target of the map

    '''
    def __init__(self, binary_operations=None):
        """Initialize the set with binary operations"""
        self.binary_operations = []
        self.set_binary_operations(binary_operations)

    def set_binary_operations(self, binary_operations):
        from  Maps import BinaryOperation
        
        """Assign binary operations to the set"""
        if binary_operations is None:
            self.binary_operations = []
        elif isinstance(binary_operations, list):
            self.binary_operations = binary_operations
        elif isinstance(binary_operations, BinaryOperation):
            self.binary_operations = [binary_operations]
        else:
            raise ValueError("Binary operations must be instances of BinaryOperation class or a list of them")

    def classify(self):
        """Classify the object and transform it based on its binary operations"""
        if not self.binary_operations:
            return self  # Remain a Set if no binary operations
        
        # If there are exactly two binary operations, classify as a Ring
        if len(self.binary_operations) == 2:
            addition_op, multiplication_op = self.binary_operations
            if addition_op.closure and addition_op.identity and addition_op.associativity and addition_op.commutativity and addition_op.invertibility:
                if multiplication_op.closure and multiplication_op.identity and multiplication_op.associativity:
                    from Rings import Ring
                    return Ring(self.binary_operations).classify()  # Recursively classify as a Ring
        
        # If there is exactly one binary operation, check if it's a Group
        elif len(self.binary_operations) == 1:
            op = self.binary_operations[0]
            if op.closure and op.identity and op.associativity:
                from Groups import Group
                return Group(self.binary_operations).classify()  # Recursively classify as a Group

        # If none of the above, classify as a Magma
        from Magmas import Magma
        return Magma(self.binary_operations).classify()

    def __str__(self):
        """String representation of the Set object"""
        if self.binary_operations:
            ops_descriptions = [str(op) for op in self.binary_operations]
            return f"Set with binary operations: {', '.join(ops_descriptions)}"
        else:
            return "Set with no binary operations"