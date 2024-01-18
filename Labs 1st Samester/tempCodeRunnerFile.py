limit=int(input("Enter Number to Print Series : "))
number1=0
numbere2=1
def series_function(n1,n2):
    while n1+n2<limit:
        print(n1+n2)
        n1,n2=n2,(n1+n2)
series_function(number1,numbere2)