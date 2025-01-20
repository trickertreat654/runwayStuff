from bitarray import bitarray  # Install bitarray using: pip install bitarray

def sieve_of_eratosthenes(limit):
    # Initialize a bit array with False (0) to represent that all numbers are initially prime
    is_prime = bitarray(limit + 1)
    is_prime.setall(True)  # Set all bits to True initially (meaning "prime")
    
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    
    # Start marking multiples of each prime starting from 2
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:  # If i is still marked as prime
            # Mark all multiples of i from i^2 up to limit as non-prime (False)
            is_prime[i * i : limit + 1 : i] = False
    
    # Now `is_prime` bit array has True at prime indices and False at non-prime indices
    primes = [i for i in range(limit + 1) if is_prime[i]]
    return primes

# start time
import time
start = time.time()
print("Start time: ", start)
# Example usage to find primes up to a large number
primes_up_to_a_billion = sieve_of_eratosthenes(10**9)

# Print the number of primes found
print(f"Number of primes found: {len(primes_up_to_a_billion)}")

# end time
end = time.time()
print("End time: ", end)
print("Time taken: ", end - start)


# Print the primes
# print("First 10 primes:", primes_up_to_a_billion[:])
