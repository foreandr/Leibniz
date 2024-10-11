# operations.py
import numpy as np

# ----- General Arithmetic Operations -----
def addition(x, y):
    """General addition operation that works for numbers, vectors, and matrices."""
    return round(x + y, 2)

def multiplication(x, y):
    """General multiplication operation."""
    return round(x * y, 2)

def subtraction(x, y):
    """Subtraction operation."""
    return round(x - y, 2)

def division(x, y):
    """Division operation."""
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return round(x / y, 2)

# ----- Vector Operations -----
def vector_dot(v1, v2):
    """Compute the dot product of two vectors."""
    return round(np.dot(v1, v2), 2)

def vector_cross(v1, v2):
    """Compute the cross product of two 3D vectors."""
    if len(v1) != 3 or len(v2) != 3:
        raise ValueError("Cross product is only defined for 3D vectors.")
    return np.round(np.cross(v1, v2), 2)

def scalar_multiplication(scalar, vector):
    """Multiply a vector by a scalar."""
    return np.round(np.multiply(scalar, vector), 2)

def vector_addition(v1, v2):
    """Add two vectors and return a tuple with standard Python types and rounded values."""
    result = np.round(np.add(v1, v2), 2)  # Perform addition and round to 2 decimal places
    # Convert numpy array to a tuple of standard Python float types
    return tuple(float(x) for x in result)

# ----- Matrix Operations -----
def matrix_addition(m1, m2):
    """Add two matrices."""
    return np.round(np.add(m1, m2), 2)

def matrix_multiplication(m1, m2):
    """Multiply two matrices."""
    return np.round(np.matmul(m1, m2), 2)

def matrix_transpose(matrix):
    """Transpose of a matrix."""
    return matrix.T

def matrix_inverse(matrix):
    """Inverse of a square matrix."""
    return np.round(np.linalg.inv(matrix), 2)

# ----- Spinor Operations -----
def pauli_spinor_multiplication(spinor1, spinor2):
    """Multiply two 2D Pauli spinors."""
    return np.round(np.dot(spinor1, spinor2), 2)

def dirac_spinor_multiplication(spinor1, spinor2):
    """Multiply two 4D Dirac spinors."""
    return np.round(np.dot(spinor1, spinor2), 2)

def spinor_conjugate(spinor):
    """Complex conjugate of a spinor."""
    return np.round(np.conjugate(spinor), 2)

# ----- Spacetime Operations -----
def minkowski_inner_product(v1, v2):
    """
    Compute the Minkowski inner product of two spacetime vectors.
    Assume metric signature (-,+,+,+) for spacetime points.
    """
    metric = np.array([-1, 1, 1, 1])
    return round(np.sum(metric * np.array(v1) * np.array(v2)), 2)

def lorentz_boost(spacetime_point, beta):
    """
    Apply a Lorentz boost along the x-direction.
    spacetime_point: (t, x, y, z)
    beta: velocity/c (must be less than 1)
    """
    if abs(beta) >= 1:
        raise ValueError("Beta must be less than 1.")
    gamma = 1 / np.sqrt(1 - beta**2)
    boost_matrix = np.array([
        [gamma, -gamma * beta, 0, 0],
        [-gamma * beta, gamma, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    return np.round(np.dot(boost_matrix, np.array(spacetime_point)), 2)

# ----- Operation Router -----
def apply_operation(element1, element2, operation):
    """Router to apply an operation based on element type."""
    if isinstance(element1, (list, tuple, np.ndarray)) and isinstance(element2, (list, tuple, np.ndarray)):
        if len(element1) == 2 and len(element2) == 2:  # Spinor-like
            return tuple(pauli_spinor_multiplication(element1, element2))
        elif len(element1) == 4 and len(element2) == 4:  # Dirac Spinor-like
            return tuple(dirac_spinor_multiplication(element1, element2))
        else:
            return operation(element1, element2)
    else:
        return operation(element1, element2)
