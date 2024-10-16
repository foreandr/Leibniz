from Sets import Set

class Magma(Set):
    def __init__(self, binary_operations=None):
        super().__init__(binary_operations)

    def classify(self):
        """Terminal classification for Magma (no further properties to check)"""
        return "Magma"