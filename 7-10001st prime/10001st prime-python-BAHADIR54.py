a = 0
for i in range(1, 100000000):

   if i > 1:
       for j in range(2, i):
           if (i % j) == 0:
               break
       else:
            a +=1

   if a == 10001:
       print(i)
       exit()
