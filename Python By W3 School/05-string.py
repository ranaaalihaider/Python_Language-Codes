#string can be in single quotes or double
print("Hello1")
print('Hello2') 
x="String with variable x "
print(x)
"""This is a multi line
comment example with no variavle assign"""
a="""This is an example of
multi line string that will be used to represent things 
like paragraph"""
print(a)
#now for single qoute
a='''Multi line 
string with single quotes'''
print(a)
"""String in array now we will see string as array and we will get elements seprately from array
and we wwill print them remember that numbering start from 0"""
a="This is a demo string 1"
print(a)
print("Now i will print 3 number letter from upper string ")
print(a[3])
print("Now i will print all characters of upper string sing for function")
for x in a:
    print(x)
print("Now we will print length of string using len function")
print(len(a))
#now we will check that certain word is present in string or not i will check demo and hello seprately
print("demo" in a)
print("Hello" in a)
if "demo" in a:
    print("demo is in string a")
else:
    print("demo is not in string a")
if "demo22" in a:
    print("demo22 is in string a")
else:
    print("demo22 is not in string a")
#we can also use not in text function
if "expensive " not in a:  
    print("expensive is not in a")
else:
    print("Expensive is in a")
if "demo" not in a:
    print("demo is not in a")
else: 
    print("Demo is in a")
#string slicing
print(a[0:3])
print(a[3:])
print(a[:-4])
#exercise of string slicing
cab="This is an example string to test string slicing using [:]"
print(cab)
print(cab[0:10])
print(cab[2:])
print(cab[2:2])
print(cab[0:-4])
#we can also multiply strings
abc=" ICT LAB"
final=abc*3
print(final)