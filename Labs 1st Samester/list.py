'''list1=["Apples Bnana ","Mouse Keyboard","Pen Register"]
print(list1)
print(list1[1])
for i in list1:
    print(i)
print(list1[0][1])'''
#Exercise 5: Display numbers from a list using loop
'''list=[12,35,36,50,100]
for i in list:
    print(i)'''
#Exercise 6: Count the total number of digits in a number
'''number=str(input("Enter Number : "))
print("Length of Number is ",len(number))'''
#2nd method
'''
number=int(input("Enter Number : "))
limit=10
answer=1
while True:
    if number<limit:
        print("Length of Number is ",answer)
        break
    else:
        limit=limit*10
        answer=answer+1'''
'''Write a program to use for loop to print the following reverse number pattern

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1'''
'''
limit=int(input("Enter Number of lines"))
for i in range(0,limit):
    number=limit-i
    for x in range(0,(limit-i)):
        print((number-x),end=" ")
    print()'''
#Exercise 8: Print list in reverse order using a loop
'''
list=[12,20,30,40,50,60]
length=len(list)
for items in list:
    print(items)
print("reversed ")
for x in range(0,length):
    print(list[(length-1)-x])'''
#Exercise 9: Display numbers from -10 to -1 using for loop
'''
for i in range(-10,0):
    print(i)'''
#prime number finder
'''
while True:
    prime_status=True
    number=int(input("Enter Number : "))
    for i in range(2,number):
        if number%i==0:
            prime_status=False
    if prime_status==True:
            print('Number is prime')
    else:
        print("Your Number is not prime")'''
#Exercise 15: Use a loop to display elements from a given list 
#present at odd index positions
'''
list=[1,2,3,4,5,6,7,8,9]
length=len(list)
for i in range(1,length):
    if i%2 !=0:
        print(list[i])'''
#Calculate the cube of all numbers from 1 to a given number
'''
limit=20
for i in range(1,limit+1):
    print(i**3)'''
#2nd Last 
''' 
number=str(input("Enter Number : "))
limit=int(input("Enter Series Limit : "))
result=0
for i in range(1,limit+1):
    final=number*i
    print(final)
    final=int(final)
    result=result+final
print("The sum is : ",result)'''
'''
limit=9
limit=limit//2
for i in range(0,limit+1):
    for x in range(-1,i):
        print("*",end=" ")
    
    print()
for i in range(0,limit+1):
    for y in range(limit,i,-1):
        print("*",end=" ")
    print()'''
'''lis2=["ali","laptop","haider"]
for i in lis2:
    print(lis2.index(i),i)'''
x="1221"
print(len(x))