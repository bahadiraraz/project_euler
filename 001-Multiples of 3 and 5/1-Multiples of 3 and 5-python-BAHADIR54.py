def SumOfMultiples(n):
    sum3 = sum(n for n in range(3, n, 3))
    sum5 = sum(n for n in range(5, n, 5))
    sum15 = sum(n for n in range(15, n, 15))

    return sum3 + sum5 - sum15

print("Sum of multiples of 3 or 5 below 1000:", SumOfMultiples(1000))
