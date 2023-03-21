for a in range(1,20):
    c=0
    for i in range(2,a+1):
        if a%i==0:
            c+=1
    prime="prime"
    nonprime="nonprime"
    if c==1:
        print(prime,a)
    else:
        print(nonprime,a)

