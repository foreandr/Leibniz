from Rings import Ring

class Field(Ring):
    def __init__(self, binary_operations=None):
        super().__init__(binary_operations)

    def classify(self):
        """Terminal classification for Field"""
        return "Field"