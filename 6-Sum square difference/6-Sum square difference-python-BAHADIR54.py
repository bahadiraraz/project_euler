def kare_ayri():
    a = 0
    for i in range(1,101):
        a += pow(i,2)
    return a


def toplam_kare():
    a =  list(range(1, 101))

    return pow(sum(a),2)
print(toplam_kare()-kare_ayri())