
   
import turtle                                    
from defs import *

            
        
def main():
    while(1): # runs the program endlessly, this is the main game loop
        
        space(100)    # clears the screen by scrolling down 100 lines  
            
        print("---------PLAYER 1---------")
        space(1)
        print("(Make sure PLAYER 2 is not peaking)")

        lengthOfword = 14 # intilizes the variable wiht the length of the letter

        while lengthOfword >= 14 or lengthOfword < 4 :     # loop to prevent words with more than 13 letters or less than 4 letters beign entered  
                                                           # Also prevents the player form entering no word at all                                                     
            space(1)                                       # if the word does not follow the condtions, player 1 will be asked to enter another word                             
            wordtoGuess=str(input("Enter your word (if it has a space, use '-', e.g. ice-cream, maximum of 13 letters and a minimum of 4) : ")) # takes input
                                                                                                                                            # as a string        
            lengthOfword= int(len(wordtoGuess)) # takes the length as a integer
        
            if lengthOfword >=14: # limiting the letter count to 13 to prevent the game from being too hard  
                space(1)
                print("Sorry this word is too long. Please enter word with less than 13 letters.")

            if lengthOfword == 0:
                space(1)
                print("You have not entered a word. Please enter a word.") 
            
            if lengthOfword < 4 and lengthOfword > 0: # requiring a word with alteast 4 letters so the game is not too easy
                space(1)
                print("The word is too short. Please enter a word with at least 4 letter")


    

        letterList = ["N"]*lengthOfword # intializes the list to store each letter of the word
        letterMask = ["*"]*lengthOfword # this variable will be used for "masking" the letters
        qResult = False                 # this variable will be used check if the player's answer was correct or not    
                                        # with the help of the letterCheck function  
        playerWin = False               # this will be used to find out if the player won or not
    
        wrongGuessspace = 0
        letterAssignment(lengthOfword,letterList,wordtoGuess) # uses the assignment function to store each letter as list to the letterList variable

        letterCheck("-", letterList,letterMask,lengthOfword) # overwrites the mask for word with space, and thus "-" inbetween
        
        playerAttempts = 8 # the number of attempts. if it reaches zero, the player loses

        turtle.title("Guess The Word Game")  # sets the game screen at a resolution of 600x700  
        turtle.setup(600,700,880,50)         # towards the right of the screen with a yellow background
        turtle.bgcolor("yellow")

        # declares four turtles, each having a different function for the sake of simplicity and to remove any confusion
        t1 = turtle.Turtle() # to draw the word mask and the letters of the given word if the player gets the guess correct(which must be reflected by clearing turtle and drawing again)
        t2 = turtle.Turtle() # to draw the attempts counter at the bottom the screen(which also must be cleared each time the player gets a wrong guesss and rewritten) 
        t3 = turtle.Turtle() # to draw the text that doesn't need to be changed. e.g the "Guess the Word" title
        s1 = turtle.Turtle() # to draw shapes, specifically the parts of the ambulance each time the player gets a guess wrong
        
        space(100)# like above, "clears the screen" 

    
        print("---------PLAYER 2---------")
        space(1)

        while(playerAttempts > 0): # loop than runs until the player has 0 attempts left, the sub game loop

            textDraw(t3,2,0,0,0,"Guess the Word:",20,"Courier","left","bold",-290,280,"blue",2) # draws heading line
            textDraw(t1,1,lengthOfword,0,46,letterMask,20,"Courier","left","bold",-290,240,"blue",2) # draws the mask(and each letter of the word) with even spacing between each letter
            textDraw(t2,2,0,0,0,"You have "+str(playerAttempts)+" attempts remaining",15,"Courier","center","italic",-15,-340,"blue",2) # draws the player attempts with the player attempts variable
            textDraw(t3,2,0,0,0,"Wrong Guesses:",20,"Courier","center","italic",-180,-200,"blue",2) #draws wrong guesses title

            playerinputLength = 2 # for input validation, so the player doesn't enter more than 1 letter or no letter at all that will get proccessed

            while(playerinputLength >= 2 or playerinputLength == 0): # validation loop similar to the word length validation loop above

                
                playerInput = str(input("Enter a letter: "))
                space(1)
                playerinputLength = int(len(playerInput))

                if(playerinputLength > 1): # if the player enters more than 1 letter
                    print("You have entered more than one letter. Please enter a single letter.")
                    space(1)

                if(playerinputLength == 0): # if the player enters no letter, and just presses enter. Helpful if the player presses enter by accident
                    print("You have not entered a letter. Please enter a letter")
                    space(1)
      
            qResult = letterCheck(playerInput,letterList,letterMask,lengthOfword) #overwrites the mask if the player's guess is correct and retruns true. otherwise, returns false
        
            if(qResult == True): # if the guess is correct 

                playerWin = letterCheck("*",letterMask,letterMask,lengthOfword) # uses the letterCheck function, this time to check if the player got the whole 
                                                                                # word correct, by checking if there are any masks("*") remaining in the list.
                                                                                # if the player got the whole word, the function would return "False"(or else "True")
                                                                                # which is stored in the playerWin variable  
                if(playerWin == False): # if the player got all the letter correct                       
                    playerWin == True   # changed to true to avoid confusion as this variable will be used again
                    t1.clear()          # clears the word mask at the top
                    textDraw(t1,1,lengthOfword,0,46,letterMask,20,"Courier","left","bold",-290,240,"blue",2) # redraws the word mask, this time as the full word, 
                                                                                                             # to show the player has won
                    break  # breaks from the loop as the player has won
                
                t1.clear()# clears the mask so it can be redrawn, this time with the correct guess via the draw function at the start of the loop

            elif(qResult == False):  # if the player's guess is wrong   
            
                playerAttempts -= 1  # decrements the attempts counter 
            
                textDraw(t3,2,0,0,0,playerInput,20,"Courier","left","italic",-240+(wrongGuessspace),-240,"blue",2) # draws the wrong guess at the bottom
                wrongGuessspace += 40 # spacing between the wrong guesses drawn at the bottom of the screen(e.g."E  A") which increases by 40 each time the player gets a guess wrong
                                      # this variable is then added to the x coordinate of the draw function above each time the loop is run. Increases by 40 
                                      # for a maximum of 7 times(the no of attempts) 
            

                if(playerAttempts == 7): # first wrong guess  
                    squareDraw(s1,0,150,125,-110,10,"white","blue",3,2) # draws the back of  the ambulance 

                if(playerAttempts == 6): # second wrong guess
                    squareDraw(s1,0,90,90,40,-25,"white","blue",3,2)    # draws the head of the ambulance

                if(playerAttempts == 5): # third wrong guess
                    circleDraw(s1,180,35,-60,-75,"blue","blue",3)       # draws the back wheel

                if(playerAttempts == 4): # fourth wrong guess
                    circleDraw(s1,0,35,65,-75,"blue","blue",3)          # draws the front wheel

                if(playerAttempts == 3): # fifth wrong guess
                    squareDraw(s1,180,50,20,50,-35,"white","blue",3,2)  # draws the front window

                if(playerAttempts == 2): # sixith wrong guess
                    squareDraw(s1,0,25,7,-47,18,"red","blue",3,2)       # draws the siren
                
                if(playerAttempts == 1): # seventh wrong guess
                    squareDraw(s1,0,50,25,-60,-20,"red","red",3,2)      # draws first part of the symbol 

                t2.clear() # clears the attempts counter at the bottom so it can be redrawn with the updated count at the start of the loop
            
                if(playerAttempts == 0): # final wrong guess and the failure condition
                    
                    squareDraw(s1,0,25,50,-47,-7,"red","red",3,2)      # draws the second part of the symbol, completing the ambulance

                    textDraw(t2,2,0,0,0,"You have "+str(playerAttempts)+" attempts remaining",15,"Courier","center","italic",-15,-340,"blue",2)# draws the counter 
                    # one last time to show that the player has 0 attempts remaining 

                    break # breaks from the loop as the player has lost

        if(qResult == True): # if the player has Won

            textDraw(t1,2,0,0,0,"YOU WIN",50,"Courier","center","bold",-30,100,"black",2) # success title drawn 
            
            if(playerAttempts == 8): # if the player had a perfect score, with no wrong guesses, therefore a perfect rating  
                textDraw(t1,2,0,0,0,"Perfect",40,"Courier","center","italic",-30,50,"black",2)

            if(playerAttempts < 8):  # default rating
                textDraw(t1,2,0,0,0,"Nice Work",40,"Courier","center","italic",-30,50,"black",2)

        if(qResult == False): # if the player has Lost

            textDraw(t1,2,0,0,0,"YOU LOSE",50,"Courier","center","bold",-30,100,"black",2) # failure title drawn 
            textDraw(t1,2,0,0,0,"Better Luck Next Time",20,"Courier","center","italic",-20,50,"black",2)

        space(100) 
        input("Press any key to restart the game ") # takes player input to restart the game
        turtle.resetscreen()                       # resets the whole game screen

                            

main() # runs the main game function


