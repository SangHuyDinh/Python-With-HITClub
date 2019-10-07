#Nhập một số vào từ bàn phím. Sau đó in ra các số là số chính phương từ 1 tới số vừa nhập.
def checka(num):
    if int(num**0.5)**2 == num:
        return True

n = int(input())
for i in range(1,n+1):
    if checka(i):
        print(i,end=' ')
    
#other way:
#num = int(input())
#for i in range(1, num+1): print(str(i)+", " if int(i**0.5)**2==i else '',end='')