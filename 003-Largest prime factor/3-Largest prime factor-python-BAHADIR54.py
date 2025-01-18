def LargestPrimeFactor(n):
    while n%2 == 0:
        n //= 2
    while n%3 == 0:
        n //= 3
    
    #control of 6n+1 and 6n-1
    i=5
    while i*i <=n:
        while n%i == 0:
            n //=i
        while n%(i+2) == 0:
            n //= (i+2)

        i+=6
    
    return n

print("The largest prime factor of the number 600851475143  is :  ", LargestPrimeFactor(600851475143))