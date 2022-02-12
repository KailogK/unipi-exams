from random import randint

def showTable(x): #                                           \
    print () #                                                 \
    print (" ===== BEGINNING OF TABLE =====") #                 \
    print () #                                                   \
    print (" ",x[0]," ",x[1]," ",x[2]," ") # \                    \
    print ()                               #  \                    \
    print ()                               #   \                    | FUNCTION MADE FOR SHOWING
    print (" ",x[3]," ",x[4]," ",x[5]," ") #    } 9 "ringholders"   | GAME RESULTS WITH DETAILS
    print ()                               #   /                   /
    print ()                               #  /                   /
    print (" ",x[6]," ",x[7]," ",x[8]," ") # /                   /
    print () #                                                  /
    print (" ======== END OF TABLE ========") #                /
    print () #                                                /

def checkTable(x):
    combs = [["o", "0", "O"], ["O", "0", "o"], ["o", "o", "o"], ["0", "0", "0"], ["O", "O", "O"]] # all of needed combinations with "o", "0", "O"
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if (([x[0][i], x[1][j], x[2][k]] in combs) or ([x[3][i], x[4][j], x[5][k]] in combs) or ([x[6][i], x[7][j], x[8][k]] in combs)): # checking every row (1st,2nd,3rd)
                    return "rows"
                if (([x[0][i], x[3][j], x[6][k]] in combs) or ([x[1][i], x[4][j], x[7][k]] in combs) or ([x[2][i], x[5][j], x[8][k]] in combs)): # checking every collumn (1st,2nd,3rd)
                    return "collumns"
                if (([x[0][i], x[4][j], x[8][k]] in combs) or ([x[2][i], x[4][j], x[6][k]] in combs)): # checking in the form of X ("ringholders": 1st,5th,9th or 3rd,5th,7th)
                    return "X"

print ()
print ("Description: 100 randomly played games with 3 sized rings (small, medium, large).")
print ("A game is won by having rings with same size horizontally, vertically or diagonally \n or from smallest to largest and reversed.")
print ("Before we continue choose an option: 1) show just the results | 2) show every game with details")
choice=str(input("Option: "))
while (choice != "1" and choice != "2"):
    choice=str(input("Please give option between 1 and 2: "))
rings = ["o","0","O"] #ring array - [small, medium, large]
totalsteps = 0
for i in range(100):
    ringtable = [[" ", " ", " "] for j in range(9)] # initializing empty ringtable for every game
    steps = 0                                       # same with steps
    win = False
    while (win == False):
        randomnum1 = randint(0,8)
        if (" " in ringtable[randomnum1]):
        #checking if there's empty space in the selected "ringholder"

            randomnum2 = randint(0,2)
            if (rings[randomnum2] not in ringtable[randomnum1]):
            #checking if selected ring is not in the selected "ringholder"

                if (rings[randomnum2] == "o"):     # \
                    ringtable[randomnum1][0] = "o" #  \
                elif (rings[randomnum2] == "0"):   #   | sorting
                    ringtable[randomnum1][1] = "0" #   | rings by size
                else:                              #  /
                    ringtable[randomnum1][2] = "O" # /

                steps += 1
                winner = checkTable(ringtable)
                if (winner == "rows" or winner == "collumns" or winner == "X"):
                    win = True
                    totalsteps += steps
                    if (choice == "2"):                                    # \
                        print ("for game:", i+1, "   total steps:", steps) #  \
                        if (winner == "rows"):                             #   \
                            print ("winning combination: rows")            #    \
                        elif (winner == "collumns"):                       #     } showing every game with details
                            print ("winning combination: collumns")        #    /
                        else:                                              #   /
                            print ("winning combination: \ or /")          #  /
                        showTable(ringtable)                               # /

print ("===== RESULTS =====")
print ()
print ("For 100 randomly played games we have:")
print ("Total steps:", totalsteps)
print ("Average steps per game:", totalsteps//100)
if (choice == "2"):
    print ("NOTE: every array can hold 3 rings with different sizes each. \n In every example above, rings are sorted from smallest to largest")
print ()
x=str(input("Type anything to quit: "))
