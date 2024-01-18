import sys
def main_multi():
    while True:
        print("Welcome to Multipurpose App\nWhat Would Your Like to Do\n1-Calculator   2-To Do List        3-Quote Of The Day   4-Historical Events\n5-Dictionary   6-Number Guessing   7-Quiz               or exit")
        programme_selection=str(input("Enter Command : "))
        if programme_selection=="1":
            import Calculator
            Calculator.main_calculator_function()
        elif programme_selection=="2":
            import To_Do_List 
            To_Do_List.main_to_do_list_()
        elif programme_selection=="3":
            import Quote_of_the_day
            Quote_of_the_day.function_for_random_quote()
        elif programme_selection=="4":
            import historical_events
            historical_events.historical_event_function()
        elif programme_selection=="5":
            import Dictionary
            Dictionary.dictionary_main_function()
        elif programme_selection=="6":
            import number_guessing_game
            number_guessing_game.number_guessing_main_function()
        elif programme_selection=="7":
            import quiz
            quiz.quiz_main_function()
        elif programme_selection=="exit":
            print("Thanks for using")
            sys.exit()

        else:
            print("Wrong Command")

        print(programme_selection)
main_multi()