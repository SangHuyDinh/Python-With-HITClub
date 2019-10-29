#import sys
#input=sys.stdin.readline
s = input()
lens = len(s)
while lens>0:
    t = lens//2-1 if lens%2==0 else lens//2
    print(s[t], end='')
    s=s.replace(s[t], '')
    lens-=1
    
