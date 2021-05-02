f = 0
n = 0
def bolen(n):
    a = 0

    for i in range(1, int(n**0.5 + 1)):
        if n % i == 0:
            a += 1

    return (a * 2) - 1
while f < 500:
    ucgen_sayi = sum(list(range(n)))
    f = bolen(ucgen_sayi)
    n += 1
print(ucgen_sayi)