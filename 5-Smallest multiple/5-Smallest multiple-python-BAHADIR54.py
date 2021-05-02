def bolum(a):
     for i in range(1,21):
         if a %  i != 0:
             return False
     return True
for  i in range(1,1000000000):
    if bolum(i):
        print(i)
        exit()
