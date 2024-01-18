x=int(input("enter your number "))
limit=10
answer=1
while True:
    if x<limit:
        print(answer)
        break
    else:
        limit=limit*10
        answer=answer+1
print("hello")