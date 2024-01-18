number=str(input("Enter Number : "))
refrence=["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]
refrence2=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
final=[]
for i in number:
    final.append(i)
print(final)
length=len(final)
while True:
    if length%4 !=0:
        final.insert(0,"0")
    else:
        break
    length=len(final)
print(final)
a=0
b=4                
length=int(length/4)
OUTPUT=[]
for i in range(0,length):
    res1="".join(final[a:b])
    c=(refrence.index(res1))
    OUTPUT.append(refrence2[c])
    a=a+4
    b=b+4
    
f=" ".join(OUTPUT)
print(f)