list1=["banana1","apple2","fruits3","laptop","computer","mouse","keyboard"]
print(list1)
for x in list1:
    print(x)
print("Continue statement")
for x in list1:
    if x=="laptop":
        continue
    print(x)
print("Break statement")
for x in list1:
    if x=="laptop":
        break
    print(x)
#Range
for x in range(6):
    print(x)
for x in range(10,20):
    print(x)
#incriments
print("Incriemnt 2")
for x in range(2,30,2):
    print(x)
print("Incriemnt 3")
for x in range(2,30,3):
    print(x)
print("Use of else statement")
for x in range(1,15):
    print(x)
else:
    print("Finally Finished")