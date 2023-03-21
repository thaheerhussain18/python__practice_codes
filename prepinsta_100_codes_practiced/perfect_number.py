n=int(input())
su=[]
for i in range(1,n):
    if n%i==0:
        su.append(i)

if n==sum(su):
    print("perfect_number")

