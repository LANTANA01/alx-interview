#!/usr/bin/python3
"""Finding minimum operations """

def minOperations(n):
    #defines the functin for minoperations
    if n <= 1:
        return 0
    
    num_of_operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            #print("divisor is", divisor)
            n = n / divisor
            #print("\nn = n / divisor", n)

            num_of_operations = num_of_operations + divisor
            #print("\nnum of operations", num_of_operations)

        else:
            divisor += 1
            #print("divisor after increment: ", divisor)

    return num_of_operations
