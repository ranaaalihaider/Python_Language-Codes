import random#importing random function to choce random quotes next in code 
import datetime#importing datetime function to show automatically current day in output that we will use next
#Database for English Quotes
Quotes_English= [
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "The only way of finding the limits of the possible is by going beyond them into the impossible. - Arthur C. Clarke",
    "It always seems impossible until it is done. - Nelson Mandela",
    "We may encounter many defeats, but we must not be defeated. - Maya Angelou",
    "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart. - Helen Keller",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. - Ralph Waldo Emerson",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "The biggest risk is not taking any risk. In a world that is changing quickly, the only strategy that is guaranteed to fail is not taking risks. - Mark Zuckerberg",
    "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it. - Jordan Belfort",
    "Dream big and dare to fail. - Norman Vaughan",
    "You must expect great things of yourself before you can do them. - Michael Jordan",
    "You can't use up creativity. The more you use, the more you have. - Maya Angelou",
    "It is never too late to be what you might have been. - George Eliot",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar",
    "In the middle of every difficulty lies opportunity. - Albert Einstein",
    "If you want to lift yourself up, lift up someone else. - Booker T. Washington",
    "Strive not to be a success, but rather to be of value. - Albert Einstein",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Success is not just about making money. It's about making a difference. - Unknown",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "The will to win, the desire to succeed, the urge to reach your full potential... these are the keys that will unlock the door to personal excellence. - Confucius",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
    "Opportunities don't happen. You create them. - Chris Grosser",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart. - Roy T. Bennett",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Success is not in what you have, but who you are. - Bo Bennett",
    "The future depends on what you do today. - Mahatma Gandhi",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The best way to predict the future is to invent it. - Alan Kay",
    "The only thing necessary for the triumph of evil is for good men to do nothing. - Edmund Burke",
    "Change your thoughts and you change your world. - Norman Vincent Peale",
    "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
    "The best preparation for tomorrow is doing your best today. - H. Jackson Brown Jr.",
    "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "The future depends on what you do today. - Mahatma Gandhi",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The secret of getting ahead is getting started. - Mark Twain",
    "Happiness is not something ready-made. It comes from your own actions. - Dalai Lama",
    "Success is walking from failure to failure with no loss of enthusiasm. - Winston Churchill",
    "The only true wisdom is in knowing you know nothing. - Socrates"
]
#Urdu quotes Database
urdu_quotes = [
    "Har baat ka waqt hota hai.",
    "Rang barangi duniya ko dekhne ka maza hai.",
    "Der aaye durust aaye.",
    "Jo kuch hona hai, achha hona hai.",
    "Rishtay mohabbat ke hote hain.",
    "Zindagi ek safar hai, khwab dekho.",
    "Mohabbat har mushkil ko aasan kar deti hai.",
    "Dunya ka koi maqam humain dosron se behtar nahi bana sakta.",
    "Apne manzil ka pata hamesha khud hi karna chahiye.",
    "Khawabon ko panay ke liye neend khoni bhi parti hai.",
    "Mushkil raaste bhi aasaan ho jate hain mohabbat se.",
    "Khushiyan milne se zyada unhe baantne se milti hain.",
    "Jab tak zindagi hai, tab tak ummeed hai.",
    "Bure waqt mein bhi achaai chhupi hoti hai.",
    "Zindagi mein kamiyabi us bande ko milti hai jo hausla nahi haar ta.",
    "Zindagi jeene ke liye sab kuch qurbaan kar dena chahiye.",
    "Mehek jo hai woh phoolon se nahi, khaaroun se aati hai.",
    "Apne khwabon se bada koi dost nahi hota.",
    "Mushkil waqt mein hosla aur mohabbat sab kuch hai.",
    "Ameer wo hai jo khud ko samjhe, gareeb wo hai jo doosron ko samjhe.",
    "Dil mein jazbaat rakhne walay hi asli shair hote hain.",
    "Dil ko chhoo jane wale alfaz hi asal mohabbat ke hote hain.",
    "Mushkil raaste bhi asaan ho jate hain, mohabbat se.",
    "Aik muskurahat sab par bhaari hoti hai.",
    "Kamyabi us par muskurane wale ki muskurahat par muskurati hai.",
    "Mushkil raaste bhi asaan ho jate hain mohabbat se.",
    "Zindagi mein kabhi haar na maano.",
    "Kisi bhi mushkil ko chhupane ke liye kuch bhi karo, bas khush raho.",
    "Hamesha sacha aur imandar raho, duniya khud tumhare saath hogi.",
    "Koi bhi kam asaan nahi hota, lekin uska asan tareeka zaroor hota hai.",
    "Mehnat rang laati hai, kabhi na kabhi.",
    "Kabhi kabhi humein us cheez ki talash hoti hai jo humare paas hoti hai.",
    "Zindagi ki asal khoobsurti woh hoti hai jo hum andar se mehsoos karte hain.",
    "Jab dil ka raasta saaf hota hai, to mushkil raaste bhi aasaan ho jate hain.",
    "Koshish karne walon ki haar nahi hoti.",
    "Mehnat ka fal zaroor milta hai.",
    "Zindagi mein kamiyabi paane ke liye, khud ko kho dena padta hai.",
    "Zindagi ka asal rang mohabbat aur khushi se bharpoor hota hai.",
    "Dunya mein kisi se kam nahi aur kisi se zyada nahi.",
    "Zindagi ki asal keemat mohabbat se hoti hai.",
    "Har mushkil ko qubool karo, taqatwar bano.",
    "Khud ko pehchaan kar dikhao, duniya khud tumhe pehchaanegi.",
    "Har mushkil asaan ho jati hai jab saath mohabbat hoti hai.",
    "Kamyabi us insaan ko milti hai jo darna nahi janta.",
    "Kamyabi us bande ko milti hai jo apni soch badal deta hai.",
    "Zindagi ka sab se bada maqsad, khud ko behtar banana chahiye.",
    "Mushkil raaste bhi aasaan ho jate hain mohabbat se.",
    "Jab dil ka raasta saaf hota hai, to mushkil raaste bhi aasaan ho jate hain.",
    "Kamyabi us bande ko milti hai jo haar ke baad bhi na haar maane.",
    "Dil ko chhoo jane wale alfaz hi asal mohabbat ke hote hain.",
    "Zindagi mein kabhi haar na maano."
]
#Code starting from here
#main function is below
def function_for_random_quote():
    while True: #will run the programme again and again until we break 
        print("Welcome to Quote of the day Generator\nSelect Your prefered Language\n1-For English   2-For Urdu  3-For Multiple Quotes Or exit for main page")
        language_choice=str(input("Enter Command : "))#taking command 
        if language_choice=="1":#if 1 is selected
            date=datetime.datetime.now() #will import date and time of now and will set it equall to date variable
            day=date.strftime("%A")
#as current date and time has been imported on day variable now we will use .strftime("%A") function to convert current date and time in Day name
            print("Quote of the day for",day,"in English is :\n\n",random.choice(Quotes_English),"\n")
#will show current day and will choce random quote from english quotes list using random.choice method
        elif language_choice=="2":#if 2 is selected
            date=datetime.datetime.now() #will import date and time of now and will set it equall to date variable
            day=date.strftime("%A")
#as current date and time has been imported on day variable now we will use .strftime("%A") function to convert current date and time in Day name
            print("Quote of the day for",day," in urdu is : \n\n",random.choice(urdu_quotes),"\n")
#will show current day and will choce random quote from Urdu quotes list using random.choice method
        elif language_choice=="3":#if 3 is selected for multiple Quotes
            language_for_multiple=input("1-English  2-Urdu : ")#chose language of quotes
            number_of_quotes=input("Enter Number of Quotes Below 45 : ")#as we have upto 45 Quotes 
            try:#will try tasks given in it if error comes will go to except without crashing programme otherwise it will run smoothly
                language_for_multiple=int(language_for_multiple)#converting string to int
                number_of_quotes=int(number_of_quotes)   #converting string to input
                if language_for_multiple==1 and number_of_quotes<46:# checking conditions
                    for i in range(0,number_of_quotes): #running for loop from 0 to given range by user
                        print(i+1,":",Quotes_English[i]) 
#in upper line we are first printing the numbers in every loop, +1 is used as i value in range is starting from 0 so we have to display 1
#in next sextion of upper code we are calling Quotes Enslish list and calling index number [] each time value of i will change in next loop
#with change of value of i in loop it will print next index number of list untill loop stops 
                if language_for_multiple==2 and number_of_quotes<46:
                    for i in range(0,number_of_quotes):
                        print(i+1,":",urdu_quotes[i])
#in upper line we are first printing the numbers in every loop, +1 is used as i value in range is starting from 0 so we have to display 1
#in next sextion of upper code we are calling Quotes Urdu list and calling index number [] each time value of i will change in next loop
#with change of value of i in loop it will print next index number of list untill loop stops 
                else:
                    print("\nPleasse Enter Correct Values \n") #if no if condition is true it mean there is invalid input according to condition
            except:
                print("\nEnter Valid Command\n")#if try function will give error this command will run
        elif language_choice=="exit":# if someone wants to exit
            print("Thanks for using Programme.\n")
            import multi_purpose_app#will iimport multipurpose app file from folder
            multi_purpose_app.main_multi()#will call maun_multi function in multi purpose app file in same folder
            break#will break the loop  for safety or to avoid any crash
        else:
            print("\nWrong Command Re-enter\n")#error handling if no valid command is entered programme will run again due to while loop
function_for_random_quote()#calling main function