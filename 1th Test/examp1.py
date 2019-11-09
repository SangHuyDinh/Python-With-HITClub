n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
summ = 0
for i in a:
    summ += i
    if summ > sum(a)//2:
        summ -= i
print(sum(a) - (summ*2))




    