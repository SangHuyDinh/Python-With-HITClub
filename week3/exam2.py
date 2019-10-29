x,y,x1,y1 = map(int, input().split())
a,b,a1,b1 = map(int, input().split())
S_a = abs((x1-x)*(y1-y))
S_b = abs((a1-a)*(b1-b))
S_ch = (min(x1, a1) - max(x,a))*(min(b1,y1) - max(b,y))
rs = S_a+S_b - 2*S_ch if S_ch>0 else S_a+S_b
print(rs)
