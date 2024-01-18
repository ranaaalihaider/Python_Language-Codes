number=int(input("Enter Number : "))
output=0
first=number
for x in range(number,2,-1):
    next=x-1
    result=first*next
    first=result
print(result)