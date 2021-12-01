num = input()
n = num.split(',')
m = int(n[0])
c = int(n[1])
w = int(n[2])
k= int(n[3])
w = m//c
x = m//c
while w//3 != 0 :
    s = (w//3) * k
    x = x + s
    w= s + w%3
print(x)
