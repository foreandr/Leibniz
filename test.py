import colors

class Set:
    def __init__(self, finite=False):
        self.finite = finite

class Magma:
    def __init__(self, set_obj, operation, is_associative=False, has_identity=False):
        self.set_obj = set_obj
        self.operation = operation
        self.is_associative = is_associative
        self.has_identity = has_identity

        self.classify()

    def classify(self):
        if self.is_associative and self.has_identity:
            self.__class__ = Group
            self.classify_as_group()

    def classify_as_group(self):
        print("This object is now classified as a Group")

class Group(Magma):
    def __init__(self, set_obj, operation, is_abelian=False, is_cyclic=False, has_inverses=False,
                 identity=True):
        super().__init__(set_obj, operation, is_associative=True, has_identity=identity)
        self.is_abelian = is_abelian
        self.is_cyclic = is_cyclic
        self.has_inverses = has_inverses

        self.classify_as_specific_group()

    def classify_as_specific_group(self):
        if self.is_abelian:
            self.__class__ = AbelianGroup
        elif self.is_cyclic and not self.is_abelian:
            self.__class__ = CyclicNonAbelianGroup

        print(f"This group is classified as a {self.__class__.__name__}")

class AbelianGroup(Group):
    def __init__(self, set_obj, operation, identity=True, is_finite=True, is_cyclic=False):
        super().__init__(set_obj, operation, is_abelian=True, identity=identity)
        self.is_finite = is_finite
        self.is_cyclic = is_cyclic

        self.classify_sub_abelian()

    def classify_sub_abelian(self):
        if self.is_finite:
            self.__class__ = FiniteAbelianGroup
        if self.is_cyclic:
            self.__class__ = CyclicAbelianGroup

        print(f"Abelian group is now classified as {self.__class__.__name__}")

class FiniteAbelianGroup(AbelianGroup):
    def __init__(self, set_obj, operation, identity=True):
        super().__init__(set_obj, operation, identity=identity, is_finite=True)
        print("This is a Finite Abelian Group")

class CyclicAbelianGroup(AbelianGroup):
    def __init__(self, set_obj, operation, identity=True):
        super().__init__(set_obj, operation, identity=identity, is_finite=True, is_cyclic=True)
        print("This is a Cyclic Abelian Group")

class CyclicNonAbelianGroup(Group):
    def __init__(self, set_obj, operation, identity=True, is_finite=False, is_simple=False):
        super().__init__(set_obj, operation, is_cyclic=True, is_abelian=False, identity=identity)
        self.is_finite = is_finite
        self.is_simple = is_simple

        self.classify_cyclic_nonabelian()

    def classify_cyclic_nonabelian(self):
        if self.is_finite and self.is_simple:
            self.__class__ = FiniteSimpleCyclicNonAbelianGroup
        elif not self.is_finite and self.is_simple:
            self.__class__ = InfiniteSimpleCyclicNonAbelianGroup
        elif self.is_finite and not self.is_simple:
            self.__class__ = FiniteCyclicNonAbelianGroup
        elif not self.is_finite and not self.is_simple:
            self.__class__ = InfiniteCyclicNonAbelianGroup

        print(f"This group is classified as {self.__class__.__name__}")

# Subclass for finite, simple cyclic non-Abelian group
class FiniteSimpleCyclicNonAbelianGroup(CyclicNonAbelianGroup):
    def __init__(self, set_obj, operation, identity=True):
        super().__init__(set_obj, operation, identity=identity, is_finite=True, is_simple=True)
        print("This is a Finite Simple Cyclic Non-Abelian Group")

# Subclass for infinite, simple cyclic non-Abelian group
class InfiniteSimpleCyclicNonAbelianGroup(CyclicNonAbelianGroup):
    def __init__(self, set_obj, operation, identity=True):
        super().__init__(set_obj, operation, identity=identity, is_finite=False, is_simple=True)
        print("This is an Infinite Simple Cyclic Non-Abelian Group")

# Subclass for finite, non-simple cyclic non-Abelian group
class FiniteCyclicNonAbelianGroup(CyclicNonAbelianGroup):
    def __init__(self, set_obj, operation, identity=True):
        super().__init__(set_obj, operation, identity=identity, is_finite=True, is_simple=False)
        print("This is a Finite Cyclic Non-Abelian Group")

# Subclass for infinite, non-simple cyclic non-Abelian group
class InfiniteCyclicNonAbelianGroup(CyclicNonAbelianGroup):
    def __init__(self, set_obj, operation, identity=True):
        super().__init__(set_obj, operation, identity=identity, is_finite=False, is_simple=False)
        print("This is an Infinite Cyclic Non-Abelian Group")

# Example Usage

# Create a finite set object
finite_set = Set(finite=True)

# Create a general magma that will classify into different groups
magma_example1 = Magma(set_obj=finite_set, operation="addition", is_associative=True, has_identity=True)
print(f"Current class after promotion: {magma_example1.__class__.__name__}")  # This should output "Group"
print("--\n")

# Create an Abelian Group, it should further classify as finite and/or cyclic
abelian_group = AbelianGroup(set_obj=finite_set, operation="addition")
print(f"Current class: {abelian_group.__class__.__name__}")  # This should output "FiniteAbelianGroup"
print("--\n")

# Create a Cyclic Abelian Group
cyclic_abelian_group = CyclicAbelianGroup(set_obj=finite_set, operation="multiplication")
print(f"Current class: {cyclic_abelian_group.__class__.__name__}")  # This should output "CyclicAbelianGroup"
print("--\n")

# Create a finite, simple cyclic non-Abelian group
finite_simple_cyclic_nonabelian = CyclicNonAbelianGroup(set_obj=finite_set, operation="non-commutative operation", is_finite=True, is_simple=True)
print(f"Current class: {finite_simple_cyclic_nonabelian.__class__.__name__}")  # Output: FiniteSimpleCyclicNonAbelianGroup
print("--\n")

# Create an infinite, simple cyclic non-Abelian group
infinite_simple_cyclic_nonabelian = CyclicNonAbelianGroup(set_obj=finite_set, operation="non-commutative operation", is_finite=False, is_simple=True)
print(f"Current class: {infinite_simple_cyclic_nonabelian.__class__.__name__}")  # Output: InfiniteSimpleCyclicNonAbelianGroup
print("--\n")

# Create a finite, non-simple cyclic non-Abelian group
finite_nonsimple_cyclic_nonabelian = CyclicNonAbelianGroup(set_obj=finite_set, operation="non-commutative operation", is_finite=True, is_simple=False)
print(f"Current class: {finite_nonsimple_cyclic_nonabelian.__class__.__name__}")  # Output: FiniteCyclicNonAbelianGroup
print("--\n")

# Create an infinite, non-simple cyclic non-Abelian group
infinite_nonsimple_cyclic_nonabelian = CyclicNonAbelianGroup(set_obj=finite_set, operation="non-commutative operation", is_finite=False, is_simple=False)
print(f"Current class: {infinite_nonsimple_cyclic_nonabelian.__class__.__name__}")  # Output: InfiniteCyclicNonAbelianGroup
print("--\n")