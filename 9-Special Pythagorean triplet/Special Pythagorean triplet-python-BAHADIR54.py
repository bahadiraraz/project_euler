def pisagor():
    l = list()
    for i in range(1, 1000):
        for j in range(1, 1000):

            c = (i ** 2 + j ** 2) ** 0.5

            if (c == int(c)) and (i + j +int(c))==1000:
                l.append([i, j, int(c)])


    return l


for i in pisagor():
    print(i[0]*i[1]*i[2])
    exit()
