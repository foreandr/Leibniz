from sympy import symbols, Function, diff

# Define symbols for smooth functions and variables
x, y, z = symbols('x y z')  # Base space variables
f = Function('f')(x, y, z)  # Example smooth function f(x, y, z)
g = Function('g')(x, y, z)  # Example smooth function g(x, y, z)

# A class to represent a derivation
class Derivation:
    def __init__(self, partials):
        """Initialize a derivation given the partial derivatives along each variable."""
        self.partials = partials  # Dictionary of {variable: coefficient}

    def __call__(self, func):
        """Apply the derivation to a function using the Leibniz rule."""
        return sum(coef * diff(func, var) for var, coef in self.partials.items())

    def __repr__(self):
        """Display the derivation in a readable format."""
        terms = [f"{coef} ∂/∂{var}" for var, coef in self.partials.items()]
        return " + ".join(terms)

# Example: Define a derivation D that acts as D(f) = f_x + 2f_y - f_z
D = Derivation({x: 1, y: 2, z: -1})

# Apply the derivation D to the smooth functions f and g
D_f = D(f)
D_g = D(g)

# Output the result of the derivation applied to the functions
print(f"D(f) = {D_f}")
print(f"D(g) = {D_g}")
