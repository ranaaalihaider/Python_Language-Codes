number1=str(input("Enter Number 1 : "))
number2=str(input("Enter Number 2 : "))
number_1_list=[]
number_2_list=[]
for i in (number1):
    number_1_list.append(i)
for j in (number2):
    number_2_list.append(j)

length_1=len(number_1_list)
length_2=len(number_2_list)
while True:
    if length_1>length_2:
        number_2_list.insert(0,"0")
    elif length_2>length_1:
        number_1_list.insert(0,"0")
    else:
        break
    length_1=len(number_1_list)
    length_2=len(number_2_list)
print(number_1_list)
print(number_2_list)
output=[]
carry=0
for k in range(length_1-1,-1,-1):
    n1=int(number_1_list[k])
    n2=int(number_2_list[k])
    sum=(n1+n2+carry)
    result=sum%16
    output.append(result)
    carry=sum//16
if carry !=0:
    output.append(carry)
output.reverse()
print(output)
refrence=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
for z in output:
    print(refrence[z],end=" ")