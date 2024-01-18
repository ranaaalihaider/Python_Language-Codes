number_1=str(input("Enter Number 1 : "))
number_2=str(input("Enter Number 2 : "))
list_number_1=[]
list_number_2=[]
for i in number_1:
    list_number_1.append(i)
for j in number_2:
    list_number_2.append(j)

length_1=len(list_number_1)
length_2=len(list_number_2)
while True:
    if length_1>length_2:
        list_number_2.insert(0,"0")
    elif length_2>length_1:
        list_number_1.insert(0,"0")
    else:
        break
    length_1=len(list_number_1)
    length_2=len(list_number_2)
print(list_number_1)
print(list_number_2)
output=[]
carry=0
for k in range(length_1-1,-1,-1):
    n1=int(list_number_1[k])
    n2=int(list_number_2[k])
    sum=(n1+n2+carry)%2
    output.append(sum)
    carry=(n1+n2+carry)//2
if carry==1:
    output.append("1")
output.reverse()
print(output)