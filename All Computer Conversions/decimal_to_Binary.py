number=int(input("Enter Number : "))
binary=[]
while number>0:
    result=number%2
    binary.append(result)
    number=number//2
length=len(binary)
length=length-1
for i in range(length,-1,-1):
    print(binary[i],end=" ")