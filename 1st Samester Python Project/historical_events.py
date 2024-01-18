#List of Events
#database for events 
historical_events =[
    {'1066': 'Battle of Hastings. This battle, led by William the Conqueror, saw the Normans defeat the Anglo-Saxons, changing the course of English history.'},
    {'1348': "Black Death arrives in Europe. The bubonic plague, one of history's deadliest pandemics, devastated Europe, resulting in widespread death and societal upheaval."},
    {'1453': 'Fall of Constantinople. The city fell to the Ottoman Empire, marking the end of the Byzantine Empire and the beginning of the Ottoman era.'},
    {'1492': "Christopher Columbus arrives in the Americas. Columbus's voyage opened the Age of Exploration and initiated European colonization of the Americas."},
    {'1517': 'Martin Luther nails his 95 Theses. This act in Wittenberg, Germany, sparked the Protestant Reformation, challenging the authority of the Catholic Church.'},
    {'1588': 'The Spanish Armada is defeated by the English fleet. This event marked a significant victory for England over Spain, enhancing English naval power.'},
    {'1770': 'Boston Massacre. A clash between British soldiers and American colonists, fueling anti-British sentiment in the lead-up to the American Revolution.'},
    {'1776': 'Declaration of Independence signed. It marked the birth of the United States of America, declaring independence from British rule.'},
    {'1789': 'Storming of the Bastille in Paris. A key event of the French Revolution, symbolizing the overthrow of the monarchy.'},
    {'1804': 'Lewis and Clark begin their expedition. The Corps of Discovery, led by Meriwether Lewis and William Clark, explored the newly acquired Louisiana Territory.'},
    {'1815': "Battle of Waterloo. Napoleon's final defeat, ending his rule as Emperor of France and marking the end of the Napoleonic Wars."},
    {'1863': 'Gettysburg Address delivered by Abraham Lincoln. A speech given during the American Civil War, emphasizing the principles of democracy and equality.'},
    {'1914': 'Assassination of Archduke Franz Ferdinand. The event that triggered World War I by igniting tensions between European powers.'},
    {'1917': 'October Revolution in Russia. The Bolsheviks, led by Lenin, overthrow the provisional government, leading to the establishment of the Soviet Union.'},
    {'1929': 'Wall Street Crash. The stock market collapse leading to the Great Depression, causing economic turmoil worldwide.'},
    {'1945': 'Atomic bomb dropped on Hiroshima. The first use of nuclear weapons in warfare during World War II.'},
    {'1947': 'India gains independence from British rule. Marks the end of British colonialism in India after a long struggle for freedom.'},
    {'1963': "Martin Luther King Jr. delivers 'I Have a Dream' speech. A defining moment in the American Civil Rights Movement."},
    {'1969': 'First Moon Landing by Apollo 11. Neil Armstrong becomes the first person to walk on the moon.'},
    {'1989': 'Fall of the Berlin Wall. Symbolized the end of the Cold War and the reunification of East and West Germany.'},
    {'2001': '9/11 terrorist attacks in the United States. Al-Qaeda hijackers crash planes into the World Trade Center and the Pentagon.'},
    {'2011': 'Death of Osama bin Laden. The founder of Al-Qaeda is killed by U.S. Special Forces in Pakistan.'},
    {'2016': 'Brexit referendum. The United Kingdom votes to leave the European Union.'},
    {'2020': 'World Health Organization declares COVID-19 a pandemic. The coronavirus outbreak is declared a global health crisis.'}
]
#Function for searching event
def historical_event_function():
    while True:#will continue this function untill break
        print("Enter 1 to See List Of Available Years \nEnter 2 to search in Range 1066 to 2020 \nEnter Year to check event Availabe or not  \nExit for main page")
        date=str(input("Enter Date to Search For Event : "))
        if date=="1":
            print(len(historical_events))
            print("1066   1348   1453   1492   1517   1588   1770   1776   1789   1804   1815   1863   \n1914   1917   1929   1945   1947   1963   1969   1989   2001   2011   2016   2020")
        elif date=="2":
            rangr_entry_status=True
            range1=str(input("Enter Starting Range : "))
            range2=str(input("Enter Ending Range : "))
            try:#converting ranges into int 
                range1=int(range1)
                range2=int(range2)
            except:
                print("Please Enter Valid Commands ")
                rangr_entry_status=False
            if rangr_entry_status==True:
                for x in range(len(historical_events)):
                    for dates in range(range1,range2+1):
                        dates=str(dates)
                        if dates in historical_events[x]:
                            print(dates," : ",historical_events[x][dates])
        elif date=="exit":
            print("Thanks for using event viewer\n")
            import multi_purpose_app
            multi_purpose_app.main_multi()
            break
        else:    
            for x in range(len(historical_events)):
                if date in historical_events[x]:
                    print("\nYour Historical Event of Year ",date,"is:\n",historical_events[x][date],"\n")
#calling function to perform task
historical_event_function()