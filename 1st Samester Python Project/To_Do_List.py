
Sunday_string,monday_string,tuesday_string,wednesday_string,thursday_string,friday_string,saturday_string=[],[],[],[],[],[],[]

print("\nWelcome to Your To Do List") #welcome note
def all_tasks():
    print("Your all tasks are here")
    if len(Sunday_string)>0:
        print("For Sunday : \n",Sunday_string)
    if len(monday_string)>0:
        print("For Monday : \n",monday_string)
    if len(tuesday_string)>0:
        print("For Tuesday : \n",tuesday_string)
    if len(wednesday_string)>0:
        print("For Wednesday : \n",wednesday_string)
    if len(thursday_string)>0:
        print("For Thursday : \n",thursday_string)
    if len(friday_string)>0:
        print("For Friday : \n",friday_string)
    if len(saturday_string)>0:
        print("For Saturday : \n",saturday_string)
def add_new_task_function(): #adding task function
    print("Select Day\n1-Sunday   2-Monday   3-Tuesday   4-Wednesday\n5-Thursday 6-Friday   7-Saturday")
    add_task_day=str(input("Enter Command : ")) #selecting days
    new_task=str(input("Enter Your Task : ")) #entring tasks
    if add_task_day=="1":#Sunday
        Sunday_string.append(new_task)
    elif add_task_day=="2":#Monday
        monday_string.append(new_task)
    elif add_task_day=="3":#Tuesday
        tuesday_string.append(new_task)
    elif add_task_day=="4":#Wednseday
        wednesday_string.append(new_task)
    elif add_task_day=="5":#Thursday
        thursday_string.append(new_task)
    elif add_task_day=="6":#Friday
        friday_string.append(new_task)
    elif add_task_day=="7":#Saturday   
        saturday_string.append(new_task)
    elif add_task_day=="exit":
        main_to_do_list_()
    else:
        print("Wrong Command Of Day Re-Enter \n") #error handling 
        add_new_task_function()#calling function again
def see_or_remove_function():#making function
    print("\nWhat would you like to do\n1-See Tasks 2-Remove Tasks or exit")
    view_or_remove=str(input("Enter Command : "))
    if view_or_remove=="1":
        print("Select Day\n1-Sunday   2-Monday   3-Tuesday   4-Wednesday\n5-Thursday 6-Friday   7-Saturday")
        select_see_task_day=str(input("Enter Command : "))
        if select_see_task_day=="1":
            for index,tasks in enumerate(Sunday_string):
                print(index,tasks)
        elif select_see_task_day=="2":
            for index,tasks in enumerate(monday_string):
                print(index,tasks)
        elif select_see_task_day=="3":
            for index,tasks in enumerate(tuesday_string):
                print(index,tasks)
        elif select_see_task_day=="4":
            for index,tasks in enumerate(wednesday_string):
                print(index,tasks)
        elif select_see_task_day=="5":
            for index,tasks in enumerate(thursday_string):
                print(index,tasks)
        elif select_see_task_day=="6":
            for index,tasks in enumerate(friday_string):
                print(index,tasks)
        elif select_see_task_day=="7":
            for index,tasks in enumerate(saturday_string):
                print(index,tasks)
        elif select_see_task_day=="exit":
            main_to_do_list_()
        else:
            print("Wrong Command \n")
            see_or_remove_function()#calling same function again
    elif view_or_remove=="2":#remove
        print("Select Day\n1-Sunday   2-Monday   3-Tuesday   4-Wednesday\n5-Thursday 6-Friday   7-Saturday")
        select_see_task_day=str(input("Enter Command : "))
        if select_see_task_day=="1":
            if len(Sunday_string)<1:
                print("No Tasks Found ")
            elif len(Sunday_string)>1:
                for index,tasks in enumerate(Sunday_string):
                    print(index,tasks)
                task_to_remove=int(input("Enter Task Number to Remove :"))
                Sunday_string.pop(task_to_remove)
                print("Your task has been removed")
        elif select_see_task_day=="2":
            if len(monday_string)<1:
                print("No Tasks Found ")
            elif len(monday_string)>1:
                for index,tasks in enumerate(monday_string):
                    print(index,tasks)
                task_to_remove=int(input("Enter Task Number to Remove :"))
                monday_string.pop(task_to_remove)
                print("Your task has been removed")
        elif select_see_task_day=="3":
            if len(tuesday_string)<1:
                print("No Tasks Found ")
            elif len(tuesday_string)>1:
                for index,tasks in enumerate(tuesday_string):
                    print(index,tasks)
                task_to_remove=int(input("Enter Task Number to Remove :"))
                tuesday_string.pop(task_to_remove)
                print("Your task has been removed")
        elif select_see_task_day=="4":
            if len(wednesday_string)<1:
                print("No Tasks Found ")
            elif len(wednesday_string)>1:
                for index,tasks in enumerate(wednesday_string):
                    print(index,tasks)
                task_to_remove=int(input("Enter Task Number to Remove :"))
                wednesday_string.pop(task_to_remove)
                print("Your task has been removed")
        elif select_see_task_day=="5":
            if len(thursday_string)<1:
                print("No Tasks Found ")
            elif len(thursday_string)>1:
                for index,tasks in enumerate(thursday_string):
                    print(index,tasks)
                task_to_remove=int(input("Enter Task Number to Remove :"))
                thursday_string.pop(task_to_remove)
                print("Your task has been removed")
        elif select_see_task_day=="6":
            if len(friday_string)<1:
                print("No Tasks Found ")
            elif len(friday_string)>1:
                for index,tasks in enumerate(friday_string):
                    print(index,tasks)
                task_to_remove=int(input("Enter Task Number to Remove :"))
                friday_string.pop(task_to_remove)
                print("Your task has been removed")
        elif select_see_task_day=="7":
            if len(saturday_string)<1:
                print("No Tasks Found ")
            elif len(saturday_string)>1:
                for index,tasks in enumerate(saturday_string):
                    print(index,tasks)
                task_to_remove=int(input("Enter Task Number to Remove :"))
                saturday_string.pop(task_to_remove)
                print("Your task has been removed")
        elif select_see_task_day=="exit":
            main_to_do_list_() #calling main function 
        else:
            print("Wrong Command \n")
            see_or_remove_function()#calling same function again
    elif view_or_remove=="exit":
        print(" ")
        main_to_do_list_()
    else:
        print("Wrong Command Re-Enter\n")
        see_or_remove_function()
def main_to_do_list_():
    print("Select Your Purpose\n1-Add New Task  2-See Or Remove Tasks   \n3-For All Tasks exit for main mage")
    command=str(input("Enter Command : "))
    if command=="1":#add /or remove tasks
        add_new_task_function()
            
    elif command=="2":#see pending or Remove
        see_or_remove_function()
    elif command=="3":
        all_tasks()
    elif command=="exit":
        print("Thanks for using To Do List\n")
        import multi_purpose_app
        multi_purpose_app.main_multi()
    else:
        print("Wrong Command Re-Enter\n")
main_to_do_list_()