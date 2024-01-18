#task1 number print 1 to 10
'''limit=0
while limit<=10:
    print(limit)
    limit=limit+1'''
#task2 Factorial
'''
number=int(input("Enter Number : "))
multiplier=number-1
while multiplier>0:
    result=number*(multiplier)
    number=result
    multiplier=multiplier-1
print(result)'''
#task3  fibonachi
'''
number=int(input("Enter Number : "))
n1=0
n2=1
while n2<=number:
    result=n1+n2
    print(result)
    n1,n2=n2,result'''
#check number is palindrome
'''
number22=str(input("Enter Number : "))
length=len(number22)
pel_status=True
for i in range(0,length):
    if number22[i]==number22[((length-1)-i)]:
        pel_status=True
    else:
        pel_status=False
if pel_status==True:
    print("Pel")
elif pel_status==False:
    print("Not Pel")'''
#method 2
'''
command=str(input("Enter Command : "))
command2=command[::-1]
if command==command2:
    print("It is Pelentron")
else:
    print("It is not Pelentrone")
'''
#Take 10 integers from keyboard using loop and print their average value on the screen.
'''n=0
sum=0
while n<10:
    num1=int(input("Enter Number : "))
    n=n+1
    sum=sum+num1
print(sum/10)'''
#Print the following patterns using loop
'''a=0
limit=5
while a<limit:
    a=a+1
    c=0
    while a>c:
        c=c+1
        print("*",end="")
    print()
'''

#Print multiplication table of 24, 50 and 29 using loop.
'''multiplier=int(input("Enter Number For Table : "))
count=1
while count<=10:
    print(multiplier*count)
    count=count+1
'''

#Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.
'''number1=int(input("Enter Number 1 : "))
number2=int(input("Enter Number 2 : "))
limit=0
count=0
if number1>number2:
    count=number1
if number2>number1:
    count=number2
while limit<=count:
    limit=limit+1
    if number1%limit==0 and number2%limit==0:
        result=limit
print("Your Highest Common Divisior is : ",result)'''
#Take integer inputs from user until he/she presses q 
#( Ask to press q to quit). Print average and product of all numbers.
'''count=0
sum=0
while True:
    number=str(input("Enter Numbers to find average or q to exit: "))
    if number=="q":
        break
    else:
        number=int(number)
        count=count+1
        sum=sum+number
        average=sum/count
print(average)'''
