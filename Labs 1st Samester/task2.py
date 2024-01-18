#Taking Inputs
n1=int(input("Enter Number 1 : "))
n2=int(input("Enter Number 2 : "))
n3=int(input("Enter Number 3 : "))
n4=int(input("Enter Number 4 : "))
#making function to check greater
def maxfunction(n1,n2,n3,n4):
    if n1>n2 and n1>n3 and n1>n4:
        print(n1,"is Greatest Number")
    elif n2>n1 and n2>n3 and n2>n4:
        print(n2,"is Greatest Number")
    elif n3>n1 and n3>n2 and n3>n4:
        print(n3,"is Greatest Number")
    elif n4>n1 and n4>n2 and n4>n3:
        print(n4,"is Greatest Number")
#calling function that was madessssssss
maxfunction(n1,n2,n3,n4)