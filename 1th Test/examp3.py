n = int(input())
a = list(map(str,input().split()))
b = list()
for i in range(len(a)):
    b.append(a[i][::-1])
for i in range(len(a)):
    if b[i] in a:
        print(b[i])
        