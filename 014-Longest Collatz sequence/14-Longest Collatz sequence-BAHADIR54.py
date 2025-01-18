import  time
t = time.time()
def sayi2(a):
    bir = 0
    def sayi(a):
        nonlocal bir
        if a % 2 == 0 :bir +=1;return sayi(a/2)
        elif a == 1:bir += 1;return 1
        else:bir += 1;return  sayi(3*a +1)
    return sayi(a),bir
g = 0
for  i in range(1000000,1,-1):
    a,b=sayi2(i)
    if g < b:
        g ,y= b,i
        print(f"uzunluk: {g}, sayi: {i}", end="\r")
print(f"cevap = uzunluk: {g}, sayi: {y} , bulma suresi: {time.time()-t}", end="\r")