# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

# pseudocode

# Define the function of exponent
def exponent(base, exp):
    result=1
    for _ in range(exp):
        result*=base
    return result

# Testing Case 1

# Testing Case 2