def find(b,na):
    b[na] = (b[na]+1 if na in b else 1)
a = dict()
for i in range(int(input())):
    name = input()
    find(a,name)
print(max(a.keys(), key=(lambda k: a[k])))