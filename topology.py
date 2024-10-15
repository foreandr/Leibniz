from axioms import *
from sets2 import *  # Import the sets

# 1. Trivial Topology on the Empty Set
trivial_topology_empty = empty_set + [
    logic_axioms["Existential Generalization"],  # Ensures empty set and whole set exist
    logic_axioms["Non-Contradiction"]           # No contradictions between the two open sets
]

# 2. Discrete Topology on the Natural Numbers (ℕ)
discrete_topology_natural_numbers = natural_numbers + [
    logic_axioms["Universal Instantiation"],    # Every subset of ℕ is open
    logic_axioms["Existential Generalization"], # All subsets exist as open sets
    logic_axioms["Conjunction"]                 # Ensures logical consistency for all subsets
]

# 3. Standard Topology on the Real Numbers (ℝ)
standard_topology_real_numbers = real_numbers + [
    logic_axioms["Existential Generalization"],  # Open intervals (a, b) exist
    logic_axioms["Universal Generalization"],    # Union of open sets is open
    logic_axioms["Implication"],                 # Finite intersection of open sets is open
    logic_axioms["Conjunction"]                  # Ensures logical consistency of the open sets
]

# 4. Cofinite Topology on Rational Numbers (ℚ)
cofinite_topology_rational_numbers = rational_numbers + [
    logic_axioms["Existential Generalization"], # Open sets have finite complements
    logic_axioms["Universal Generalization"],   # Universally applies the finite complement rule
    logic_axioms["Negation Introduction"]       # Ensures finite complements are open
]

# 5. Product Topology on Cartesian Product (ℝ × ℝ)
product_topology_cartesian_product = cartesian_product + [
    logic_axioms["Existential Generalization"], # Ensures open sets on ℝ × ℝ exist
    logic_axioms["Conjunction"],                # Combines open sets from both dimensions
    logic_axioms["Universal Generalization"]    # Applies universally for products
]

# 6. Subspace Topology on Real Numbers (Subset of ℝ)
subspace_topology_real_numbers = real_numbers + [
    logic_axioms["Existential Generalization"], # Open sets are intersections with ℝ
    logic_axioms["Conjunction"],                # Ensures intersection logic holds
    logic_axioms["Universal Generalization"]    # Applies to all subsets
]

# 7. Zariski Topology on Complex Numbers (ℂ)
zariski_topology_complex_numbers = complex_numbers + [
    logic_axioms["Existential Generalization"], # Closed sets correspond to zeros of polynomials
    logic_axioms["Universal Generalization"],   # Algebraic sets are closed
    logic_axioms["Implication"]                 # Closed sets are based on polynomial zeros
]

# 8. Finite Complement Topology on Ordinals
finite_complement_topology_ordinals = ordinals + [
    logic_axioms["Existential Generalization"], # Open sets are those with finite complements
    logic_axioms["Conjunction"],                # Combines open set and complement properties
    logic_axioms["Universal Generalization"]    # Ensures finite complements hold for all
]

# 9. Coarsest Topology on Cardinal Numbers
coarsest_topology_cardinals = cardinal_numbers + [
    logic_axioms["Existential Generalization"], # The empty set and full set exist
    logic_axioms["Universal Generalization"],   # No other open sets exist
    logic_axioms["Non-Contradiction"]           # Ensures no contradictions
]

# 10. Trivial Topology on Tarski's Universe
trivial_topology_tarski_universe = tarski_universe + [
    logic_axioms["Existential Generalization"],  # Ensures the trivial open sets
    logic_axioms["Non-Contradiction"]           # Ensures consistency in the trivial topology
]

# NEW TOPOLOGIES SPECIFIC TO DIFFERENTIABLE MANIFOLDS

# 11. Smooth Manifold Topology (open sets defined by charts from ℝ^n)
smooth_manifold_topology = real_numbers + [
    logic_axioms["Existential Generalization"],  # Charts from ℝ^n exist in each open set
    logic_axioms["Universal Generalization"],    # Union of open sets is open
    logic_axioms["Implication"],                 # Overlapping charts must be smoothly compatible
    logic_axioms["Conjunction"]                  # Ensures logical consistency of smooth charts
]