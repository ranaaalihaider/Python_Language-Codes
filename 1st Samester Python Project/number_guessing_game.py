import random
def hint(random_num):# function to display hints
    if random_num==1:
        print("A single step on a journey of a thousand miles.")
    if random_num==2:
        print("One little duck.")
    if random_num==3:
        print("Happy family.")
    if random_num==4:
        print("knock at the door.")
    if random_num==5:
        print("The petals on a common flower that brings good luck.")
    if random_num==6:
        print("Bottom heavy. Devil's number")
    if random_num==7:
        print("I'm the only single-digit number that can't be multiplied or added within the first ten digits.")
    if random_num==8:
        print("Turn me sideways, and you'll find endless amusement!")
    if random_num==9:
        print("I'm the cat's luck.")
    if random_num==10:
        print("A big fat hen,")
def check(num):#check the answer
    if num==random_num:
        print("congratulations")
        return 1
    else:
        print("Last chance!")
def number_guessing_main_function():#main function
    while True:#keeps the loop running
        try:#error handling
            x=eval(input("To start press: 1\nTo end press: 0"))
            if x==0:
                import multi_purpose_app
                multi_purpose_app.main_multi()
                break#breaks the loop
            if x!=1:
                print("Invalid input!\nTry again")
                continue#skips the next part of loop
            random_num = random.randint(1,10)
            hint(random_num)
            turn=0#keeps the count of turn
            while True:#keeps the loop running
                num=eval(input("Enter your guess between 1 to 10: "))
                turn+=1#increment turn by 1
                if 1<= num <=10:
                    ans=check(num)
                    if ans==1:
                        break
                    if turn>=2:#breaks the loop after 2 turns
                        print("Game Over")
                        break
                else:
                    print("Invalid Input")
                    turn-=1#decreement turn by 1
                    continue# continue the loop from the start
        except:
            print("\nWrong Inputs \n")
                
            
number_guessing_main_function()