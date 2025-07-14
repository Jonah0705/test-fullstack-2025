import math

def f(n: int) -> int:
    if n < 0:
        raise ValueError("Please input a value greater than 0")
    factorial = math.factorial(n)
    power_of_n = 2 ** n
    result = math.ceil(factorial / power_of_n)
    return result
# insert value in here
value = 22
for i in range(value):
    print(f"f({i}) = {f(i)}")
