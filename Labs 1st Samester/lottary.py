import random
print("Welcome to Lottery \nEnter 3 digit Number")
number=random.randint(100,999)
while True:
    answeer=int(input("Enter Your Number : "))
    length=len(str(answeer))
    if length<4 and length>2:
        break
    else:
        print("Wrong Input Number Should be of three digits")
if number==answeer:
    print("Congratulations! You won $10,000!")
else:
    points=0
    number_str=str(number)
    answeer_str=str(answeer)
    for i in number_str:
        if i in answeer_str:
            points=points+1
    if points==0:
        print("Your Number was ",number,"You Lost No Match")
    elif points==1:
        print("Your Number was ",number,"You won 1000$")
    elif points==3:
        print("Your Number was ",number,"You won 3000$")
