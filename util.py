def generate_primes(limit):
    """Generate a list of prime numbers up to a specified limit using the Sieve of Eratosthenes."""
    # Create a boolean array "prime[0..limit]" and initialize all entries as True.
    # A value in prime[i] will be False if i is not a prime.
    prime = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Update all multiples of p to False
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1

    # Collect all prime numbers
    return [number for number, is_prime in enumerate(prime) if is_prime and number >= 2]

