number=str(input("Enter Number : "))
length=len(number)
refrence=["000","001","010","011","100","101","110","111"]
final=""
for i in number:
    i=int(i)
    resut=refrence[i]
    final=final+resut+" "

print(final)