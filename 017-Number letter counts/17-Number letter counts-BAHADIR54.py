birler = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
onlar = [0,3,6,6,5,5,5,7,6,6]
onlar2=[0,6,6,8,8,7,7,9,8,8]
yuzler = [7, 10]
a = ((sum(birler) * 9 + onlar[1] + sum(onlar2) + sum(onlar[2:]) * 10) * 10)
b = (yuzler[0] * 9 + yuzler[1] * 99 * 9 + sum(birler) * 100)
print(a +b +11)



