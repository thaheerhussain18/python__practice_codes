def NumChecker(n):
    if n==0:
        return "zero"
    elif n>0:
        return "positive"
    else:
        return "negative"
  
  
n=input("enter the number to check positive and negative")
print(NumChecker(int(n)))
