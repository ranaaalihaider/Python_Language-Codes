def dictionary(word,operation):# function for printing words and meanings
    if operation==1:
        word = word.lower()
        word_list= word_data(word)#calling function to fetch word
        meaning_list=meaning_data(word)#calling function to fetch meanings
        for i in range(len(word_list)):
            print(word_list[i],": ",meaning_list[i])
    if operation==2:
        for i in range(97,123):
            word_list=word_data(chr(i))
            word_list.sort(reverse=True, key=len)
            meaning_list=meaning_data(chr(i))
            meaning_list.sort
            print("****",chr(i).upper(),"****")
            for y in range(len(word_list)):
                print(word_list[y],": ",meaning_list[y])
                
    if operation==3:
        word = word.lower()
        word_list= word_data(word)
        meaning_list=meaning_data(word)
        for i in range(len(word_list)):
            if word==word_list[i]:
                print(word.upper(),": ",meaning_list[i])
def word_data(word):#Word Database: fetch words
    
    if word[0]=='a':
        return ["able","agree","air","always","animal","apple","ask","aunt","awake","away"]
    elif word[0]=='b':
        return["ball","beautiful","big","book","bread","bring","brother","buy","busy","blue"]
    elif word[0]=='c':
        return ["car","care","cat","child","clear","cloud","coffee","color","cool","country"]
    elif word[0]=='d':
        return ["dance","dark","day","delight","doctor","dog","dollar","door","dive","dream"]
    elif word[0]=='e':
        return ["earth","easy","eat","elder","elephant""energy","enjoy","evening","excite","express"]
    elif word[0]=='f':
        return ["family","fast","finish","fire","flower","food","forest","free","friend","fun"]
    elif word[0]=='g':
        return ["game","garden","gift","glass","goal","good","grateful","green","group","grow"]
    elif word[0]=='h':
        return ["happy","hat","heart","help","high","hold","home","honest","hope","hot"]
    elif word[0]=='i':
        return ["idea","ice","import","imagine","information","inspire","interesting","improve","insect","include"]
    elif word[0]=='j':
        return ["joy","jump","journy","join","joke","jelly","jungle","judge","journal","just"]
    elif word[0]=='k':
        return ["kind","key","keep","knowledge","kick","kid","kitchen","king","kite","kindergarten"]
    elif word[0]=='l':
        return ["love","laugh","light","learn","listen","lion","lucky","leaf","lost","last"]
    elif word[0]=='m':
        return ["music","moon","move","mountain","mind","money","morning","mother","movie","map"]
    elif word[0]=='n':
        return ["nature","night","new","name","nose","near","nice","north","number","nightingale"]
    elif word[0]=='o':
        return ["open","ocean","old","orange","organize","owl","out","opportunity","over","ostrich"]
    elif word[0]=='p':
        return ["paper","park","peace","people","piano","pizza","plant","play","please","purple"]
    elif word[0]=='q':
        return ["quality","quantity","queen","quilt","quiet","quietly","question","questionnaire","quick","quote"]
    elif word[0]=='r':
        return ["rainbow","rain","read","red","rest","river","road","rabbit","rose","run"]
    elif word[0]=='s':
        return ["sea","sky","sleep","smile","song","spring","star","sun","sweet","swift"]
    elif word[0]=='t':
        return ["talk","tea","team","thank","tiger","time","train","travel","tree","true"]
    elif word[0]=='u':
        return ["ugly","umbrella","uncle","understand","universe","university","unique","up","upset","use"]
    elif word[0]=='v':
        return ["vacation","valuable","variety","vegetable","vehicle","velocity","venture","verdict","vibrant","victory"]
    elif word[0]=='w':
        return ["wait","wall","warm","water","weather","web","well","wild","win","write"]
    elif word[0]=='x': 
        return ["xanadu","xanthophyll","xenon","xenophobia","xerophyte","xerox","xylography","xylophone","x-axis","x-ray"]
    elif word[0]=='y':
        return ["yarn","yawn","year","yearn","yeast","yellow","yield","yoga","yogurt","yonder"]
    elif word[0]=='z':
        return ["zany","zeal","zebra","zenith","zephyr","zero","zest","zigzag","zone","zoom"]
    

def meaning_data(word):#Meaninig Database: fetch meanings
    if word[0]=='a':
        return ["having the power, skill, or means to do something.","to have the same opinion or be in harmony.","the invisible gaseous substance surrounding the earth.","at all times; on all occasions."," a living organism that feeds on organic matter.","a round fruit with red or green skin.","to inquire or request information.","the sister of one's father or mother.","at a distance from a particular place.","at a distance from a particular place."]
    elif word[0]=='b':
        return["A round object used in various sports and games.","Pleasing the senses or mind aesthetically; attractive.","Of considerable size or extent."," Of a color intermediate between green and violet, as of the sky or sea on a sunny day."," A written or printed work consisting of pages glued or sewn together along one side and bound in covers.","A staple food made from flour and water mixed together, usually with yeast or baking powder, and often with other ingredients such as fruit or sugar.","Take or go with (someone or something) to a place.","A man or boy in relation to other sons and daughters of his parents.","Having a great deal to do; occupied with tasks or activities.","Acquire in exchange for payment; purchase."]
    elif word[0]=='c':
        return ["a four-wheeled road vehicle that is powered by an engine.","a small domesticated carnivorous mammal.","a small domesticated carnivorous mammal.","a young human being below the age of puberty","easy to perceive, understand, or interpret.","a visible mass of water droplets or ice crystals suspended in the atmosphere.","a drink made from the roasted and ground bean-like seeds of a tropical shrub.","the property possessed by an object of producing different sensations on the eye as a result of the way the object reflects or emits light.","of or at a fairly low temperature.","a nation with its own government, occupying a particular territory."]
    elif word[0]=='d':
        return ["the time between sunrise and sunset.","move rhythmically to music, typically following a set sequence of steps.","having very little or no light.","a high degree of gratification or pleasure.","plunge headfirst into water with one's arms raised over one's head.","a qualified practitioner of medicine; a physician.","a domesticated carnivorous mammal.","the basic monetary unit of the US, Canada, Australia, and certain countries in the Pacific, Caribbean, Southeast Asia, Africa, and South America.","a hinged, sliding, or revolving barrier at the entrance to a building or room.","a series of thoughts, images, and sensations occurring in a person's mind during sleep."]
    elif word[0]=='e':
        return ["the planet on which we live.","achieved without great effort; presenting few difficulties.","put (food) into the mouth and chew and swallow it.","a person who is older than another.","a very large plant-eating mammal with a trunk, long curved ivory tusks, and large ears.","the strength and vitality required for sustained physical or mental activity.","take delight or pleasure in (an activity or occasion).","the period of time at the end of the day, usually from about 6 p.m. to bedtime.","cause strong feelings of enthusiasm and eagerness in someone.","convey (a thought or feeling) in words or by gestures and conduct."]
    elif word[0]=='f':
        return ["a group consisting of parents and children living together in a household.","moving or capable of moving quickly.","bring (a task or activity) to an end; complete.","the rapid oxidation of a material in the chemical process of combustion, releasing heat and light.","the reproductive part of a plant, often colorful and fragrant.","any nutritious substance that people or animals eat or drink to maintain life and growth.","a large area covered chiefly with trees and undergrowth.","not under the control or in the power of another; able to act or be done as one wishes.","a person whom one knows and with whom one has a bond of mutual affection.","enjoyment, amusement, or lighthearted pleasure."]
    elif word[0]=='g':
        return ["a form of play or sport, especially a competitive one.","a piece of ground, often near a house, used for growing flowers, fruit, or vegetables.","a thing given willingly to someone without payment.","a hard, brittle substance, typically transparent or translucent, made by fusing sand with soda and lime.","the object of a person's ambition or effort; an aim or desired result.","to be desired or approved of; having the required qualities.","feeling or showing an appreciation for kindness; thankful.","of the color between blue and yellow in the spectrum.","a number of people or things that are located close together or are considered or classed together.","undergo natural development by increasing in size or changing physically."]
    elif word[0]=='h':
        return ["feeling or showing pleasure or contentment.","a shaped covering for the head, typically with a crown and a brim.","a muscular organ in humans and animals that pumps blood through the circulatory system.","make it easier or possible for (someone) to do something by offering one's services or resources.","great, or greater than normal, in quantity, size, or intensity.","grasp, carry, or support with one's arms or hands.","the place where one lives permanently, especially as a member of a family or household.","free of deceit and untruthfulness; sincere.","a feeling of expectation and desire for a particular thing to happen.","having a high degree of heat or a high temperature."]
    elif word[0]=='i':
        return ["a thought or suggestion as to a possible course of action.","frozen water, a brittle transparent crystalline solid.","of great significance or value; likely to have a profound effect on success, survival, or well-being.","form a mental image or concept of something not present to the senses.","facts provided or learned about something or someone.","fill (someone) with the urge or ability to do or feel something, especially to do something creative.","arousing curiosity or interest; holding or catching the attention.","make or become better.","a small arthropod animal with six legs and a hard exoskeleton.","comprise or contain as part of a whole."]
    elif word[0]=='j':
        return ["a feeling of great pleasure and happiness.","propel oneself off the ground by using one's muscles, typically in one swift motion.","an act of traveling from one place to another.","cause to be in or form a connection or relation with.","a form of entertainment, consisting of telling jokes or amusing anecdotes.","a sweet, clear, or translucent fruit preserve.","an area of land overgrown with dense forest and tangled vegetation.","a public official appointed to decide cases in a court of law.","a daily record of news and events of a personal nature; a diary.","based on or behaving according to what is morally right and fair."]
    elif word[0]=='k':
        return ["having a friendly, generous, and considerate nature.","a small piece of shaped metal with incisions cut to fit the wards of a particular lock.","have or retain possession of.","facts, information, and skills acquired through experience or education.","strike or propel forcibly with the foot.","a child or young person.","a room or area where food is prepared and cooked.","the male ruler of an independent state, especially one who inherits the position by right of birth.","a toy consisting of a light frame with thin material stretched over it, flown in the wind at the end of a long string.","a school or class that prepares children for first grade."]
    elif word[0]=='l':
        return ["an intense feeling of deep affection.","make the spontaneous sounds and movements of the face and body that are the instinctive expressions of lively amusement.","the natural agent that stimulates sight and makes things visible.","gain or acquire knowledge or skill in (a subject or activity) by study, experience, or being taught.","give one's attention to a sound.","a large carnivorous feline mammal.","having, bringing, or resulting from good luck.","a flattened structure of a higher plant, typically green and blade-like, that is attached to a stem directly or via a stalk.","unable to find one's way; not knowing one's whereabouts.","coming after all others in time or order."]
    elif word[0]=='m':
        return ["vocal or instrumental sounds (or both) combined in such a way as to produce beauty of form, harmony, and expression of emotion.","the natural satellite of the Earth, visible by reflection of sunlight and having a slightly elliptical orbit.","go in a specified direction or manner; change position.","a large natural elevation of the earth's surface rising abruptly from the surrounding level; a large steep hill.","the element of a person that enables them to be aware of the world and their experiences, to think, and to feel.","a current medium of exchange in the form of coins and banknotes.","the period of time between midnight and noon, especially from sunrise to noon.","a woman in relation to her child or children.","a story or event recorded by a camera as a set of moving images and shown in a theater or on television; a film.","a diagrammatic representation of an area of land or sea showing physical features, cities, roads, etc."]
    elif word[0]=='n':
        return ["the phenomena of the physical world collectively, including plants, animals, the landscape, and other features and products of the earth.","the period of darkness in each twenty-four hours.","not existing before; made, introduced, or discovered recently or now for the first time.","a word or set of words by which a person or thing is known, addressed, or referred to.","the part of the human face or the forward part of the head of other animals, that contains the nostrils and organs of smell and forms the beginning of the respiratory tract.","at or to a short distance away; nearby.","pleasing; agreeable; delightful.","the direction in which a compass needle normally points, towards the horizon on the left-hand side of a person facing east.","an arithmetical value, expressed by a word, symbol, or figure, representing a particular quantity and used in counting and making calculations.","a small, thrush-like Old World songbird with a plain brownish plumage."]
    elif word[0]=='o':
        return ["allowing access, passage, or a view through an empty space.","a very large expanse of sea, in particular, each of the main areas into which the sea is divided geographically.","having lived for a long time; not young.","a round juicy citrus fruit with a tough bright reddish-yellow rind.","arrange systematically; order.","a nocturnal bird of prey with large eyes, a facial disc, a hooked beak, and typically a loud hooting call.","moving or appearing to move away from a particular place, especially one that is enclosed or hidden.","a set of circumstances that makes it possible to do something.","extending directly upwards from.","a large flightless fast-running bird native to Africa."]
    elif word[0]=='p':
        return ["A material manufactured in thin sheets from the pulp of wood or other fibrous substances.","A large public green area in a town used for recreation.","Freedom from disturbance; quiet and tranquility.","Human beings in general or considered collectively.","A large keyboard musical instrument with a wooden case enclosing a soundboard and metal strings, played by pressing keys that cause hammers to strike the strings.","A dish of Italian origin consisting of a flat, round base of dough baked with a topping of tomato sauce and cheese, typically with added meat or vegetables.","A living organism of the kind exemplified by trees, shrubs, herbs, grasses, ferns, and mosses.","Engage in activity for enjoyment and recreation rather than a serious or practical purpose.","Used to ask for something in a polite way.","A color intermediate between red and blue."]
    elif word[0]=='q':
        return ["The standard of something as measured against other things of a similar kind.","The amount or number of a material or immaterial thing not usually estimated by spatial measurement.","The female ruler of an independent state.","A warm bed covering made of padding enclosed between layers of fabric and kept in place by lines of stitching.","Making little or no noise.","With little or no noise.","A sentence worded or expressed so as to elicit information.","A set of printed or written questions with a choice of answers.","Moving fast or doing something in a short time.","Repeat or copy out (a group of words from a text or speech), typically with an indication that one is not the original author or speaker."]
    elif word[0]=='r':
        return ["A meteorological phenomenon that is caused by reflection, refraction, and dispersion of light in water droplets, resulting in a spectrum of light appearing in the sky.","Moisture condensed from the atmosphere that falls visibly in separate drops.","Look at and comprehend the meaning of (written or printed matter) by interpreting the characters or symbols of which it is composed.","Of a color at the end of the spectrum next to orange and opposite violet."," Cease work or movement in order to relax, refresh oneself, or recover strength.","A large natural stream of water flowing in a channel to the sea, a lake, or another such stream.","A wide way leading from one place to another, especially one with a specially prepared surface that vehicles can use.","A small burrowing mammal with long ears, soft fur, and a short tail.","A prickly bush or shrub that typically bears red, pink, yellow, or white fragrant flowers.","Move at a speed faster than a walk, never having both or all the feet on the ground at the same time."]
    elif word[0]=='s':
        return ["The expanse of saltwater that covers most of the Earth's surface and surrounds its landmasses.","The region of the atmosphere and outer space seen from the Earth.","A condition of body and mind that typically recurs for several hours every night.","Form one's features into a pleased, kind, or amused expression.","A short poem or other set of words set to music or meant to be sung."," The season after winter and before summer, in which vegetation begins to appear.","A fixed luminous point in the night sky that is a large, remote incandescent body like the sun.","The star around which the Earth orbits, providing light and warmth to the Earth.","Having the pleasant taste characteristic of sugar or honey; not salty, sour, or bitter.","Form one's features into a pleased, kind, or amused expression."]
    elif word[0]=='t':
        return ["Speak in order to give information or express ideas or feelings.","A hot drink made by infusing the dried crushed leaves of the tea plant in boiling water.","A group of players forming one side in a competitive game or sport.","Express gratitude to someone by saying thank you.","A large carnivorous feline mammal with a yellow-brown coat striped with black.","The indefinite continued progress of existence and events in the past, present, and future regarded as a whole.","A connected series of railroad cars with or without a locomotive."," Make a journey, typically of some length or abroad.","A woody perennial plant, typically having a single stem or trunk supporting branches and leaves.","In accordance with fact or reality; accurate or exact."]
    elif word[0]=='u':
        return ["unpleasant or repulsive, especially in appearance","A device consisting of a circular canopy of cloth on a folding metal frame supported by a central rod, used as protection against rain.","The brother of one's father or mother or the husband of one's aunt.","Perceive the intended meaning or significance of.","All existing matter, space, and energy considered as a whole.","All existing matter, space, and energy considered as a whole.","Being the only one of its kind; unlike anything else.","Moving or situated higher in position or status.","Make someone unhappy, disappointed, or worried.","The action of using something or the state of being used for a purpose."]
    elif word[0]=='v':
        return ["A period of time devoted to pleasure, rest, or relaxation, especially one with pay granted to an employee.","Having considerable monetary worth; something that is of great worth or importance.","The quality or state of being different or diverse; a collection or assortment of different things.","A plant or part of a plant used as food, typically as an accompaniment to meat or fish.","A means of transporting goods or passengers, such as a car, bus, or bicycle.","The speed of an object in a particular direction.","A risky or daring journey or undertaking.","A formal decision or judgment on a matter.","Full of energy and enthusiasm; lively.","The overcoming of an enemy or antagonist; success in a contest or struggle."]
    elif word[0]=='w':
        return ["Stay where one is or delay action until a particular time.","A continuous vertical brick or stone structure that encloses or divides an area of land.","Of or at a fairly or comfortably high temperature; having, showing, or expressive of enthusiasm, affection, or kindness.","A colorless, transparent, odorless, and tasteless liquid that forms the seas, lakes, rivers, and rain.","The state of the atmosphere at a particular place and time, as regards heat, cloudiness, dryness, sunshine, wind, rain, etc.","A complex system of interconnected elements, especially one perceived as a trap or danger.","In a good or satisfactory way.","Occurring, growing, or living in a natural state; not domesticated or cultivated.","Be successful or victorious in a contest or competition.","Mark (letters, words, or other symbols) on a surface, typically paper, with a pen, pencil, or similar implement."]
    elif word[0]=='x': 
        return ["An idyllic, beautiful place.","A yellow or brown carotenoid pigment in plants.","A chemical element with the symbol Xe and atomic number 54, a colorless, dense, odorless noble gas.","Intense or irrational dislike or fear of people from other countries.","A plant adapted to grow in conditions of aridity (dry conditions).","To make a copy of (a document) using a xerographic process.","The art of engraving on wood, especially in Chinese, Japanese, or Korean styles.","A musical instrument consisting of a set of wooden bars of different lengths that are struck with mallets to produce musical tones.","The horizontal line on a graph.","A form of electromagnetic radiation used to penetrate objects, especially for medical examination or treatment."]
    elif word[0]=='y':
        return ["Fiber used for knitting, weaving, or sewing.","Involuntarily open one's mouth wide and inhale deeply due to tiredness or boredom.","The time taken by a planet to make one revolution around the sun.","Have an intense longing or desire.","A microscopic fungus consisting of single oval cells that reproduce by budding and are capable of converting sugar into alcohol and carbon dioxide.","Of the color between green and orange in the spectrum.","Produce or provide (a natural, agricultural, or industrial product).","A Hindu spiritual and ascetic discipline, a part of which, including breath control, simple meditation, and the adoption of specific bodily postures, is widely practiced for health and relaxation.","A semisolid sourish food prepared from milk fermented by added bacteria, often sweetened and flavored.","At some distance in the direction indicated; over there."]
    elif word[0]=='z':
        return ["Amusingly unconventional and idiosyncratic.","Great energy or enthusiasm in pursuit of a cause or an objective.","An African wild horse with black-and-white stripes and an erect mane.","The time at which something is most powerful or successful.","A soft, gentle breeze.","The numerical symbol 0, representing the absence of quantity; nothing.","Great enthusiasm and energy.","A line or course having abrupt alternate right and left turns.","An area or stretch of land having a particular characteristic, purpose, or use.","Move or travel very quickly."]
def dictionary_main_function():# main function of dictionary
    while True:# keeps the loop running
        try:#error handling 
            print("For charachter search press: 1\nFor whole dictionary press: 2\nFor word search press: 3\nTo exit press: 0")
            operation=eval(input())#takes input for operation to be performed
            if operation==1:
                while True:#keeps the loop running
                    word=input("Enter your Character: ").lower()#takes input and convert to lower case
                    if 'a'<= word <='z':#check the character input
                        dictionary(word,operation)#calls the main function of dictionary
                        break#exit the loop
                    else:
                        print("Invalid Alphabet!")
            elif operation==2:
                dictionary("",operation)
            elif operation==3:
                while True:
                    word=input("Enter your word: ").lower()
                    if 'a'<= word[0] <='z':
                            dictionary(word,operation)
                            operationn=eval(input("To Search again: 1\nTo Stop Press: 0\n"))
                            if operationn==0:
                                break
                            if operationn!=1:
                                print("Invalid input!")
                                continue
                    else:
                        print("Invalid Alphabet!")
            elif operation==0:
                print("Good Bye")
                import multi_purpose_app
                multi_purpose_app.main_multi()
                break
            else:
                print("Invalid Input. Try again")
        except:
            print("\nWrong Inputs \n")
dictionary_main_function()
