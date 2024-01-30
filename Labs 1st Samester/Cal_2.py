print("Enter 1 For Addition 2 For Substraction 3 For Multiplication 4 For Division")
opeartion=int(input("Enter Operation Number To Perform : "))
number1=int(input("Enter Number 1 : "))
number2=int(input("Enter Number 2 : "))
if opeartion==1:
    result=number1+number2
    print("The Sum of Number ",number1,"and",number2,"is",result)
elif opeartion==2:
    result=number1-number2
    print("The Substraction of Number ",number1,"and",number2,"is",result)
elif opeartion==3:
    result=number1*number2
    print("The Multiple of Number ",number1,"and",number2,"is",result)
elif opeartion==4:
    result=number1/number2
    print("The Division of Number ",number1,"and",number2,"is",result)
else:
    print("Wrong Command For Operation")