fibonnaci = [1,1]
a = 2
while True:
  b = fibonnaci[a-1] + fibonnaci[a-2]
  fibonnaci.append(b)
  if len(str(b)) == 1000:
      print(a)
      break
  a+=1


