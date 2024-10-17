from Sets import Set, Subset, PowerSet

class Topology(Set):
    def __init__(self):
        """
        Topology class that inherits from Set.
        :param subsets: The collection of subsets forming the topology.
        """
        super().__init__()

    def classify(self):
        """
        Classify the Topology.
        """
        return "This is a valid topology."

pset = PowerSet()  # Create a PowerSet
subset = Subset(pset, 
                has_parent_set=True, 
                has_empty_set=True, 
                topology_intersection_axiom=True, 
                topology_union_axiom=True
                )  # Create a Subset of the PowerSet

top = subset.classify()
# Print the Subset object
print(subset)
print(top)