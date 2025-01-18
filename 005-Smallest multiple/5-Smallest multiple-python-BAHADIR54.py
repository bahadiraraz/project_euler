import math

def LCM(a, b):
    return (a*b) // math.gcd(a, b)

result = 1
for i in range(1,21):
    result = LCM(result , i)

print("Smallest number divisible by all numbers from 1 to 20:", result)