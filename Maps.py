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