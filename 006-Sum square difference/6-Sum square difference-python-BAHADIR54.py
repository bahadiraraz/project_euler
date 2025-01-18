#sum of k² formula is : (n*(n+1)*(2*n+1))/6
#sum of (1+2...+k)² is (n*(n+1)/2)²
#Difference of these two formula (n*(n+1)*(3*n+2)*(n-1))/12

def differenceOfTheseFormula(n):
    return n*(n+1)*(3*n+2)*(n-1)//12

print("The answer is : ", differenceOfTheseFormula(100))