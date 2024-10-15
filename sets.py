from axioms import *

# 1. Zermelo-Fraenkel Set Theory (ZF)
zf = [
    Axiom_of_Extensionality,
    Axiom_of_Separation,
    Axiom_of_Pairing,
    Axiom_of_Union,
    Axiom_of_Power_Set,
    Axiom_of_Infinity,
    Axiom_of_Replacement,
    Axiom_of_Foundation
]

zfc = zf + [
    Axiom_of_Choice  # Adding the Axiom of Choice to ZF
]

# 2. Von Neumann-Bernays-Gödel (NBG) Set Theory
# NBG Set Theory extends ZF by adding classes and restricting certain operations to sets.
nbg = [
    Axiom_of_Extensionality,          # Sets with same elements are equal
    Axiom_of_Separation,              # Subsets based on properties
    Axiom_of_Pairing,                 # Sets containing two elements exist
    Axiom_of_Union,                   # Sets formed from the union of sets
    Axiom_of_Power_Set,               # Power sets exist
    Axiom_of_Infinity,                # Infinite set exists
    Axiom_of_Replacement,             # Replacement schema
    Axiom_of_Foundation,              # Regularity axiom, avoids self-referencing sets
    Axiom_of_Class_Comprehension,     # Class comprehension axiom (NBG-specific)
    Axiom_of_Global_Choice            # Global choice axiom (NBG-specific)
]

# 3. Kelley-Morse (KM) Set Theory
# KM is an extension of NBG that includes more powerful comprehension for classes.
km = [
    Axiom_of_Extensionality,
    Axiom_of_Separation,
    Axiom_of_Pairing,
    Axiom_of_Union,
    Axiom_of_Power_Set,
    Axiom_of_Infinity,
    Axiom_of_Replacement,
    Axiom_of_Foundation,
    Axiom_of_Class_Comprehension,     # Kelley-Morse class comprehension axiom
    Axiom_of_Global_Choice            # Global choice axiom (similar to NBG)
]

# 4. Constructive Zermelo-Fraenkel (CZF) Set Theory
# CZF avoids the law of excluded middle and focuses on constructive mathematics.
czf = [
    Axiom_of_Extensionality,
    Axiom_of_Separation,
    Axiom_of_Pairing,
    Axiom_of_Union,
    Axiom_of_Infinity,
    Axiom_of_Inductive_Set,           # Constructive version of infinity axiom
    Axiom_of_Subset_Collection,       # Subset collection axiom
    Axiom_of_Strong_Collection        # Strong collection axiom
]

# 5. Zermelo Set Theory
# An older version of ZF that excludes Replacement and Foundation but includes Choice.
zermelo_set_theory = [
    Axiom_of_Extensionality,
    Axiom_of_Separation,
    Axiom_of_Pairing,
    Axiom_of_Union,
    Axiom_of_Power_Set,
    Axiom_of_Infinity,
    Axiom_of_Choice  # This is included in Zermelo's original set theory
]

# 6. Ackermann Set Theory
# Ackermann set theory distinguishes between sets and classes without the full machinery of NBG.
ackermann_set_theory = [
    Axiom_of_Extensionality,
    Axiom_of_Separation,
    Axiom_of_Pairing,
    Axiom_of_Union,
    Axiom_of_Power_Set,
    Axiom_of_Infinity,
    Axiom_of_Set_Comprehension,        # Ackermann's comprehension axiom for classes
    Axiom_of_Class_Existence           # Classes are more fundamental than sets
]

# 7. Quine's New Foundations (NF) Set Theory
# NF allows sets to contain themselves, avoiding paradoxes by restricting comprehension.
nf_set_theory = [
    Axiom_of_Extensionality,
    Axiom_of_Universal_Class,          # New Foundations allows a universal class
    Axiom_of_Stratified_Comprehension  # Stratified comprehension to avoid Russell's Paradox
]

# 8. Kripke-Platek (KP) Set Theory
# KP set theory is weaker than ZF and focuses on sets that can be explicitly constructed.
kp_set_theory = [
    Axiom_of_Extensionality,
    Axiom_of_Separation,
    Axiom_of_Pairing,
    Axiom_of_Union,
    Axiom_of_Foundation,
    Axiom_of_Delta_0_Collection,       # A restricted form of replacement
    Axiom_of_Inductive_Set             # Ensures the existence of natural numbers
]

# 9. Tarski-Grothendieck (TG) Set Theory
# TG set theory is used in category theory and adds large cardinal axioms.
tg_set_theory = [
    Axiom_of_Extensionality,
    Axiom_of_Separation,
    Axiom_of_Pairing,
    Axiom_of_Union,
    Axiom_of_Infinity,
    Axiom_of_Tarski_Universe,          # Tarski's axiom for large cardinals
    Axiom_of_Replacement,
    Axiom_of_Foundation
]

# 10. Morse-Kelley Set Theory with Choice and Class Comprehension
# This is a full version of Morse-Kelley set theory that includes classes and the axiom of choice.
morse_kelley_choice = [
    Axiom_of_Extensionality,
    Axiom_of_Separation,
    Axiom_of_Pairing,
    Axiom_of_Union,
    Axiom_of_Power_Set,
    Axiom_of_Infinity,
    Axiom_of_Class_Comprehension,     # Kelley-Morse class comprehension axiom
    Axiom_of_Global_Choice            # Global choice axiom
]
