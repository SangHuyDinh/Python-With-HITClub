import random
a,b, c, d = list(map(int,input().split())),list(),list(),list()
b = random.sample(a, len(a))
for i in range(len(a)*30//100):
    c.append(b[i])
for i in range(len(a)*30//100,len(a)):
    d.append(b[i])
print(c)
print(d)





