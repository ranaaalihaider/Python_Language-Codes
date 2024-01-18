number=int(input("Enter Number : "))
result=[]
while number>0:
    refrence=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    hexa=number%16
    final=refrence[hexa]
    result.append(final)
    number=number//16
result.reverse()
for i in result:
    print(i,end=" ")