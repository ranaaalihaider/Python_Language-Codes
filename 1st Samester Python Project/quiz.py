def quiz(sub):#display the quiz questions
    marks=0
    Q=quiz_Q(sub)
    ans=quiz_ans(sub)
    for i in range(len(Q)):
        while True:
            print(Q[i])
            opt=input("\nInput:")
            if 'a'<= opt<='d':
                    break
            else:
                print("Invalid! Try again")
        if opt==ans[i]: 
            marks+=1
    return marks           
def quiz_Q(sub):# database for questions
    if sub==1:
        IT_list=["What does HTML stand for?\nA) Hyper Text Markup Language\nB) High Tech Multi-Language\nC) Hyperlink and Text Management Language\nD) Hyper Transfer Markup Language","Which programming language is known for its use in artificial intelligence and machine learning?\nA) Java\nB) Python\nC) C++\nD) Ruby","What is the purpose of a firewall in network security?\nA) To enhance internet speed\nB) To prevent unauthorized access\nC) To increase computer storage\nD) To improve software compatibility","What does the acronym \"URL\" stand for in the context of web addresses?\nA) Universal Resource Locator\nB) Uniform Resource Locator\nC) Unified Resource Locator\nD) Universal Reference Locator","Which of the following is a version control system used in software development?\nA) SVN\nB) FTP\nC) HTTP\nD) DNS"]
        return IT_list
    elif sub==2:
        math_list=["What is the value of π (pi) to two decimal places?\nA) 3.14\nB) 3.16\nC) 3.18\nD) 3.12","If a triangle has angles measuring 45°, 45°, and 90°, what type of triangle is it?\nA) Equilateral\nB) Isosceles\nC) Scalene\nD) Isosceles Right Triangle","What is the square root of 64?\nA) 8\nB) 6\nC) 10\nD) 12","In algebra, what does \"x\" represent in the equation 2x + 5 = 15?\nA) 2\nB) 5\nC) 10\nD) 7.5","What is the area of a rectangle with length 8 units and width 5 units?\nA) 40 square units\nB) 13 square units\nC) 26 square units\nD) 20 square units"]
        return math_list
    else:
        geo_list=["Which river is the longest in the world?\nA) Amazon\nB) Nile\nC) Yangtze\nD) Mississippi","In which continent is the Sahara Desert located?\nA) Asia\nB) Africa\nC) South America\nD) Australia","What is the capital city of Australia?\nA) Sydney\nB) Melbourne\nC) Canberra\nD) Brisbane","Which mountain range separates Europe and Asia?\nA) Andes\nB) Alps\nC) Ural Mountains\nD) Himalayas","The Great Barrier Reef, the world's largest coral reef system, is located in which ocean?\nA) Pacific Ocean\nB) Atlantic Ocean\nC) Indian Ocean\nD) Southern Ocean"]
        return geo_list
    
def quiz_ans(sub):# database for answers
    if sub==1:
        ans=['a','b','b','b','a']
        return ans
    elif sub==2:
        ans=['a','d','a','b','a']
        return ans
    else:
        ans=['b','b','c','c','a']
        return ans
def quiz_main_function():#main function
    try:
        while True:#keeps the loop running
                comp_marks=0
                math_marks=0
                geo_marks=0
                while True:
                    sub=eval(input("For \"IT\" press:1\nFor \"Maths\" press:2\nFor \"Geography\"press:3\nFor \"Result\" press:4\nFor  Exit press:0\nInput:"))
                    if sub==0:
                        print("Good Bye!")
                        import multi_purpose_app
                        multi_purpose_app.main_multi()
                        break#exit the loop
                    if sub==1:
                        comp_marks=quiz(sub)
                    elif sub==2:
                        math_marks=quiz(sub)
                    elif sub==3:
                        geo_marks=quiz(sub)
                    elif sub==4:
                        print("Marks in computer: ",comp_marks,"\nMarks in mathematics: ",math_marks,"\nMarks in geography: ",geo_marks)
                        sum=comp_marks+math_marks+geo_marks
                        print("Obtain Marks= ",sum,"/15")
                        avg=sum/3
                        print("Average= ",round(avg,2))
                        perc=(sum/15)*100
                        print("Percentage = ",round(perc,2))
                    else:
                        print("Invalid Input")
    except:
        print("\n Wrong Inputs \n")


quiz_main_function()#calling main function