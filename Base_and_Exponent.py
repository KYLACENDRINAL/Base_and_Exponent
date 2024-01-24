# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

# pseudocode

# Define the function of exponent
def exponent(base, exp):
    result=1
    for _ in range(exp):
        result*=base
    return result

# Testing Case 1
print("Case 1: ")
base1=2
exp1=5
result1=exponent(base1, exp1)
print(f"{base1} raises to the power of {exp1} is {result1}")

# Testing Case 2