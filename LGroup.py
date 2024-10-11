class Group:
    def __init__(self, set_object, operation):
        """Initialize a Group with elements and a binary operation."""
        self.core_elements = set_object.core_elements  # Core elements of the group
        self.global_elements = set_object.global_elements  # Larger set for closure testing
        self.operation = operation

    def is_closed_under(self):
        """Check if the core set is closed under the binary operation with respect to the global set."""
        failed_pairs = []
        for a in self.core_elements:
            for b in self.core_elements:
                if self.operation(a, b) not in self.global_elements:
                    failed_pairs.append((a, b))
        return len(failed_pairs) == 0, failed_pairs

    def has_identity(self):
        """Check if there is an identity element in the core set."""
        for e in self.core_elements:
            if all(self.operation(e, x) == x and self.operation(x, e) == x for x in self.core_elements):
                return True, e
        return False, None

    def has_inverses(self):
        """Check if every element has an inverse in the core set under the operation."""
        identity = self.identity_element()
        failed_elements = []
        for a in self.core_elements:
            if not any(self.operation(a, b) == identity for b in self.core_elements):
                failed_elements.append(a)
        return len(failed_elements) == 0, failed_elements

    def is_associative(self):
        """Check if the binary operation is associative on the core set."""
        failed_triples = []
        for a in self.core_elements:
            for b in self.core_elements:
                for c in self.core_elements:
                    if self.operation(self.operation(a, b), c) != self.operation(a, self.operation(b, c)):
                        failed_triples.append((a, b, c))
        return len(failed_triples) == 0, failed_triples

    def identity_element(self):
        """Find and return the identity element in the core set, if it exists."""
        for e in self.core_elements:
            if all(self.operation(e, x) == x and self.operation(x, e) == x for x in self.core_elements):
                return e
        return None

    def is_group(self):
        """Check if the set forms a group under the defined operation for core elements with respect to global closure."""
        failed_checks = []

        # Check Closure with respect to the global set
        is_closed, failed_closure = self.is_closed_under()
        if not is_closed:
            failed_checks.append(f"Not closed under operation with respect to global set for pairs: {failed_closure}")

        # Check Associativity on core elements
        is_assoc, failed_assoc = self.is_associative()
        if not is_assoc:
            failed_checks.append(f"Fails associativity for element triples: {failed_assoc}")

        # Check Identity on core elements
        has_id, identity = self.has_identity()
        if not has_id:
            failed_checks.append("No identity element in core set")

        # Check Inverses on core elements
        has_inverses, failed_inverses = self.has_inverses()
        if not has_inverses:
            failed_checks.append(f"No inverses for elements in core set: {failed_inverses}")

        if failed_checks:
            return False, f"Fails: {', '.join(failed_checks)}"

        return True, f"Core set satisfies all group axioms with identity element: {identity}"


# Example operations
def addition(x, y):
    return x + y

# Usage example
from L_Set import integers  # Import the 'integers' Set from L_Set

# Create a Group object using the core set of integers with the addition operation
group_example = Group(integers, addition)
group_status, message = group_example.is_group()

print(f"Group Status: {group_status}")
print(f"Message: {message}")
