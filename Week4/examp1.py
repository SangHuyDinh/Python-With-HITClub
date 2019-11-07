def add(a, b):
    return a+b
a,b = list(map(int,input().split())),list(map(int,input().split()))
for i in range(min(len(a),len(b))):
    print(add(a[i],b[i]),end=' ')
