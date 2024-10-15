from axioms import *

propositional_logic = [
    logic_axioms["Identity"],
    logic_axioms["Non-Contradiction"],
    logic_axioms["Excluded Middle"],
    logic_axioms["Modus Ponens"],
    logic_axioms["Double Negation"],
    logic_axioms["Conjunction"],
    logic_axioms["Disjunction Introduction"],
    logic_axioms["Disjunction Elimination"],
    logic_axioms["Biconditional Introduction"],
    logic_axioms["Biconditional Elimination"],
    logic_axioms["De Morgan's Laws"],
    logic_axioms["Contrapositive"],
    logic_axioms["Hypothetical Syllogism"]
]

predicate_logic = [
    logic_axioms["Identity"],
    logic_axioms["Non-Contradiction"],
    logic_axioms["Excluded Middle"],
    logic_axioms["Modus Ponens"],
    logic_axioms["Universal Instantiation"],
    logic_axioms["Existential Generalization"],
    logic_axioms["Transitivity"],
    logic_axioms["Negation Introduction"],
    logic_axioms["Existential Instantiation"],
    logic_axioms["Universal Generalization"]
]

intuitionistic_logic = [
    logic_axioms["Identity"],
    logic_axioms["Non-Contradiction"],
    logic_axioms["Modus Ponens"],
    logic_axioms["Conjunction"],
    logic_axioms["Disjunction Introduction"],
    logic_axioms["Disjunction Elimination"],
    logic_axioms["Negation Introduction"],
    logic_axioms["Universal Instantiation"],
    logic_axioms["Existential Generalization"]
]
modal_logic = [
    logic_axioms["Identity"],
    logic_axioms["Non-Contradiction"],
    logic_axioms["Excluded Middle"],
    logic_axioms["Modus Ponens"],
    logic_axioms["Necessity"],
    logic_axioms["Possibility"],
    logic_axioms["Necessity Distribution"],
    logic_axioms["Possibility Distribution"]
]

peano_arithmetic = [
    logic_axioms["Existential Generalization"],  # ∃x (x = 0) (Axiom of Zero)
    logic_axioms["Existential Instantiation"],   # ∃y (y = S(x)) (Axiom of Successor)
    logic_axioms["Non-Contradiction"],          # ¬(S(x) = 0) (Zero is not the successor of any natural number)
    logic_axioms["Contrapositive"],             # x ≠ y -> S(x) ≠ S(y) (Axiom of distinct successors)
    logic_axioms["Universal Instantiation"],     # ∀P [P(0) ∧ (∀x(P(x) → P(S(x)))) → ∀x P(x)] (Induction)
    logic_axioms["Modus Ponens"]                # For applying induction and chaining implications
]