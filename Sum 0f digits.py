num=int(input("enter positive number:"))
result=0
for i in range(len(str(num))):
    digit=num%10
    result=result+digit
    num=num/10
print("sum is :",result)
