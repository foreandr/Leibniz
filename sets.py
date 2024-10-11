# Import rich components for printing
from rich.console import Console
from rich.text import Text
from rich.panel import Panel

# Redefine the sets (as done previously) for printing with rich
import sympy as sp
from sympy import I, sqrt, pprint

# 1. Integers (ℤ)
infinite_integers = sp.Range(-sp.oo, sp.oo, 1)

# 2. Complex Numbers (ℂ)
real_part, imag_part = sp.symbols('n m', integer=True)
infinite_complex_numbers = sp.FiniteSet(real_part + imag_part * I)

# 3. Rational Numbers (ℚ)
infinite_rationals = sp.FiniteSet(*[sp.Rational(n, n+1) for n in range(1, 10)])

# 4. Real Numbers (ℝ)
real_set = sp.Interval(-sp.oo, sp.oo)

# 5. Polynomials
x, y = sp.symbols('x y')
infinite_polynomials = sp.FiniteSet(*[sp.Poly(n*x**2 + n*y + 1, x, y) for n in range(1, 4)])

# 6. Square Roots
infinite_square_roots = sp.FiniteSet(*[sqrt(n) for n in range(1, 10)])

# Create a console object
console = Console()

# Use rich to format and print the sets nicely
# Use rich to format and print the sets nicely with adjusted panel widths
console.print(Panel(Text("Integers (ℤ):", style="bold"), subtitle=str(infinite_integers), expand=True))

console.print(Panel(Text("Complex Numbers (ℂ):", style="bold"), subtitle=str(infinite_complex_numbers), expand=True))

console.print(Panel(Text("Rational Numbers (ℚ):", style="bold"), subtitle=str(infinite_rationals), expand=True))

console.print(Panel(Text("Real Numbers (ℝ):", style="bold"), subtitle=str(real_set), expand=True))

console.print(Panel(Text("Polynomials:", style="bold"), subtitle=str(infinite_polynomials), expand=True))

console.print(Panel(Text("Square Roots:", style="bold"), subtitle=str(infinite_square_roots), expand=True))
