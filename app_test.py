import unittest
import time
from Rings import *
from Groups import *
from Magmas import *
from Maps import *
from Sets import *
from Fields import *
from Logics import *

class TestClassification(unittest.TestCase):

    def setUp(self):
        self.object1 = Object([
            "Axiom of Extensionality",
            "Axiom of Empty Set",
            "Axiom of Pairing",
            "Axiom of Union",
            "Axiom of Power Set",
            "Axiom of Infinity",
            "Axiom of Foundation"
        ])

    def test_case_1_basic_set(self):
        """Test basic Set classification."""
        start_time = time.time()
        classified_object1 = self.object1.classify()
        self.assertIsInstance(classified_object1, Set)  # Check if classified as Set
        end_time = time.time()
        print(f"Test Case 1 (Basic Set): {end_time - start_time:.6f} seconds")

    def test_case_2_group(self):
        """Test Group classification only for Set objects."""
        start_time = time.time()
        classified_object1 = self.object1.classify()

        if isinstance(classified_object1, Set):  # Ensure object is a Set
            # Now add binary operations since it's classified as a Set
            op2 = BinaryOperation(closure=True, identity=True, associativity=True)
            # Assuming the set_binary_operations method exists on Set objects
            classified_object1.set_binary_operations(op2)
            self.assertEqual(classified_object1.classify(), "Associative Non-Abelian Group")
        else:
            self.fail("Object is not classified as a Set, cannot add binary operations")

        end_time = time.time()
        print(f"Test Case 2 (Group): {end_time - start_time:.6f} seconds")

    def test_case_not_a_set_should_fail_to_add_operations(self):
        """Test that binary operations cannot be added to non-Set objects."""
        start_time = time.time()
        object2 = Object([
            "Axiom of Extensionality",
            "Axiom of Empty Set",
            "Axiom of Union"
        ])
        classified_object2 = object2.classify()

        if not isinstance(classified_object2, Set):  # Object is not a Set
            with self.assertRaises(AttributeError):  # Expect failure when trying to add binary operations
                classified_object2.set_binary_operations(BinaryOperation(closure=True, identity=True, associativity=True))
        else:
            self.fail("Object classified as a Set, test case expects failure")

        end_time = time.time()
        print(f"Test Case (Not a Set - should fail to add operations): {end_time - start_time:.6f} seconds")

    def test_case_9_not_a_set(self):
        """Test object missing ZFC axioms (not classified as a Set)."""
        start_time = time.time()
        object2 = Object([
            "Axiom of Extensionality",
            "Axiom of Empty Set",
            "Axiom of Union"
        ])
        classified_object2 = object2.classify()
        expected_message = "Not a Set - Missing axioms: ['Axiom of Pairing', 'Axiom of Power Set', 'Axiom of Infinity', 'Axiom of Foundation']"
        self.assertEqual(classified_object2, expected_message)
        end_time = time.time()
        print(f"Test Case 9 (Not a Set): {end_time - start_time:.6f} seconds")


if __name__ == '__main__':
    start = time.time()
    unittest.main(verbosity=2)
    end = time.time()
    print(f"\nTotal Execution Time: {end - start:.6f} seconds")
