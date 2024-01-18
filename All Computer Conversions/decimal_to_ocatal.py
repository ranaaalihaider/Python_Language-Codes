number=int(input("Enter Number : "))
result=[]
while number>0:
    reminder=number%8
    result.append(reminder)
    number=number//8
result.reverse()
for i in result:
    print(i,end=" ")