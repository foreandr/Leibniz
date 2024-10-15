logic_axioms = {
    "Identity": "x = x",                        
    "Non-Contradiction": "¬(P ∧ ¬P)",           
    "Excluded Middle": "P ∨ ¬P",                
    "Modus Ponens": "If P and P -> Q, then Q",  
    "Double Negation": "¬¬P → P",               
    "Transitivity": "If P -> Q and Q -> R, then P -> R",  
    "Universal Instantiation": "∀x P(x) -> P(c)",    
    "Existential Generalization": "P(c) -> ∃x P(x)", 
    "Conjunction": "P ∧ Q -> P, P ∧ Q -> Q",         
    "Disjunction Introduction": "P -> P ∨ Q",        
    "Disjunction Elimination": "P ∨ Q, ¬P -> Q",     
    "Biconditional Introduction": "(P -> Q) ∧ (Q -> P) -> P ↔ Q",  
    "Biconditional Elimination": "P ↔ Q -> (P -> Q) ∧ (Q -> P)",   
    "Implication": "P -> Q is the same as ¬P ∨ Q",  
    "De Morgan's Laws": "¬(P ∧ Q) ↔ (¬P ∨ ¬Q)",     
    "Contrapositive": "P -> Q ↔ ¬Q -> ¬P",          
    "Negation Introduction": "If assuming P leads to a contradiction, then ¬P",  
    "Existential Instantiation": "∃x P(x) -> P(c)", 
    "Universal Generalization": "P(c) for arbitrary c -> ∀x P(x)", 
    "Hypothetical Syllogism": "If P -> Q and Q -> R, then P -> R",
    
    # Modal Logic Specific Axioms (Necessity and Possibility)
    "Necessity": "□P → P",                       # If necessarily P, then P
    "Possibility": "P → ◇P",                     # If P, then possibly P
    "Necessity Distribution": "□(P → Q) → (□P → □Q)",  
    "Possibility Distribution": "◇(P ∨ Q) ↔ (◇P ∨ ◇Q)"  
}

Axiom_of_Extensionality = [
    logic_axioms["Identity"],
    logic_axioms["Biconditional Introduction"],
    logic_axioms["Universal Instantiation"]
]

Axiom_of_Separation = [
    logic_axioms["Existential Generalization"],
    logic_axioms["Universal Instantiation"],
    logic_axioms["Conjunction"]
]

Axiom_of_Pairing = [
    logic_axioms["Existential Instantiation"],
    logic_axioms["Conjunction"]
]

Axiom_of_Union = [
    logic_axioms["Existential Generalization"],
    logic_axioms["Disjunction Introduction"]
]

Axiom_of_Power_Set = [
    logic_axioms["Universal Instantiation"],
    logic_axioms["Existential Generalization"]
]

Axiom_of_Infinity = [
    logic_axioms["Existential Generalization"]
]

Axiom_of_Replacement = [
    logic_axioms["Universal Instantiation"],
    logic_axioms["Existential Generalization"],
    logic_axioms["Modus Ponens"]
]

Axiom_of_Foundation = [
    logic_axioms["Non-Contradiction"],
    logic_axioms["Universal Instantiation"]
]

Axiom_of_Choice = [
    logic_axioms["Existential Generalization"],
    logic_axioms["Universal Instantiation"]
]

Axiom_of_Regularity = [
    logic_axioms["Non-Contradiction"],
    logic_axioms["Universal Instantiation"]
]

Axiom_of_Empty_Set = [
    logic_axioms["Existential Generalization"]
]

Axiom_of_Subsets = [
    logic_axioms["Universal Instantiation"],
    logic_axioms["Existential Generalization"],
    logic_axioms["Conjunction"]
]

Axiom_of_Well_Ordering = [
    logic_axioms["Existential Generalization"],
    logic_axioms["Modus Ponens"]
]

Axiom_of_Finite_Choice = [
    logic_axioms["Existential Generalization"],
    logic_axioms["Universal Instantiation"]
]

Axiom_of_Class_Comprehension = [
    logic_axioms["Universal Instantiation"],  # Classes behave like sets in comprehension
    logic_axioms["Existential Generalization"],
    logic_axioms["Conjunction"]
]

Axiom_of_Global_Choice = [
    logic_axioms["Existential Generalization"],  # For every class, a choice exists
    logic_axioms["Universal Instantiation"],
    logic_axioms["Modus Ponens"]
]

Axiom_of_Inductive_Set = [
    logic_axioms["Existential Generalization"],  # Ensures an inductive set (infinity)
    logic_axioms["Universal Instantiation"],
    logic_axioms["Modus Ponens"]
]

Axiom_of_Subset_Collection = [
    logic_axioms["Universal Instantiation"],   # Collect all subsets
    logic_axioms["Conjunction"],
    logic_axioms["Existential Generalization"]
]

Axiom_of_Strong_Collection = [
    logic_axioms["Existential Instantiation"],  # Images under functions form sets
    logic_axioms["Universal Instantiation"],
    logic_axioms["Modus Ponens"]
]

Axiom_of_Set_Comprehension = [
    logic_axioms["Existential Generalization"],  # Sets are formed by comprehending elements
    logic_axioms["Universal Instantiation"],
    logic_axioms["Conjunction"]
]

Axiom_of_Class_Existence = [
    logic_axioms["Existential Generalization"],  # Classes exist independent of sets
    logic_axioms["Universal Instantiation"]
]

Axiom_of_Universal_Class = [
    logic_axioms["Existential Generalization"],  # The class of all sets exists
    logic_axioms["Universal Instantiation"]
]

Axiom_of_Stratified_Comprehension = [
    logic_axioms["Conjunction"],                 # Comprehension restricted to stratified formulas
    logic_axioms["Existential Generalization"],
    logic_axioms["Universal Instantiation"]
]

Axiom_of_Delta_0_Collection = [
    logic_axioms["Existential Generalization"],  # Collection for Δ₀ definable functions
    logic_axioms["Universal Instantiation"],
    logic_axioms["Modus Ponens"]
]

Axiom_of_Delta_0_Collection = [
    logic_axioms["Existential Generalization"],  # Collection for Δ₀ definable functions
    logic_axioms["Universal Instantiation"],
    logic_axioms["Modus Ponens"]
]

Axiom_of_Inductive_Set = [
    logic_axioms["Existential Generalization"],  # Inductive sets to ensure natural numbers
    logic_axioms["Universal Instantiation"]
]

Axiom_of_Tarski_Universe = [
    logic_axioms["Existential Generalization"],  # Large cardinals (Tarski's Universe)
    logic_axioms["Universal Instantiation"],
    logic_axioms["Modus Ponens"]
]
