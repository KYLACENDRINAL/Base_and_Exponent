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
base1=25
exp1=2
result1=exponent(base1, exp1)
print(f"{base1} raises to the power of {exp1} is {result1}")

# Testing Case 2
print("Case 2: ")
base2=2
exp2=3
result2=exponent(base2, exp2)
print(f"{base2} raises to the power of {exp2} is {result2}")