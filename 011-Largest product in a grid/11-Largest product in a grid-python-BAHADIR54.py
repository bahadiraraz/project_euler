file = open("in.txt","r+",encoding="UTF-8")
h = list()
for i in range(1,21) :
    g=file.readline().strip("\n")
    h.append(g.split(" "))

a = [list(a)for a in h]
yatay = list()
dikey = list()
capraz1 = list()
capraz2 = list()
for i in a: print(i)
for i in range(20):
    for j in range(17):
        yatay.append(int(a[i][j]) * int(a[i][j + 1])*  int(a[i][j + 2]) * int(a[i][j + 3]))
for i in range(17):
    for j in range(20):
        dikey.append(int(a[i][j])*int(a[i+1][j])*int(a[i+2][j])*int(a[i+3][j]))
for i in range(17):
    for j in range(17):
        capraz1.append(int(a[i][j])*int(a[i+1][j+1])*int(a[i+2][j+2])*int(a[i+3][j+3]))
for i in range(3,20):
    for j in range(17):
        capraz2.append(int(a[i][j]) * int(a[i - 1][j + 1] )*int( a[i - 2][j + 2]) *int( a[i - 3][j + 3]))
print(max(max(dikey),max(yatay),max(capraz1),max(capraz2)))