import sys

n,r,c = map(int,sys.stdin.readline().rstrip().split())
def Z(n,n1,n2,x,y):
    global cnt
    if x==r and y==c:
        return 
    if n1//2>r and n2//2>c:
        Z(n//2,(n1+x)//2,(n2+y)//2,x,y)
        return
    else:
        cnt += (n//2)*(n//2)
    if n1//2>r and n2//2<=c:
        Z(n//2,n1//2+x//2,n2,x,y//2+n2//2)
        return
    else:
        cnt += (n//2)*(n//2)
    if n1//2<=r and n2//2>c:
        Z(n//2,n1,n2//2+y//2,x//2+n1//2,y)
        return
    else:
        cnt += (n//2)*(n//2)
    if n1//2<=r and n2//2<=c:
        Z(n//2,n1,n2,x//2+n1//2,y//2+n2//2)
        return
    else:
        cnt += (n//2)*(n//2)
    
cnt = 0
Z(2**n,2**n,2**n,0,0)
print(cnt)