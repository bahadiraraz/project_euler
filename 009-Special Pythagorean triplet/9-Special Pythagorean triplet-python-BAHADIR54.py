for a in range(1,333):
    b = (1000000-2000*a)//(2000-2*a)
    c = (1000-a-b)

    if a**2 + b**2 == c**2:
        print(a*b*c)