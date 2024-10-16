from Rings import Ring

class SkewField(Ring):
    def __init__(self, binary_operations=None):
        super().__init__(binary_operations)

    def classify(self):
        """Classification for Skew Field (non-commutative Field)"""
        return "Skew Field / Division Ring"
    
class Field(Ring):
    def __init__(self, binary_operations=None):
        super().__init__(binary_operations)

    def classify(self):
        """Classify as Field if multiplication is commutative, otherwise fallback to Skew Field"""
        addition_op, multiplication_op = self.binary_operations

        # If multiplication is commutative, it's a proper Field
        if multiplication_op.commutativity:
            return "Field"
        else:
            # Return a SkewField classification if multiplication isn't commutative
            return SkewField(self.binary_operations).classify()