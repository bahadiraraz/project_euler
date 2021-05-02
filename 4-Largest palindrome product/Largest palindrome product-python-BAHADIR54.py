ddd = list()
def test(i):

    b = i
    ok = i
    z = 0
    while i > 0:
        x = i % 10
        z = (z * 10) + x
        i = i // 10

    n = z
    yes = z
    op = z
    o = 0
    t = 0
    p = 1
    digits = 0
    while op > 0:
        digits += 1
        op //= 10
    half = (digits+1)/2
    half2 = (digits+1)/2

    d=int(ok//10**(half-1))
    d2=int(ok//10**(half-1))
    if yes == b :
        ddd.append(ok)


for i in (range(900000,1000000)):
    test(i)
for j in ddd:
    for i in (range(1000,1,-1)):

        for t in (range(1000, 1, -1)):

            if t * i == j:
                kume = set()
                kume.add(j)
                a=list(kume)
                print(a[0])
                exit()