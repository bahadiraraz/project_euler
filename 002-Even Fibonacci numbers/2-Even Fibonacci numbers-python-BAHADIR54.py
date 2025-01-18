def sumOfEvenValuedFibonacciNumbers(n):
    fibonacci = [1, 2]
    
    while fibonacci[-1] + fibonacci[-2] <= n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    result = 0
    for i in range(1, len(fibonacci), 3):
        result += fibonacci[i]
    
    return result

print("sum of the even-valued fibonacci numbers are: ", sumOfEvenValuedFibonacciNumbers(4000000))