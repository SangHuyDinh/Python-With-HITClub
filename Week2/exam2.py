#Viết Chương trình nhập vào 3 số là 3 cạnh của tam giác. In ra cạnh dài nhất của tam giác tương ứng. 
#Tính chu vị, diện tích tam giác đó và in ra màn hình.
a,b,c = map(int,input('nhap 3 canh cua tam giac:').split())
m = max(a,b,c)
mi = min(a,b,c)
cv = a+b+c
cv2 = cv/2
s = (cv2*(cv2-a)*(cv2-b)*(cv2-c))**0.5
print("canh lon nhat = ",m,"\ncanh nho nhat = ",mi,"\nchu vi = ",cv,"\ndien tich = ",s)
#other way:
# a,b,c = map(int,input('nhap 3 canh cua tam giac:').split())
# print("canh lon nhat = ",max(a,b,c),"\ncanh nho nhat = ",min(a,b,c),"\nchu vi = ",a+b+c,"\ndien tich = ",((a+b+c)/2*((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c))**0.5)


