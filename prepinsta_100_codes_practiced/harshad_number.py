n=int(input())
s=0
t=n
while n!=0:
    d=n%10
    s=s+d
    n=n//10
if t%s==0:
    print("true",t,s)