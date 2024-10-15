import colors

class Set:
    def __init__(self, finite=False, infinite=False, countable=False, uncountable=False,
                 open=False, closed=False, compact=False,
                 singleton=False, empty=False, measurable=False, null_set=False):
        self.finite = finite
        self.infinite = infinite
        self.countable = countable
        self.uncountable = uncountable
        self.open = open
        self.closed = closed
        self.compact = compact
        self.singleton = singleton
        self.empty = empty
        self.measurable = measurable
        self.null_set = null_set

class Magma:
    def __init__(self, set_obj, operation, is_associative=False, has_identity=False):
        self.set_obj = set_obj  # Accepting a Set object
        self.operation = operation  # String representing the binary operation
        self.is_associative = is_associative  # Is the operation associative?
        self.has_identity = has_identity  # Does the magma have an identity element?

        # Check properties for magma
        if not self.is_associative:
            colors.c_print("THIS MUST HAVE AN ASSOCIATIVE OPERATION TO BE A MAGMA.", "red")
        if not self.has_identity:
            colors.c_print("THIS MUST HAVE AN IDENTITY ELEMENT TO BE A MAGMA.", "red")

class Group(Magma):
    def __init__(self, set_obj, operation, identity, inverse_function, 
                 abelian=False, cyclic=False, has_inverses=False):
        super().__init__(set_obj, operation, is_associative=True, has_identity=True)  # All groups are magmas
        self.identity = identity  # Identity element
        self.inverse_function = inverse_function  # String representing the inverse function
        self.abelian = abelian  # Is the group abelian?
        self.cyclic = cyclic  # Is the group cyclic?
        self.has_inverses = has_inverses  # Does the group have inverses for all elements?

        # Check properties for group
        if not self.has_inverses:
            colors.c_print("THIS MUST HAVE INVERSES FOR ALL ELEMENTS TO BE A GROUP.", "red")
        if not self.identity:
            colors.c_print("THIS MUST HAVE AN IDENTITY ELEMENT TO BE A GROUP.", "red")

class Ring:
    def __init__(self, set_obj, addition_operation, multiplication_operation,
                 has_additive_identity=False, has_multiplicative_identity=False,
                 is_commutative=False):
        self.set_obj = set_obj  # Accepting a Set object
        self.addition_operation = addition_operation  # String representing the addition operation
        self.multiplication_operation = multiplication_operation  # String representing the multiplication operation
        self.has_additive_identity = has_additive_identity  # Does the ring have an additive identity?
        self.has_multiplicative_identity = has_multiplicative_identity  # Does the ring have a multiplicative identity?
        self.is_commutative = is_commutative  # Is the ring commutative?

        # Check properties for ring
        if not self.has_additive_identity:
            colors.c_print("THIS MUST HAVE AN ADDITIVE IDENTITY TO BE A RING", "red")
        if not self.is_commutative:
            colors.c_print("THIS MUST BE COMMUTATIVE UNDER MULTIPLICATION TO BE A RING.", "red")

class Field(Ring):  # Field inherits from Ring
    def __init__(self, ring_obj):  # Take an instance of Ring
        super().__init__(ring_obj.set_obj, ring_obj.addition_operation, ring_obj.multiplication_operation,
                         has_additive_identity=True,
                         has_multiplicative_identity=True,
                         is_commutative=True)

        # Check properties for field
        if not ring_obj.has_multiplicative_identity:
            colors.c_print("A FIELD MUST HAVE A MULTIPLICATIVE IDENTITY.", "red")
        if not ring_obj.has_additive_identity:
            colors.c_print("A FIELD MUST HAVE AN ADDITIVE IDENTITY.", "red")
        if not ring_obj.is_commutative:
            colors.c_print("A FIELD MUST BE COMMUTATIVE UNDER MULTIPLICATION.", "red")

class Space(Field):  # Space inherits from Field
    def __init__(self, field_obj, dimension=None, is_finite=True, is_infinite=False):
        super().__init__(field_obj)  # Call the Field constructor
        self.dimension = dimension  # Dimension of the space (None for infinite dimensions)
        self.is_finite = is_finite  # Is the space finite?
        self.is_infinite = is_infinite  # Is the space infinite?

class VectorSpace(Space):  # VectorSpace inherits from Space
    def __init__(self, space_obj):
        super().__init__(space_obj)  # Call the Space constructor

# Example usage:

# Create a finite set for a ring
set_Z4 = Set(finite=True)

# Step 1: Define operations for addition and multiplication
addition_operation = "addition modulo 4"
multiplication_operation = "multiplication modulo 4"

# Step 2: Create a ring
ring_Z4 = Ring(set_obj=set_Z4,
                addition_operation=addition_operation,
                multiplication_operation=multiplication_operation,
                has_additive_identity=True,
                has_multiplicative_identity=True,  # This ring does not have a multiplicative identity
                is_commutative=True)

# Step 3: Create a field from the ring
field_F = Field(ring_obj=ring_Z4)

# Step 4: Create a space from the field
space1 = Space(field_obj=field_F, dimension=3, is_finite=True)

# Step 5: Create a vector space from the space
vector_space_R3 = VectorSpace(space_obj=space1)

# Display results
print("\nRing Z_4 Properties:")
print("Is finite:", ring_Z4.set_obj.finite)              # True
print("Addition operation:", ring_Z4.addition_operation)   # "addition modulo 4"
print("Multiplication operation:", ring_Z4.multiplication_operation) # "multiplication modulo 4"
print("Has additive identity:", ring_Z4.has_additive_identity)  # True
print("Has multiplicative identity:", ring_Z4.has_multiplicative_identity)  # False
print("Is commutative:", ring_Z4.is_commutative)        # True

print("\nField F Properties:")
print("Is finite:", field_F.set_obj.finite)              # True
print("Addition operation:", field_F.addition_operation)   # "addition modulo 4"
print("Multiplication operation:", field_F.multiplication_operation) # "multiplication modulo 4"
print("Has additive identity:", field_F.has_additive_identity)  # True
print("Has multiplicative identity:", field_F.has_multiplicative_identity)  # True
print("Is commutative:", field_F.is_commutative)        # True

print("\nSpace Properties:")
print("Dimension:", space1.dimension)          # 3
print("Is Finite:", space1.is_finite)          # True
print("Has Additive Identity:", space1.has_additive_identity)  # True
print("Has Multiplicative Identity:", space1.has_multiplicative_identity)  # True

print("\nVector Space Properties:")
print("Dimension:", vector_space_R3.dimension)          # 3
print("Is Finite:", vector_space_R3.is_finite)          # True
print("Has Additive Identity:", vector_space_R3.has_additive_identity)  # True
print("Has Multiplicative Identity:", vector_space_R3.has_multiplicative_identity)  # True
