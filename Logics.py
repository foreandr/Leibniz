from Sets import Set

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