import random
print("Welcome to Tic-Tac-Toe game")
game_mode=int(input("Chose Mode to Play Game \n 1-Multiplayer   2-With Computer : " ))
chart=[[" "," "," "],[" "," "," "],[" "," "," "]]
length=len(chart)
winner_status=False
#Asking to play again
def play_again():
    global chart
    choice=int(input("Enter 1 to Play Agin 0 to Exit : "))
    if choice==1:
        print("Lets Start Again ")
        #Method 1 to reset
        for i in range (length):
            for j in range(length):
                chart[i][j]=" "
        #Method 2 to reset is commented
        #chart=[[" "," "," "],[" "," "," "],[" "," "," "]]
        game_function()
    else:
        exit()
#Chart Printer Function
def chart_printer():
    print("\t\t\t\t\t\t C0   C1   C2\n")
    for i in range(length):
        print("\t\t\t\t\t\t",end="")
        for x in range(len(chart[i])):
            print("",chart[i][x],end=" | ")
        print(" R",i)
def winner_checker():
    X_Statement="\n ****Congratulations****  Player X is Winner \n"
    O_Statement="\n ****Congratulations****  Player O is Winner \n"
    for a in range(length):
        for b in range(len(chart[a])):
            if chart[a][0]==chart[a][1]==chart[a][2]=="X":
                print(X_Statement)
                chart_printer()
                play_again()
            elif chart[0][b]==chart[1][b]==chart[2][b]=="X":
                print(X_Statement)
                chart_printer()
                play_again()
    for a in range(length):
        for b in range(len(chart[a])):
            if chart[a][0]==chart[a][1]==chart[a][2]=="O":
                print(O_Statement)
                play_again()
            elif chart[0][b]==chart[1][b]==chart[2][b]=="O":
                print(O_Statement)
                play_again()
    if chart[0][0]==chart[1][1]==chart[2][2]=="X":
                print(X_Statement)
                chart_printer()
                play_again()
    elif chart[0][0]==chart[1][1]==chart[2][2]=="O":
                print(O_Statement)
                chart_printer()
                play_again()
    elif chart[0][2]==chart[1][1]==chart[2][0]=="X":
                print(X_Statement)
                chart_printer()
                play_again()
    elif chart[0][2]==chart[1][1]==chart[2][0]=="O":
                print(O_Statement)
                chart_printer()
                play_again()
#Function Asking from user to Enter
def game_function():
    count=1
    while True:
        if count>9:
            print("Thanks Match Draw")
            play_again()
        if count%2 !=0:
            print("Player X Turn")
            row=int(input("Enter Row Number (0,1,2) : "))
            while row>2:
                print("Wrong Entry Enter Again ")
                row=int(input("Enter Row Number (0,1,2) : "))
            colum=int(input("Enter Colum Number (0,1,2) : "))
            while colum>2:
                print("Wrong Entry Enter Again ")
                colum=int(input("Enter Colum Number (0,1,2) : "))
            if chart[row][colum]==" ":
                chart[row][colum]="X"
                winner_checker()
                count=count+1        
            else:
                print("Wrong Entry")
            chart_printer()

        else:
            if game_mode==2:
                print("Player O Turn")
                row=random.randint(0,2)
                colum=random.randint(0,2)
                while chart[row][colum]!=" ":
                    row=random.randint(0,2)
                    colum=random.randint(0,2)
                chart[row][colum]="O"
                winner_checker()
                count=count+1
                chart_printer()

            elif game_mode==1:
                print("Player O Turn")
                row=int(input("Enter Row Number (0,1,2) : "))
                while row>2:
                    print("Wrong Entry Enter Again ")
                    row=int(input("Enter Row Number (0,1,2) : "))
                colum=int(input("Enter Colum Number (0,1,2) : "))
                while colum>2:
                    print("Wrong Entry Enter Again ")
                    colum=int(input("Enter Colum Number (0,1,2) : "))
                if chart[row][colum]==" ":
                    chart[row][colum]="O"
                    winner_checker()
                    count=count+1
                else:
                    print("Wrong Entry")
                chart_printer()
game_function()

