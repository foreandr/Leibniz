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

    def print_separator(self, case):
        print(f"\n==================== Test Case {case} ====================\n")

    def test_case_1_basic_set(self):
        """Test basic Set classification."""
        self.print_separator("1 (Basic Set)")
        start_time = time.time()
        classified_object1 = self.object1.classify()
        self.assertIsInstance(classified_object1, Set)  # Check if classified as Set
        end_time = time.time()
        print(f"Execution Time: {end_time - start_time:.6f} seconds")

    def test_case_2_group(self):
        """Test Group classification (Associative Non-Abelian Group)."""
        self.print_separator("2 (Group)")
        start_time = time.time()
        classified_object1 = self.object1.classify()

        if isinstance(classified_object1, Set):  # Ensure object is a Set
            op2 = BinaryOperation(closure=True, identity=True, associativity=True)
            classified_object1.set_binary_operations(op2)
            self.assertEqual(classified_object1.classify(), "Associative Non-Abelian Group")
        else:
            self.fail("Object is not classified as a Set, cannot add binary operations")

        end_time = time.time()
        print(f"Execution Time: {end_time - start_time:.6f} seconds")

    def test_case_3_abelian_group(self):
        """Test Abelian Group classification."""
        self.print_separator("3 (Abelian Group)")
        start_time = time.time()
        classified_object1 = self.object1.classify()

        if isinstance(classified_object1, Set):  # Ensure object is a Set
            op3 = BinaryOperation(closure=True, identity=True, associativity=True, commutativity=True)
            classified_object1.set_binary_operations(op3)
            self.assertEqual(classified_object1.classify(), "Associative Abelian Group")
        else:
            self.fail("Object is not classified as a Set, cannot add binary operations")

        end_time = time.time()
        print(f"Execution Time: {end_time - start_time:.6f} seconds")

    def test_case_4_non_abelian_group(self):
        """Test Non-Abelian Group classification."""
        self.print_separator("4 (Non-Abelian Group)")
        start_time = time.time()
        classified_object1 = self.object1.classify()

        if isinstance(classified_object1, Set):  # Ensure object is a Set
            op4 = BinaryOperation(closure=True, identity=True, associativity=True, commutativity=False)
            classified_object1.set_binary_operations(op4)
            self.assertEqual(classified_object1.classify(), "Associative Non-Abelian Group")
        else:
            self.fail("Object is not classified as a Set, cannot add binary operations")

        end_time = time.time()
        print(f"Execution Time: {end_time - start_time:.6f} seconds")

    def test_case_5_magma(self):
        """Test Magma classification."""
        self.print_separator("5 (Magma)")
        start_time = time.time()
        classified_object1 = self.object1.classify()

        if isinstance(classified_object1, Set):  # Ensure object is a Set
            op5 = BinaryOperation(closure=True, identity=False, associativity=False)
            classified_object1.set_binary_operations(op5)
            self.assertEqual(classified_object1.classify(), "Magma")
        else:
            self.fail("Object is not classified as a Set, cannot add binary operations")

        end_time = time.time()
        print(f"Execution Time: {end_time - start_time:.6f} seconds")

    def test_case_6_ring(self):
        """Test Ring classification."""
        self.print_separator("6 (Ring)")
        start_time = time.time()
        classified_object1 = self.object1.classify()

        if isinstance(classified_object1, Set):  # Ensure object is a Set
            addition_op = BinaryOperation(closure=True, identity=True, associativity=True, commutativity=True, invertibility=True)
            multiplication_op = BinaryOperation(closure=True, identity=True, associativity=True)
            classified_object1.set_binary_operations([addition_op, multiplication_op])
            self.assertEqual(classified_object1.classify(), "Ring")
        else:
            self.fail("Object is not classified as a Set, cannot add binary operations")

        end_time = time.time()
        print(f"Execution Time: {end_time - start_time:.6f} seconds")

    def test_case_7_division_ring(self):
        """Test Skew Field classification."""
        self.print_separator("7 (Skew Field)")
        start_time = time.time()
        classified_object1 = self.object1.classify()

        if isinstance(classified_object1, Set):  # Ensure object is a Set
            addition_op = BinaryOperation(closure=True, identity=True, associativity=True, commutativity=True, invertibility=True)
            multiplication_op_non_commutativity = BinaryOperation(closure=True, identity=True, associativity=True, commutativity=False, invertibility=True)
            classified_object1.set_binary_operations([addition_op, multiplication_op_non_commutativity])
            self.assertEqual(classified_object1.classify(), "Skew Field / Division Ring")
        else:
            self.fail("Object is not classified as a Set, cannot add binary operations")

        end_time = time.time()
        print(f"Execution Time: {end_time - start_time:.6f} seconds")

    def test_case_8_field(self):
        """Test Field classification."""
        self.print_separator("8 (Field)")
        start_time = time.time()
        classified_object1 = self.object1.classify()

        if isinstance(classified_object1, Set):  # Ensure object is a Set
            addition_op = BinaryOperation(closure=True, identity=True, associativity=True, commutativity=True, invertibility=True)
            multiplication_op_field = BinaryOperation(closure=True, identity=True, associativity=True, commutativity=True, invertibility=True)
            classified_object1.set_binary_operations([addition_op, multiplication_op_field])
            self.assertEqual(classified_object1.classify(), "Field")
        else:
            self.fail("Object is not classified as a Set, cannot add binary operations")

        end_time = time.time()
        print(f"Execution Time: {end_time - start_time:.6f} seconds")

if __name__ == '__main__':
    start = time.time()
    unittest.main(verbosity=2)
    end = time.time()
    print(f"\n==================== Total Execution Time: {end - start:.6f} seconds ====================")
