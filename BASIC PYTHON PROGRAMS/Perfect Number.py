lower=int(input("enter thr lower limit:"))
upper=int(input("enter thr upper limit:"))
for num in range(lower,upper+1):
    result=0
    for i in range(1,num):
        if(num%i)==0:
            result=result+i
    if num==result:
        print(num)

