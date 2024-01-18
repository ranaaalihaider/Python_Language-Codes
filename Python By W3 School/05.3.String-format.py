"""age=36
stataement="The age of person is " + age
print(stataement)"""
#This is wrong method by this medthod we can not combine string and variable like int
#we cna use function like format()
age=25
stm="I am ali haider and i am {}"
print(stm.format(age))
#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
str2="Hi my name is ali and i am {} years old and we are {} brothers. My contact number is {} thats all for one example."
age=20
brothers=4
number= 3056949459
print(str2.format(age,brothers,number))
#this will start indexing from 0 we can also take indexing manually
str3="I am ali i am {2} years old we are {0} brothers. My contact number is {1}"
print(str3.format(brothers,number,age))
