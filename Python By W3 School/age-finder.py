import datetime

current_date=datetime.datetime.now()
print(current_date.year)
print(current_date.month)
print(current_date.day)
z=current_date.date()
current_year=current_date.year
current_month=current_date.month
current_day=current_date.day
birth_year=int(input("y"))
birth_month=int(input("m"))
birth_day=int(input("d"))
age=(current_year-birth_year,current_month-birth_month,current_day-birth_month)
print("Your Age is ",age)


