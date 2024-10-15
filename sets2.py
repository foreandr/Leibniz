from axioms import *

# 1. Singleton Set
singleton_set = [
    Axiom_of_Pairing, 
    Axiom_of_Extensionality
]

# 2. Empty Set
empty_set = [
    Axiom_of_Extensionality, 
    Axiom_of_Empty_Set
]

# 3. Union of Sets
union_set = [
    Axiom_of_Union, 
    Axiom_of_Extensionality
]

# 4. Power Set
power_set = [
    Axiom_of_Power_Set, 
    Axiom_of_Extensionality
]

# 5. Ordered Pair
ordered_pair = [
    Axiom_of_Pairing, 
    Axiom_of_Extensionality
]

# 6. Cartesian Product
cartesian_product = [
    Axiom_of_Pairing, 
    Axiom_of_Union
]

# 7. Natural Numbers (ℕ)
natural_numbers = [
    Axiom_of_Infinity, 
    Axiom_of_Foundation, 
    Axiom_of_Extensionality
]

# 8. Rational Numbers (ℚ)
rational_numbers = [
    Axiom_of_Pairing, 
    Axiom_of_Union, 
    Axiom_of_Replacement
]

complex_numbers = [
    Axiom_of_Pairing, 
    Axiom_of_Power_Set, 
    Axiom_of_Replacement, 
    Axiom_of_Infinity
]

vector_space = [
    Axiom_of_Pairing, 
    Axiom_of_Union, 
    Axiom_of_Power_Set
]

# 9. Real Numbers (ℝ)
real_numbers = [
    Axiom_of_Infinity, 
    Axiom_of_Power_Set, 
    Axiom_of_Replacement
]

# 10. Transfinite Ordinals
ordinals = [
    Axiom_of_Infinity, 
    Axiom_of_Replacement, 
    Axiom_of_Choice
]

# 11. Cardinal Numbers
cardinal_numbers = [
    Axiom_of_Power_Set, 
    Axiom_of_Replacement, 
    Axiom_of_Choice
]

# 12. Class
class_definition = [
    Axiom_of_Class_Comprehension, 
    Axiom_of_Extensionality
]

# 13. Tarski’s Universe
tarski_universe = [
    Axiom_of_Tarski_Universe, 
    Axiom_of_Infinity
]
