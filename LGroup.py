import LOperations
from LOperations import apply_operation  # Import from your operations file
import LSet 
import time


class Group:
    def __init__(self, elements, operation):
        """Initialize a Group with core and global elements and a binary operation."""
        self.core_elements = elements.core_elements  # Core subset
        self.global_elements = elements.global_elements  # Full global set
        self.operation = operation
        self.identity = self._find_identity()  # Find identity element during initialization

    def is_closed_under(self):
        """
        Closure Property: Check if the set is closed under the binary operation.
        A set is closed under an operation if performing the operation on any elements of the set results in an element still within the set.
        """
        failed_pairs = []
        for a in self.core_elements:
            for b in self.core_elements:
                if apply_operation(a, b, self.operation) not in self.global_elements:
                    failed_pairs.append((a, b))
        return len(failed_pairs) == 0, failed_pairs

    def _find_identity(self):
        """
        Identity Element: Look for an identity element.
        An identity element `e` satisfies: a * e = e * a = a for all elements `a` in the set.
        """
        for e in self.core_elements:
            if all(apply_operation(e, x, self.operation) == x and apply_operation(x, e, self.operation) == x for x in self.core_elements):
                return e
        return None

    def has_identity(self):
        """
        Identity Property: Check if there is an identity element.
        An identity element `e` leaves other elements unchanged when used with the group operation.
        """
        identity = self._find_identity()
        if identity is not None:
            return True, identity
        return False, None

    def has_inverses(self):
        """
        Inverses Property: Verify that every element has an inverse.
        An inverse element `b` for `a` satisfies: a * b = b * a = e, where `e` is the identity.
        """
        identity = self.identity
        if identity is None:
            return False, []
        failed_elements = []
        for a in self.core_elements:
            if not any(apply_operation(a, b, self.operation) == identity for b in self.core_elements):
                failed_elements.append(a)
        return len(failed_elements) == 0, failed_elements

    def is_associative(self):
        """
        Associativity Property: Check if the operation is associative.
        Associativity means the grouping of operations doesn't change the result: (a * b) * c = a * (b * c).
        """
        failed_triples = []
        for a in self.core_elements:
            for b in self.core_elements:
                for c in self.core_elements:
                    if apply_operation(apply_operation(a, b, self.operation), c, self.operation) != apply_operation(a, apply_operation(b, c, self.operation), self.operation):
                        failed_triples.append((a, b, c))
        return len(failed_triples) == 0, failed_triples

    def is_group(self):
        """Check if the set forms a group under the defined operation for both core and global sets."""
        core_result, core_message = self._check_group_properties()
        return core_result, core_message

    def _check_group_properties(self):
        """
        Check group properties (Closure, Associativity, Identity, and Inverses) for core elements against the global set.
        Tracks the time taken for each individual property check and displays it separately.
        """
        failed_checks = []
        failures = 0

        # --- Check Closure ---
        start_closure = time.time()
        is_closed, failed_closure = self.is_closed_under()
        end_closure = time.time()
        closure_time = end_closure - start_closure
        if not is_closed:
            failures += 1
            failed_checks.append(f"[failures:{failures}]: Not closed under operation for elements: [{len(failed_closure)}] {failed_closure[:5]}... (Closure Time: {closure_time:.4f} seconds)")

        # --- Check Associativity ---
        start_assoc = time.time()
        is_assoc, failed_assoc = self.is_associative()
        end_assoc = time.time()
        assoc_time = end_assoc - start_assoc
        if not is_assoc:
            failures += 1
            failed_checks.append(f"[failures:{failures}]: Fails associativity for element triples: [{len(failed_assoc)}] {failed_assoc[:5]}... (Associativity Time: {assoc_time:.4f} seconds)")

        # --- Check Identity ---
        start_identity = time.time()
        has_id, identity = self.has_identity()
        end_identity = time.time()
        identity_time = end_identity - start_identity
        if not has_id:
            failures += 1
            failed_checks.append(f"[failures:{failures}]: No identity element (Identity Check Time: {identity_time:.4f} seconds)")

        # --- Check Inverses ---
        start_inverse = time.time()
        has_inverses, failed_inverses = self.has_inverses()
        end_inverse = time.time()
        inverse_time = end_inverse - start_inverse
        if not has_inverses:
            failures += 1
            failed_checks.append(f"[failures:{failures}]: No inverses for elements: [{len(failed_inverses)}] {failed_inverses[:5]}... (Inverse Check Time: {inverse_time:.4f} seconds)")

        # Display individual timings for each property check
        timing_summary = (f"\nProperty Check Times:\n"
                          f"Closure Time: {closure_time:.4f} seconds\n"
                          f"Associativity Time: {assoc_time:.4f} seconds\n"
                          f"Identity Check Time: {identity_time:.4f} seconds\n"
                          f"Inverse Check Time: {inverse_time:.4f} seconds\n")

        if failed_checks:
            return False, f"Fails:\n{'\n'.join(failed_checks)}\n{timing_summary}"
        
        return True, f"This set satisfies all group axioms with identity element: {identity}.\n{timing_summary}"



# Test 1: Integers under Addition
#group_example1 = Group(LSet.integers, LOperations.addition)
#group_status1, message1 = group_example1.is_group()
#print(f"Group Status for Integers under Addition: {group_status1}")
#print(f"Message: {message1}\n")

# Test 2: Even Numbers under Addition
#group_example2 = Group(LSet.even_numbers, LOperations.addition)
#group_status2, message2 = group_example2.is_group()
#print(f"Group Status for Even Numbers under Addition: {group_status2}")
#print(f"Message: {message2}\n")

#group_example21 = Group(LSet.integers_even, LOperations.addition)
#group_status21, message21 = group_example21.is_group()
#print(f"Group Status for  under Addition: {group_status21}")
#print(f"Message: {message21}\n")

# Test 4: Real Numbers under Addition
group_example4 = Group(LSet.real_numbers, LOperations.addition)
group_status4, message4 = group_example4.is_group()
print(f"Group Status for Real Numbers under Addition: {group_status4}")
print(f"Message: {message4}\n")
exit()

# Test 5: Complex Numbers under Addition
group_example5 = Group(LSet.complex_numbers, LOperations.addition)
group_status5, message5 = group_example5.is_group()
print(f"Group Status for Complex Numbers under Addition: {group_status5}")
print(f"Message: {message5}\n")

# Test 6: Spinors under Addition
group_example6 = Group(LSet.spinors, LOperations.addition)
group_status6, message6 = group_example6.is_group()
print(f"Group Status for Spinors under Addition: {group_status6}")
print(f"Message: {message6}\n")

# Test 7: Dirac Spinors under Pauli Spinor Multiplication
group_example7 = Group(LSet.dirac_spinors, LOperations.dirac_spinor_multiplication)
group_status7, message7 = group_example7.is_group()
print(f"Group Status for Dirac Spinors under Pauli Spinor Multiplication: {group_status7}")
print(f"Message: {message7}\n")

# Test 8: Matrices under Matrix Multiplication (Pauli Spinors)
group_example8 = Group(LSet.pauli_spinors, LOperations.pauli_spinor_multiplication)
group_status8, message8 = group_example8.is_group()
print(f"Group Status for Pauli Spinors under Matrix Multiplication: {group_status8}")
print(f"Message: {message8}\n")

# Test 9: Spacetime Points under Vector Addition
group_example9 = Group(LSet.spacetime_points, LOperations.addition)
group_status9, message9 = group_example9.is_group()
print(f"Group Status for Spacetime Points under Vector Addition: {group_status9}")
print(f"Message: {message9}\n")
