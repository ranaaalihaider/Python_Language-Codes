number=str(input("Enter Number : "))
refrence=["000","001","010","011","100","101","110","111"]
list_number=[]
for i in number:
    list_number.append(i)
length=len(list_number)
while True:
    list_number
    if length%3 !=0:
        list_number.insert(0,"0")
    else:
        break
    length=len(list_number)
length=int(length/3)
a=0
b=3
print("Your Binary Output is : ",end="")
for i in range(0,length):
    final=list_number[a:b]
    final="".join(final)
    output=refrence.index(final)
    print(output,end="")
    a=a+3
    b=b+3

