import datetime
print(datetime.datetime.now())
t=datetime.datetime.now()
minute=t.strftime("%M")
minute=int(minute)
username="ali"
password="11223344"
count=0
t_C=-1
def user_login(count,minute,t_C):
    print(count)
    if count==4:
        if minute>=(t_C):
            count=0
            user_login(count,minute,t_C)
        else:
            print("To Many attempts Wait for 1 Minute")
    username_input=input(str("Enter username : "))
    if username_input==username:
        password_input=input(str("Enter Your Password : "))
        if password_input==password:
            print("Congratulations on Log in ")
        else:
            count=count+1
            if count==4:
                t_C=minute
                t_C=int(t_C)
                t_C=t_C+1
            user_login(count,minute,t_C)
    else:
        print("Wrong User Name Try Again")
        user_login(count,minute,t_C)
user_login(count,minute,t_C)