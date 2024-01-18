number=str(input("Enter Number : "))
length=len(number)
length=length-1
result=0
for i in range(0,length+1):
    x=number[length-i]
    x=int(x)
    print(x)
    y=x*(2**(i))
    result=result+y
print(result)