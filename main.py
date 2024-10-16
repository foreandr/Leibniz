class Object:
    def __init__(self, axioms=None):
        """Initialize the object with a list of axioms (strings)"""
        self.axioms = axioms if axioms else []

    def classify(self):
        """Classify the object based on its axioms"""
        # Define the required axioms for classification as a set
        set_axioms = [
            "Axiom of Extensionality",
            "Axiom of Empty Set",
            "Axiom of Pairing",
            "Axiom of Union",
            "Axiom of Power Set",
            "Axiom of Infinity",
            "Axiom of Foundation"
        ]

        # Check if the object qualifies as a Set
        if all(axiom in self.axioms for axiom in set_axioms):
            return Set()  # Return a Set object
        
        # If it doesn't meet all set axioms, return it as an object with missing axioms
        missing_axioms = [axiom for axiom in set_axioms if axiom not in self.axioms]
        return f"Not a Set - Missing axioms: {missing_axioms}"

    def __str__(self):
        """String representation of the object and its axioms"""
        return f"Object with axioms: {', '.join(self.axioms)}"



class Set:
    '''CLASSIFICATION OF SETS:
    equivalnece relationsh

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
                    return Ring(self.binary_operations).classify()  # Recursively classify as a Ring
        
        # If there is exactly one binary operation, check if it's a Group
        elif len(self.binary_operations) == 1:
            op = self.binary_operations[0]
            if op.closure and op.identity and op.associativity:
                return Group(self.binary_operations).classify()  # Recursively classify as a Group

        # If none of the above, classify as a Magma
        return Magma(self.binary_operations).classify()

    def __str__(self):
        """String representation of the Set object"""
        if self.binary_operations:
            ops_descriptions = [str(op) for op in self.binary_operations]
            return f"Set with binary operations: {', '.join(ops_descriptions)}"
        else:
            return "Set with no binary operations"

class Ring(Set):
    def __init__(self, binary_operations=None):
        super().__init__(binary_operations)

    def classify(self):
        """Further classification for Ring if needed"""
        # Check if it qualifies as a Field
        addition_op, multiplication_op = self.binary_operations
        if addition_op.commutativity and multiplication_op.commutativity and multiplication_op.invertibility:
            return Field(self.binary_operations).classify()

        # Check if it qualifies as a Division Ring (non-commutativity multiplication)
        if multiplication_op.invertibility and multiplication_op.associativity:
            return DivisionRing(self.binary_operations).classify()

        return "Ring"

class Field(Ring):
    def __init__(self, binary_operations=None):
        super().__init__(binary_operations)

    def classify(self):
        """Terminal classification for Field"""
        return "Field"

class DivisionRing(Ring):
    def __init__(self, binary_operations=None):
        super().__init__(binary_operations)

    def classify(self):
        """Terminal classification for Division Ring (non-commutativity Field)"""
        return "Division Ring"

class Magma(Set):
    def __init__(self, binary_operations=None):
        super().__init__(binary_operations)

    def classify(self):
        """Terminal classification for Magma (no further properties to check)"""
        return "Magma"

class Group(Set):
    def __init__(self, binary_operations=None):
        super().__init__(binary_operations)

    def classify(self):
        """Further classify the Group based on additional group properties"""
        is_abelian = all(op.commutativity for op in self.binary_operations)
        if is_abelian:
            return AbelianGroup(self.binary_operations).classify()  # Recursively classify as an Abelian Group
        else:
            return NonAbelianGroup(self.binary_operations).classify()  # Recursively classify as a Non-Abelian Group

class AbelianGroup(Group):
    def __init__(self, binary_operations=None):
        super().__init__(binary_operations)

    def classify(self):
        """Classify AbelianGroup further into specific subtypes"""
        if all(op.invertibility for op in self.binary_operations):
            return "Cyclic Abelian Group"
        elif all(op.associativity for op in self.binary_operations):
            return "Associative Abelian Group"
        elif any(op.commutativity for op in self.binary_operations):
            return "Partially commutativity Abelian Group"
        else:
            return "General Abelian Group"

class NonAbelianGroup(Group):
    def __init__(self, binary_operations=None):
        super().__init__(binary_operations)

    def classify(self):
        """Classify NonAbelianGroup further into specific subtypes"""
        if any(op.invertibility for op in self.binary_operations):
            return "Symmetric Non-Abelian Group"
        elif any(op.associativity for op in self.binary_operations):
            return "Associative Non-Abelian Group"
        elif any(op.closure for op in self.binary_operations):
            return "Closure Non-Abelian Group"
        else:
            return "General Non-Abelian Group"

class BinaryOperation:
    def __init__(self, closure=True, identity=False, associativity=False, commutativity=False, invertibility=False):
        """Initialize the BinaryOperation with its axioms"""
        self.closure = closure
        self.identity = identity
        self.associativity = associativity
        self.commutativity = commutativity
        self.invertibility = invertibility

    def __str__(self):
        """String representation of the BinaryOperation object"""
        axioms = []
        if self.closure:
            axioms.append("Closure")
        if self.identity:
            axioms.append("Identity")
        if self.associativity:
            axioms.append("Associativity")
        if self.commutativity:
            axioms.append("Commutativity")
        if self.invertibility:
            axioms.append("Invertibility")
        return f"BinaryOperation with axioms: {', '.join(axioms)}" if axioms else "BinaryOperation with no axioms"


# Example usage:

# Case 1: An object with all ZFC set axioms (basic Set)
object1 = Object([
    "Axiom of Extensionality",
    "Axiom of Empty Set",
    "Axiom of Pairing",
    "Axiom of Union",
    "Axiom of Power Set",
    "Axiom of Infinity",
    "Axiom of Foundation"
])
classified_object1 = object1.classify()  # Will return a basic Set object
print("Case 1 (Basic Set):", classified_object1)
print("--")

# Case 2: Now equip the classified Set (object1) with one binary operation (Group classification)
op2 = BinaryOperation(closure=True, identity=True, associativity=True)
classified_object1.set_binary_operations(op2)
print("Case 2 (Group):", classified_object1.classify())  # Will recursively classify as a Group
print("--")

# Case 3: Equip the classified Set (object1) with a commutativity operation (Abelian Group)
op3 = BinaryOperation(closure=True, identity=True, associativity=True, commutativity=True)
classified_object1.set_binary_operations(op3)
print("Case 3 (Abelian Group):", classified_object1.classify())  # Will classify as an Abelian Group
print("--")

# Case 4: Equip the classified Set (object1) with a non-commutativity operation (Non-Abelian Group)
op4 = BinaryOperation(closure=True, identity=True, associativity=True, commutativity=False)
classified_object1.set_binary_operations(op4)
print("Case 4 (Non-Abelian Group):", classified_object1.classify())  # Will classify as Non-Abelian Group
print("--")

# Case 5: Equip the classified Set (object1) with two binary operations (Ring classification)
addition_op = BinaryOperation(closure=True, identity=True, associativity=True, commutativity=True, invertibility=True)
multiplication_op = BinaryOperation(closure=True, identity=True, associativity=True)
classified_object1.set_binary_operations([addition_op, multiplication_op])
print("Case 5 (Ring):", classified_object1.classify())  # Will classify as "Ring"
print("--")

# Case 6: Equip the classified Set (object1) with binary operations satisfying Field properties
multiplication_op_field = BinaryOperation(closure=True, identity=True, associativity=True, commutativity=True, invertibility=True)
classified_object1.set_binary_operations([addition_op, multiplication_op_field])
print("Case 6 (Field):", classified_object1.classify())  # Will classify as "Field"
print("--")

# Case 7: Equip the classified Set (object1) with non-commutativity multiplication (Division Ring)
multiplication_op_non_commutativity = BinaryOperation(closure=True, identity=True, associativity=True, commutativity=False, invertibility=True)
classified_object1.set_binary_operations([addition_op, multiplication_op_non_commutativity])
print("Case 7 (Division Ring):", classified_object1.classify())  # Will classify as "Division Ring"
print("--")

# Case 8: Equip the classified Set (object1) with multiple binary operations not satisfying Ring properties (Magma)
op5 = BinaryOperation(closure=True, identity=True, associativity=True)
op6 = BinaryOperation(closure=True, identity=True, associativity=True)
classified_object1.set_binary_operations([op5, op6])
print("Case 8 (Magma):", classified_object1.classify())  # Will classify as "Magma"
print("--")

# Case 9: An object with some missing ZFC axioms (not classified as a Set)
object2 = Object([
    "Axiom of Extensionality",
    "Axiom of Empty Set",
    "Axiom of Union"
])
classified_object2 = object2.classify()  # Will return "Not a Set"
print("Case 9 (Not a Set):", classified_object2)
print("--")