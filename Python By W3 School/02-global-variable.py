x="Awsome"
print(x)
def myfunction():
    print("Python is "+x)

myfunction()

def youfunction(): 
    x="amazing2"
    print("Python is "+x)
youfunction()
print(x)
#SO IN this case x is a variable
"""X INSIDE a function is a local variable and x outside is a function
is a global variable local variable can be used only inside a function not globally everywhere"""

y="global only"
print(y)
def function3():
    global y
    y="Global inside a function"
    print("we can make "+y)
function3()
print(y)