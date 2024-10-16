class Set:
    def __init__(self, binary_operations=None):
        """Initialize the set with binary operations"""
        self.binary_operations = []
        self.set_binary_operations(binary_operations)

    def set_binary_operations(self, binary_operations):
        """Assign binary operations to the set"""
        if binary_operations is None:
            self.binary_operations = []
        elif isinstance(binary_operations, BinaryOperation):
            self.binary_operations = [binary_operations]
        elif isinstance(binary_operations, list):
            self.binary_operations = binary_operations
        else:
            raise ValueError("Binary operations must be instances of BinaryOperation class or a list of them")

    def classify(self):
        """Classify the object and transform it recursively until a final type is returned"""
        if not self.binary_operations:
            return "Set"  # Terminal classification as a basic Set
        
        # Check if it's a Group (must have one binary operation with closure, identity, and associativity)
        if len(self.binary_operations) == 1:
            op = self.binary_operations[0]
            if op.closure and op.identity and op.associativity:
                return Group(self.binary_operations).classify()  # Recursively classify the Group
        
        # If it has multiple operations or doesn't meet group axioms, it's a Magma
        return Magma(self.binary_operations).classify()  # Recursively classify the Magma

    def __str__(self):
        """String representation of the Set object"""
        if self.binary_operations:
            ops_descriptions = [str(op) for op in self.binary_operations]
            return f"Object with binary operations: {', '.join(ops_descriptions)}"
        else:
            return "Object with no binary operations"

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
            return "Abelian Group"  # Terminal classification for Abelian Group
        else:
            return "Non-Abelian Group"  # Terminal classification for Non-Abelian Group

# `BinaryOperation` Class for reference:
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

# Case 1: A magma (no mandatory axioms)
op1 = BinaryOperation(closure=True)
object1 = Set(op1)
print(object1.classify())  # Will recursively classify as "Magma"

# Case 2: A group (must satisfy closure, identity, and associativity)
op2 = BinaryOperation(closure=True, identity=True, associativity=True, commutativity=True)
object2 = Set(op2)
print(object2.classify())  # Will recursively classify as "Abelian Group"

# Case 3: A non-abelian group
op3 = BinaryOperation(closure=True, identity=True, associativity=True, commutativity=False)
object3 = Set(op3)
print(object3.classify())  # Will recursively classify as "Non-Abelian Group"

# Case 4: A set with no operations
object4 = Set()
print(object4.classify())  # Will classify as "Set"

# Case 5: A set with multiple binary operations (cannot be a group)
op4 = BinaryOperation(closure=True, identity=True, associativity=True)
op5 = BinaryOperation(closure=True, identity=True, associativity=True)
object5 = Set([op4, op5])
print(object5.classify())  # Will classify as "Magma" because there are multiple operations
