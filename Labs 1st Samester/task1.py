def Addition(n1,n2):
    result=n1+n2
    print("Result is ",result)
def Substraction(n1,n2):
    result=n1-n2
    print("Result is ",result)
def Multiplication(n1,n2):
    result=n1*n2
    print("Result is ",result)
def Division(n1,n2):
    result=n1/n2
    print("Result is ",result)
#strating Programme

print("Enter + For Addition - For Substraction * For Multiplication / For Division")
opeartion=input("Enter Operation Number To Perform : ")
number1=int(input("Enter Number 1 : "))
number2=int(input("Enter Number 2 : "))
if opeartion=="+":
    Addition(number1,number2)
elif opeartion=="-":
    Substraction(number1,number2)
elif opeartion=="*":
    Multiplication(number1,number2)
elif opeartion=="/":
    Division(number1,number2)
