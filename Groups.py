from Sets import Set

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
