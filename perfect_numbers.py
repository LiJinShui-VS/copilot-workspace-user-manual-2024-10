# This script calculates and prints all perfect numbers within 100.
# A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.

def is_perfect(n):
    """
    Check if a number is perfect.
    
    A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is perfect, False otherwise.
    """
    # Initialize the sum of divisors
    sum_of_divisors = 0
    
    # Iterate over all possible divisors
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    
    # Check if the sum of divisors equals the number
    return sum_of_divisors == n

# Iterate over all numbers from 1 to 100
for num in range(1, 101):
    if is_perfect(num):
        # Print the perfect number and explain why it is perfect
        print(f"{num} is a perfect number because the sum of its proper divisors is equal to {num}.")
