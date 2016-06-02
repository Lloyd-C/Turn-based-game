import random #Make sure a random number can be accessed for the dice roll
import time
names=['Player 1', 'Player 2', False, 4] #Make these the default names

#Task 1 - Display a main menu for the program
print('Welcome to AQADo!')#Greet the user
def Menu(names):#Show the menu to the user
    position=[1, 1, 1, 1]#Make a list containing the positions of the counters
    turn=True #Set a value to show who's turn it is
    choice=input('''What would you like to do?
        1. Enter player names
        2. Play game
        3. Quit
        4. View instructions
        5. Play with a five-sided die
        6. Play with a computer\n''')#Show the menu to the user and allow them to enter their option
    while choice!='1' and choice!='2' and choice!='3' and choice!='4' and choice!='5' and choice!='6':#Validate the input
        print('Please enter a valid answer: 1, 2, 3, 4, 5 or 6')
        choice=input('''What would you like to do?
        1. Enter player names
        2. Play game
        3. Quit
        4. View instructions
        5. Play with a five-sided die
        6. Play with a computer\n''')
    if choice=='1':#Ask the user to enter their names if they choose to do so
        (names)=Names()
    if choice=='2' or choice=='5' or choice=='6':#Allow the user to start the game
        turn=True #Set a value to show who's turn it is
        position=[1, 1, 1, 1]#Make a list containing the positions of the counters
        if choice=='6':
            names[1], names[2]='CPU', True
        elif choice=='5':
            names[3]=5
        Play(names, turn, position)
    elif choice=='3':#Allow the user to quit the game
        exit()
    elif choice=='4':#Allow the user to view the instructions
        Instructions()
    Menu(names) #Return to the main menu

def Instructions():#Display the instructions
    print('''The players take it in turns to roll a four-sided die
The result of the die roll determines the move that you are allowed to make on the board
e.g. if you roll a 1, you can move one of your pieces one space nearer to FINISH
However, if you roll a 4, you move one of your pieces one space back towards START
The aim of the game is to move both of the player\'s pieces to the end of the 11-space board
If your piece lands on a space with an opponent’s piece on, then the opponent’s piece is moved back to START
BUT, a piece on a safe space cannot be sent back to START
You can\'t move your piece onto a space already that has your other piece on unless the space is a safe space
A piece cannot move backwards if it is on START or forwards if it is on FINISH
If a player can make a move then they must do so
A player wins the game when both of their pieces are on FINISH\n''')

#Task 2 - Allow the players to enter their names.
def Names():
    names[0]=input('Please enter the name of player 1: ')#Allow the users to enter their names
    names[1]=input('Please enter the name of player 2: ')
    while names[0]==names[1]:#Make sure that they don't enter the same name twice
        print('Please do not enter the same name twice...')
        names[0]=input('Please enter the name of player 1: ')
        names[1]=input('Please enter the name of player 2: ')
    return(names)

#Task 3 - Display the board
def Play(names, turn, position):
    for count in range(11, 0, -1):#Create a for loop with a negative stride so that it counts downwards (11 is at the top)
        array=['X', 'X', 'O', 'O'] #Make an array containing the 4 counters
        for counter in range(4):#Make a for loop that loops 4 times
            if position[counter]!=count:#If the space number isn't the position of the counter...
                array[counter]='  ' #Change the counter of this space for that column to an empty space
        if count==5 or count==4 or count==1 or count==11 or count==10:#Print this if there is a safe space line (asterisk) above it
            print('*'*29+'\n|  '+str(count)+'  |  '+array[0]+'  |  '+array[1]+'  |  '+array[2]+'  |  '+array[3] +'  |')
        else:#Print this if there is a safe space line above it (dash line)
            print('--'*13+'\n|  '+str(count)+'  |  '+array[0]+'  |   '+array[1]+'  |  '+array[2]+'  |  '+array[3] +'  |')
    print('*'*29) #Print the final asterisked line at the end
    Win(position)#Run the funtion that checks if the player has won
    Dice(names, turn, position)

#Task 4 - Generate a random number to simulate the rolling of a four-sided die
def Dice(names, turn, position):
    roll=random.randint(1, names[3])#Generate a radom number
    if turn==True:#Display the dice roll and the player that the message is directed towards
        print(str(names[0])+' got '+str(roll)+' on the dice roll!')
    else:
        print(str(names[1])+' got '+str(roll)+' on the dice roll!')
    if roll==4:#Make the die roll -1 if it rolls a 4 so that it goes back one space
        roll=-1
    if names[2]==True and turn==False:
        CPU(position, roll, names, turn)
    else:
        if turn==True:
            valid=[Check(position, 1, roll), Check(position, 2, roll)]#Check if player1's pieces can be moved
        else:
            valid=[Check(position, 3, roll), Check(position, 4, roll)]
        if valid[0]==False and valid[1]==False:#If neither of the pieces can move, swap goes and display board
            print('Neither of your pieces can be moved...'), time.sleep(1)
            turn = not turn#Swap turns
            Play(names, turn, position)#Print the board again
        if valid[1]==False:#If only piece 1 can, tell the user and swap goes
            print('Piece 2 cannot be moved\n')
        elif valid[0]==False:#If only piece 2 can, tell the user and swap goes
            print('Piece 1 cannot be moved\n')
    Select(roll, position, names, turn)

#Task 5 - Check if the result of the die roll will allow a player to move either of their pieces
def Check(position, move, roll):
    if roll==5:
        i=1
        while position[move-1]+i<12:
            if position[move-1]+i==position[0] or position[move-1]+i==position[1] or position[move-1]+i==position[2] or position[move-1]+i==position[3]:
                i+=1
            else:
                return i
        return i-1
    if position[move-1]+roll!=5 and position[move-1]+roll!=1 and position[move-1]+roll!=11:#Do the following if not on a safe space
        if ((position[move-1]+roll)<1 or (position[move-1]+roll)>11):#Make sure that it won't go under 1 or over 11
            return(False)
        if move-1==0 and position[0]+roll==position[1]:#Make sure that it won't equal the other piece of that player
            return(False)
        elif move-1==1 and position[1]+roll==position[0]:#Make sure that it won't equal the other piece of that player
            return(False)
        elif move-1==2 and position[2]+roll==position[3]:#Make sure that it won't equal the other piece of that player
            return(False)
        elif move-1==3 and position[3]+roll==position[2]:#Make sure that it won't equal the other piece of that player
            return(False)#If the piece cannot be moved, return a False boolean value
    return(True)#If the piece cannot be moved, return a True boolean value

#Task 6 - Allow the player to select which one of their pieces they want to move
def Select(roll, position, names, turn):
    valid, move=Valid(turn, position, roll)
    while valid==False:#Validate the input by checking if that piece can be moved
        print('\nThat piece cannot be moved...')
        valid, move=Valid(turn, position, roll)
    Make_move(move, roll, position, names, turn, valid)
def Valid(turn, position, roll):
    move=input('Which piece would you like to move? ') #Ask the user what piece they want to move
    while (move!='1' and move!='2'):#Validate the input
        print('\nPlease enter a valid option (1 or 2)...')
        move=input('Which piece would you like to move? ')
    move=int(move)#Change it to an integer so that the number can be changed easily
    if turn==False:#Add 2 to player 2's piece moves, as theirs is 2 to the right of player 1's
        move+=2
    valid=Check(position, move, roll)
    return valid, move

#Task 7 - Make the legal move selected by the player
def Make_move(move, roll, position, names, turn, valid):
    if isinstance(valid, bool)==False:
        position[move-1]=position[move-1]+valid
    else:
        position[move-1]=position[move-1]+roll#Change the position of the counter
        if position[move-1]!=5 and position[move-1]!=11:#Do the following when not on a safe space
            if (move-1==0 or move-1==1) and (position[move-1]==position[2]):#Check if any of player 1's pieces are on player 2's piece 1
                position[2]=1#If so, take the opponent's piece back to the start
            elif (move-1==0 or move-1==1) and (position[move-1]==position[3]):#Check if any of player 1's pieces are on player 2's piece 2
                position[3]=1#If so, take the opponent's piece back to the start
            elif (move-1==2 or move-1==3) and (position[move-1]==position[0]):#Check if any of player 2's pieces are on player 1's piece 1
                position[0]=1#If so, take the opponent's piece back to the start
            elif (move-1==2 or move-1==3) and (position[move-1]==position[1]):#Check if any of player 2's pieces are on player 1's piece 2
                position[1]=1#If so, take the opponent's piece back to the starts
    turn=not turn#Swap the turn to the other player
    Play(names, turn, position)#If no one has won, the code prints the board again

#Task 8 - Check if a player has won the game after each move
def Win(position):
    if position[0]==11 and position[1]==11:#Check if player 1 has won
        print('\nCongratulations! '+ str(names[0])+' has won!\n'), time.sleep(1)#Display a congratulations message if player 1 has won
        Menu(names) #Return to the main menu
    if position[2]==11 and position[3]==11:#Check if player 2 has won
        print('\nCongratulations! '+ str(names[1])+' has won!\n'), time.sleep(1)#Display a congratulations message if player 2 has won
        Menu(names) #Return to the main menu

#Extra - Allow the user to play with a computer
def CPU(position, roll, names, turn):
    valid=[Check(position, 3, roll), Check(position, 4, roll)]
    if valid[0]==False and valid[1]==False:
        turn=not turn
        print('Neither of the CPU\'s pieces could be moved'), time.sleep(1)
        Play(names, turn, position)#Print the board again
    if position[2]==11 and valid[1]==True:#Don't move piece 1 if it is on 11
        Move(roll, position, names, turn, valid, 3)
    elif position[3]==11 and valid[0]==True:#Don't move piece 2 if it is on 11
        Move(roll, position, names, turn, valid, 4)
    if position[2]+roll==11 and valid[0]==True:#Check if piece 1 lands on FINISH
        Move(roll, position, names, turn, valid, 3)
    if position[3]+roll==11 and valid[1]==True:#Check if piece 2 lands on FINISH
        Move(roll, position, names, turn, valid, 4)
    if position[2]+roll==position[0] or position[2]+roll==position[1] and valid[0]==True:#Check if piece 1 lands on another player's piece
        Move(roll, position, names, turn, valid, 3)
    if position[3]+roll==position[0] or position[3]+roll==position[1] and valid[1]==True:#Check if piece 2 lands on another player's piece
        Move(roll, position, names, turn, valid, 4)
    if position[2]+roll==5 or position[2]+roll==1 and valid[0]==True:#Check if piece 1 lands on a safe space
        Move(roll, position, names, turn, valid, 3)
    if position[3]+roll==5 or position[3]+roll==1 and valid[1]==True:#Check if piece 2 lands on a safe space
        Move(roll, position, names, turn, valid, 4)
    if valid[0]==False:
        move=4
    else:
        move=3
    if valid[0]==True and valid[1]==True:
        move=random.randint(3, 4)#Generate a random number
    Move(roll, position, names, turn, valid, move)
def Move(roll, position, names, turn, valid, move):
    valid=True
    print('The CPU moved piece ' + str(move-2)+' to space '+str(position[move-1]+roll)), time.sleep(1)
    Make_move(move, roll, position, names, turn, valid)
Menu(names)
