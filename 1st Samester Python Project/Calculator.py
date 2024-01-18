#Printing Welcome Statement
print("Welcome to Calculator ")
#Main Function to Perform Calculator Operations
def Calculator():
#will continue calculator function untill we break
    while True:
        print("+ - * / % (of number) or exit")#will ask what to perform
        operator=str(input("Enter Operation : "))
        if operator=="+" or operator=="-" or operator=="*" or operator=="/":#will check opeation what to perform
            num1=str(input("Enter Number 1 : "))#will get 1st number input
            num2=str(input("Enter Number 2 : "))#will get 2nd number input
            try:#will try to convert entered value in float to perform operation we use it to avoid error if we enter wrong values
                num1=float(num1)#will convert number 1
                num2=float(num2)#will convert number 2
                if operator=="+":#if upper condition is true will perform operation according to operation
                    result=num1+num2
                elif operator=="-":
                    result=num1-num2
                elif operator=="*":
                    result=num1*num2
                elif operator=="/":
                    result=num1/num2
                print("Your Output is ",result,"\n")#print output as result result will be obtained from eny of if or elif value
            except:#if try portion gives error programme will reach in except value and execute it
                print("Please Enter Valid Values \n")
        elif operator=="%":#will check if we have to find percentage
            num1=str(input("Enter Number to find percentage of : "))#will demand number 1
            num2=str(input("Enter Percentage to Find of Number : "))#will demand number 2
            try:#will try if entered values are convertable and accurate to perform operations
                num1=float(num1)
                num2=float(num2)
                print(num1,"% of",num2,"are following")
                result=(num2/100)*num1
                print("Your Output is ",result,"\n")
            except:#if try portion give any error it will rrun except without crashing programme
                print("Wrong inputs")
        elif operator=="exit":
            print("Thanks For Using Operator\n")
            break
        else:
            print("Invalid Operator")
def unitconvsrion():#main function to convert temperature values
    while True:#will continue function work untill we break
        print("Select Unit Conversion\n1-C to F   2-F to C\n3-C to K   4-K to C\n5-F to K   6-K to F")#print main instructions
        Conversion=str(input("Select Conversion : "))#will get input in string for error handlig
        if Conversion=="1" or Conversion=="2" or Conversion=="3" or Conversion=="4" or Conversion=="5" or Conversion=="6" :#will enter in if we selecting write values
            reading=str(input("Enter Reading : "))#getting temperature values in string to avoid error will convert later
            try:#try to perform function to avoid crash of programme
                reading=float(reading)#will convert reading to float if error occur will go to except portion
                if Conversion=="1":
                    result=(reading*(9/5))+32
                    return result#returning result outside the function
                elif Conversion=="2":
                    result=(reading-32)*(5/9)
                    return result#returning result outside the function
                elif Conversion=="3":
                    result=reading+273.15
                    return result#returning result outside the function
                elif Conversion=="4":
                    result=reading-273.15
                    return result#returning result outside the function
                elif Conversion=="5":
                    result=(reading-32)*(5/9)+(273.15)
                    return result#returning result outside the function
                elif Conversion=="6":
                    result=(reading-273.15)*(9/5)+(32)
                    return result#returning result outside the function
                elif Conversion=="exit":
                    print("Thanks for using\n")
                    break#breaking loop
                elif Conversion!="1" or Conversion!="2" or Conversion!="3" or Conversion!="4" or Conversion!="5" or Conversion!="6" :
                    print("Wrong command")#if values does not match accordint to condition or we can use else simple
            except:#if try portion gives any error programme will come here without crashing
                print("Please Enter Valid Values\n")   
            
def length_unit_conversion():
    while True:
        #function for length conversion
        print("Select Unit to convert\n1-Meter   2-Centimeter   3-Inch   4-Kilometer   5-Miles    exit")
        unit_to_convert = str(input("Enter Command : "))#taking input in str to avoid error
        if unit_to_convert=="exit":
            print("Thanks For Using \n")
            main_calculator_function()#if someone want to exit returning in main menu
        print("Select Unit to convert In\n1-Meter   2-Centimeter   3-Inch   4-Kilometer   5-Miles   exit")
        unit_to_convert_in = str(input("Enter Command : "))
        if unit_to_convert_in=="exit":
            print("Thanks For Using \n")
            main_calculator_function()#if someone wants to exit returning in main menu
        length = str(input("Enter Length : "))#taking input in string to avoid error
        try:#will try to run instructions given below if there is any error it will not crash programme it will go in except section
            unit_to_convert=float(unit_to_convert)#converting values in float to perform operations
            unit_to_convert_in=float(unit_to_convert_in)
            length=float(length)
            if unit_to_convert == 1 and unit_to_convert_in == 2:  # Meter to Centimeter
                result = length * 100
            elif unit_to_convert == 1 and unit_to_convert_in == 3:  #Meter to Inch
                result = length * 39.3701
            elif unit_to_convert == 1 and unit_to_convert_in == 4:  #Meter to Kilometer
                result = length * 0.001
            elif unit_to_convert == 1 and unit_to_convert_in == 5:  #Meter to Miles
                result = length * 0.000621371
            elif unit_to_convert == 2 and unit_to_convert_in == 1:  #Centimeter to Meter
                result = length / 100
            elif unit_to_convert == 2 and unit_to_convert_in == 3:  # Centimeter to Inch
                result = length / 2.54
            elif unit_to_convert == 2 and unit_to_convert_in == 4:  # Centimeter to Kilometer
                result = length / 100000
            elif unit_to_convert == 2 and unit_to_convert_in == 5:  # Centimeter   to Miles
                result = length / 160934.4
            elif unit_to_convert == 3 and unit_to_convert_in == 1:  # Inch to Meter
                result = length * 0.0254
            elif unit_to_convert == 3 and unit_to_convert_in == 2:  # Inch to Centimeter
                result = length * 2.54
            elif unit_to_convert == 3 and unit_to_convert_in == 4:  #Inch to Kilometer
                result = length * 0.0000254
            elif unit_to_convert == 3 and unit_to_convert_in == 5:  #Inch to Miles
                result = length * 0.0000157828
            elif unit_to_convert == 4 and unit_to_convert_in == 1:  #   Kilometer to Meter
                result = length * 1000 
            elif unit_to_convert == 4 and unit_to_convert_in == 2:  # Kilometer to   Centimeter
                result = length * 100000
            elif unit_to_convert == 4 and unit_to_convert_in == 3:  #Kilometer to Inch
                result = length * 39370.1
            elif unit_to_convert == 4 and unit_to_convert_in == 5:  #Kilometer to Miles
                result = length * 0.621371
            elif unit_to_convert == 5 and unit_to_convert_in == 1:  #Miles to Meter
                result = length * 1609.34
            elif unit_to_convert == 5 and unit_to_convert_in == 2:  #    Miles to Centimeter
                result = length * 160934
            elif unit_to_convert == 5 and unit_to_convert_in == 3:  #Miles to Inch
                result = length * 63360
            elif unit_to_convert == 5 and unit_to_convert_in == 4:  #         Miles to Kilometer
                result = length * 1.60934    
            else:
                result = length  # Default to input length if units are the same
            
            print("Your Output is " ,result,"\n")#will print result values obtained from any of if or else condition
        except:
            print("Please Enter Valid Command \n")


def currency_conversion():
    while True:
        print("Select Currency you want to convert\n1-PKR   2-USD   3-POUND   4-AED or exit ")
        currency=str(input("Enter Command : "))
        if currency=="exit":
            print("Thanks For Using \n")
            break
        print("Select Currency you want to convert In\n1-PKR   2-USD   3-POUND   4-AED or exit ")
        conversion_type=str(input("Enter Command : "))
        if conversion_type=="exit":
            print("Thanks For Using \n")
            break
        Amount=str(input("Enter Amount : "))
        try:#will try this 
            currency=float(currency)
            conversion_type=float(conversion_type)
            Amount=float(Amount)
            if currency==1 and conversion_type==2:
                result=Amount*(0.0036)
            elif currency==1 and conversion_type==3:
                result=Amount*(0.0028)
            elif currency==1 and conversion_type==4:
                result=Amount*(0.013)
            elif currency==2 and conversion_type==1:
                result=Amount*(279.29)
            elif currency==2 and conversion_type==3:
                result=Amount*(0.79)
            elif currency==2 and conversion_type==4:
                result=Amount*(3.67)
            elif currency==3 and conversion_type==1:
                result=Amount*(354.66)
            elif currency==3 and conversion_type==2:
                result=Amount*(1.27)
            elif currency==3 and conversion_type==4:
                result=Amount*(4.66)
            elif currency==4 and conversion_type==1:
                result=Amount*(76.05)
            elif currency==4 and conversion_type==2:
                result=Amount*(0.27)
            elif currency==4 and conversion_type==3:
                result=Amount*(0.21)
            elif currency==conversion_type:
                result=Amount
            print("Your Conversion Result is ",result,"\n")
        except:
            print("\nPlease Enter Valid Command \n")
def main_calculator_function():
    status=True#refrence value will use later
    while status==True:
        print("1-For Mathemetical Functions \n2-For Temperature Conversions\n3-For Currency Conversion\n4-For Length Conversion ")
        operator=str(input("Enter Operator or exit for main page: \n"))#asking for input what to do in string 
        if operator=="1":#calculator
            result=Calculator()#calling calculator operation by making variable result
        elif operator=="2":#temperature conversion
            result=unitconvsrion()#calling  temperature unit conversion 
            print("\nFinal Temperature is \n",result)  #printing output result returned from function 
        elif operator=="3":#currency conversion
            result=currency_conversion()
        elif operator=="4":
            length_unit_conversion()#calling length unit conversion function
        elif operator=="exit":
            print("Thanks For Using Calculator\n")
            import multi_purpose_app#will impoert other file in folder
            multi_purpose_app.main_multi()#will call function in imported app
        else:
            print("Wrong Command\n")
main_calculator_function()#calling main function
