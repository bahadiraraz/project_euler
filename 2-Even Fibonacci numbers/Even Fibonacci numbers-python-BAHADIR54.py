import sys
sys.setrecursionlimit(1000)
a = [0, 1]
def fib(n):

    if n <= 0:
        pass

    elif n <= len(a):
        return a[n - 1]
    else:

        b = fib(n - 1) + fib(n - 2)
    if b < 4000000:
        a.append(b)
    return b

fib(50)
b = [b for b in a if b % 2 == 0]
print(sum(b))
