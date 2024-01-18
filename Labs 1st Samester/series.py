n=int(input("enter  number : "))
x="2"
output=0
for i in range(1,n+1):
    final=x*i
    final=int(final)
    output=output+final
print(output)