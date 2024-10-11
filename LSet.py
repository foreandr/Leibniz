from fractions import Fraction
from itertools import chain, combinations
import numpy as np

class Set:
    def __init__(self, core_elements, global_elements=None, enforce_uniqueness=True):
        """
        Initialize the Set with core elements and optionally global elements.
        
        core_elements: A list of elements representing the main/core set.
        global_elements: A larger set for extended testing. If None, it defaults to the core elements.
        enforce_uniqueness: Ensure elements are unique.
        """
        # Store core elements
        self.core_elements = self._create_unique_set(core_elements, enforce_uniqueness)
        
        # Store global elements or use the core elements if global is not provided
        self.global_elements = self._create_unique_set(global_elements if global_elements else core_elements, enforce_uniqueness)
        
        # Default to using core elements as the active set
        self.elements = self.core_elements

    def _create_unique_set(self, elements, enforce_uniqueness):
        """Helper function to create a set with unique elements."""
        unique_elements = []  # Track unique elements manually
        seen = set()  # Track elements already encountered

        for element in elements:
            if element in seen:
                if enforce_uniqueness:
                    pass  # Skip duplicates without raising an error
            else:
                unique_elements.append(element)
                seen.add(element)

        return set(unique_elements)  # Store only unique elements

    def switch_to_global(self):
        """Switch the active set to global elements."""
        self.elements = self.global_elements

    def switch_to_core(self):
        """Switch the active set back to core elements."""
        self.elements = self.core_elements

    def issubset(self, other):
        """Check if this set is a subset of another set."""
        return self.elements.issubset(other.elements)

    def issuperset(self, other):
        """Check if this set is a superset of another set."""
        return self.elements.issuperset(other.elements)

    def __iter__(self):
        """Return an iterator over the elements in the active Set."""
        return iter(self.elements)

    def __getitem__(self, index):
        """Enable index-based access to the Set elements."""
        return list(self.elements)[index]

    def __eq__(self, other):
        """Check if two Sets are equal based on their elements."""
        return self.elements == other.elements

    def __hash__(self):
        """Hash the set based on its elements to support use in collections like dictionaries."""
        return hash(frozenset(self.elements))

    def __repr__(self):
        """String representation of the custom Set."""
        return f"Set([len:{len(self.core_elements)}] - Core: {list(self.core_elements)[:5]}..., Global Size: {len(self.global_elements)})"

    def __contains__(self, element):
        """Check if an element is in the active Set."""
        return element in self.elements

    def __len__(self):
        """Return the number of elements in the active Set."""
        return len(self.elements)


# Empty Set
empty_set = Set([], [])

# Natural Numbers
natural_numbers = Set(list(range(1, 101)), list(range(1, 2501)))

# Integers
integers = Set(list(range(-50, 51)), list(range(-1250, 1251)))
integers_even = Set(list(range(-100, 101, 2)), list(range(-2500, 2501, 2)))

# Rational Numbers
#rational_numbers = Set(
#    [Fraction(p, q) for p in range(-10, 11) for q in range(1, 11) if q != 0],
#    [Fraction(p, q) for p in range(-50, 51) for q in range(1, 51) if q != 0]
#)

# Real Numbers
real_numbers = Set(
    [round(x * 0.01, 2) for x in range(-20, 21)], 
    [round(x * 0.01, 4) for x in range(-250, 251)]
)

# Complex Numbers
complex_numbers = Set(
    [complex(r, i) for r in range(-10, 11) for i in range(-10, 11)],
    [complex(r, i) for r in range(-50, 51) for i in range(-50, 51)]
)

# Irrational Numbers
irrational_numbers = Set(
    [round(2**0.5 * i, 2) for i in range(1, 11)] +
    [round(3.14159 * i, 2) for i in range(1, 11)] +
    [round(2.71828 * i, 2) for i in range(1, 11)],

    [round(2**0.5 * i, 2) for i in range(1, 2501)] +
    [round(3.14159 * i, 2) for i in range(1, 2501)] +
    [round(2.71828 * i, 2) for i in range(1, 2501)]
)

# Algebraic Numbers
algebraic_numbers = Set(
    [round(x**0.5, 2) for x in range(1, 21)] + [round(x**(1/3), 2) for x in range(1, 21)],
    [round(x**0.5, 2) for x in range(1, 1251)] + [round(x**(1/3), 2) for x in range(1, 1251)]
)

# Transcendental Numbers
transcendental_numbers = Set(
    [round(3.14159 * i, 2) for i in range(1, 51)] + [round(2.71828 * i, 2) for i in range(1, 51)],
    [round(3.14159 * i, 2) for i in range(1, 2501)] + [round(2.71828 * i, 2) for i in range(1, 2501)]
)

# Prime Numbers
prime_numbers = Set(
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],
    [x for x in range(2, 1251) if all(x % d != 0 for d in range(2, int(x**0.5) + 1))]
)

# Even Numbers
natural_even_numbers = Set(list(range(2, 101, 2)), list(range(2, 2501, 2)))
natural_numbers_with_0 = Set(list(range(0, 101, 2)), list(range(0, 2501, 2)))



# Odd Numbers
odd_numbers = Set(list(range(1, 100, 2)), list(range(1, 2500, 2)))

# Pauli Spinors
pauli_spinors = Set([(1, 0), (0, 1), (1, 1), (-1, 1)], [(1, 0), (0, 1), (1, 1), (-1, 1)])

# Dirac Spinors
dirac_spinors = Set(
    [tuple(np.random.randn(4) + 1j * np.random.randn(4)) for _ in range(20)], 
    [tuple(np.random.randn(4) + 1j * np.random.randn(4)) for _ in range(2500)]
)

# Vectors in 2D, 3D, and 4D space
vectors_2d = Set([tuple(np.random.randint(-50, 50, 2)) for _ in range(100)],
                 [tuple(np.random.randint(-250, 250, 2)) for _ in range(2500)])

vectors_3d = Set(
    [tuple(round(np.random.uniform(-10, 10), 2) for _ in range(3)) for _ in range(10)],
    [tuple(round(np.random.uniform(-250, 250), 2) for _ in range(3)) for _ in range(2500)]
)

vectors_4d = Set([tuple(np.random.randint(-50, 50, 4)) for _ in range(100)],
                 [tuple(np.random.randint(-250, 250, 4)) for _ in range(2500)])

# Spacetime Points
spacetime_points = Set(
    [tuple(np.random.randint(-50, 50, 4)) for _ in range(100)], 
    [tuple(np.random.randint(-250, 250, 4)) for _ in range(2500)]
)