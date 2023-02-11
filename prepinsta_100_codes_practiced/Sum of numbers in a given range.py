def SumInRange(n,o):
  s=0
  for i in range(n,o+1):
    s+=i
  return s
s=int(input())
q=int(input())
print(SumInRange(s,q))
