#!/usr/bin/python3

def minOperations(n):
    if n <= 1:
        return 0
    
    operations = 0
    current = n
    
    for i in range(2, n + 1):
        while current % i == 0:
            operations += i  # Copy All (1 operation) + Paste (i-1 operations)
            current //= i  # Reduce current by factor i
            
    return operations
