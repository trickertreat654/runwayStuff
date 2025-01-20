from math import floor

def count_multiples(n, primes):
    """
    Counts the number of multiples in the range 2 to n, based on the provided list of primes.
    Uses inclusion-exclusion to avoid overcounting numbers that are multiples of multiple primes.
    """
    num_multiples = 0
    num_primes = len(primes)
    
    # Inclusion-exclusion approach: sum fractions of primes progressively
    for i in range(1, 1 << num_primes):  # Loop over all subsets of primes
        subset_product = 1
        bits_set = bin(i).count("1")  # Count how many bits are set (i.e., the number of primes in the subset)
        
        # Calculate product of primes in the subset
        for j in range(num_primes):
            if i & (1 << j):  # Check if the j-th prime is included in the subset
                subset_product *= primes[j]
        
        # Count multiples of the product within the range
        if subset_product <= n:
            count = floor(n / subset_product) - floor(primes[-1] / subset_product)
            if bits_set % 2 == 1:  # Odd subset size: add
                num_multiples += count
            else:  # Even subset size: subtract
                num_multiples -= count
    
    return num_multiples

def count_primes_in_range(lower, upper, primes):
    """
    Counts the exact number of primes in the specified range [lower, upper] 
    by excluding all non-primes based on the provided list of primes.
    """
    # Total numbers in the range
    total_numbers = upper - lower + 1
    
    # Count non-prime numbers by counting multiples of each prime
    non_prime_count = count_multiples(upper, primes)
    
    # Calculate number of primes by subtracting non-primes from total numbers
    prime_count = total_numbers - non_prime_count
    return prime_count

# Test case: primes up to 179
primes_up_to_11 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79] 
lower_bound = primes_up_to_11[-1] + 1
upper_bound = primes_up_to_11[-1] ** 2

# Run the test
primes_in_range = count_primes_in_range(lower_bound, upper_bound, primes_up_to_11)
print(f"Number of primes between {lower_bound} and {upper_bound}: {primes_in_range}")
