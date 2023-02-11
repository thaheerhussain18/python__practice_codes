def SumUpToN(n):
    s=0
    for i in range(n+1):
        s+=i
    return s

print(SumUpToN(int(input())))
