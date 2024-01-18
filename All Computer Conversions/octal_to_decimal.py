number=str(input("Enter Number : "))
length=len(number)
length=length-1
output=0
for i in number:
    i=int(i)
    multiplier=8**(length)
    result=i*multiplier
    output=output+result
    length=length-1
print(output)

