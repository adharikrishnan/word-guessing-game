def space(noLines):                                   # creates space which will be used to "clear" the screen for player 2
    for i in range(noLines):                          # the number of lines can be specified 
        print("")               

def letterAssignment(wordLength,giveWord,storeList): # stores the word enterd as a list, 
    for i in range(wordLength):                      # with each letter being a seprate element   
        giveWord[i]= storeList[i]                    # used for easier and more effective manipulation of the word entered    

def letterCheck(eLetter,anSwer,wordList,listLength):  # function used to check if the player's leeter choice was correct or wrong                                                                
    lBool = False                   # initializes the value to False
    
    for i in range(listLength):     # uses loop to check if the letter the player entered is a letter in the word  
        
        if eLetter == anSwer[i]:    # if the letter is a letter in the list (letterList), the list is overwritten with the correct letter
            wordList[i] = anSwer[i] # in the corresponding list index (in our case, the mask will be overwritten) 
                                    # e.g letterMask = ["*","o","*","*"], if the word is "monk" and the player's guess was "o" )            
            lBool = True            # sets the boolean variable to true, denoting that the player was correct in his/her guess

    return lBool                    # returns the result of the function as the boolean variable, which is either true or false for simplicity     


def squareDraw(cu,sAngle,sWidth,sHeight,xCor,yCor,fillC,outlineC,pSpeed,pSize):

    cu.ht()                                       # function used to create squares and rectangles                                               
    cu.speed(0)                                   # the height, width, position, colour of the shapes can be set,
    cu.left(sAngle)                               # along with the pen speed, colour(becomes the outline for the shape) and speed                           
    cu.penup()                                              
    cu.goto(xCor,yCor)
    cu.pendown()                                  # sAngle is used to set the start direction for the turtle                               
    cu.pencolor(outlineC)
    cu.pensize(pSize)
    cu.speed(pSpeed)
    cu.fillcolor(fillC)
    cu.begin_fill()                                                     
    cu.forward(sWidth)                           # a simple for loop can be used to create squares, however
    cu.right(90)                                 # since rectangles are needed as well, it will not be used                        
    cu.forward(sHeight)                          # this saves the need to write a seperate function to draw rectangles               
    cu.right(90)
    cu.forward(sWidth)
    cu.right(90)
    cu.forward(sHeight)
    cu.right(90)
    cu.end_fill()
    
def circleDraw(cu,cAngle,cRadius,xCor,yCor,fillC,outlineC,pSpeed):

    cu.ht()                                      # function to draw a circle           
    cu.left(cAngle)                              # similar to the above function, each feature can be set                                 
    cu.speed(0)                                  # the radius of the cirlce in this case, instead of the height and width                       
    cu.penup()
    cu.goto(xCor,yCor)
    cu.pendown()
    cu.pencolor(outlineC)
    cu.speed(pSpeed)
    cu.fillcolor(fillC)
    cu.begin_fill()
    cu.circle(cRadius)
    cu.end_fill()

def textDraw(cu,tFunction,wordLength,tAngle,lSpace,teXt,tSize,tFont,tAlign,tType,xCor,yCor,tColor,tSpeed): # the text function, which acts as two fucntions in one   
    cu.ht()
    if(int(tFunction)== 1):                                                                                                       
        for i in range(int(wordLength)):            # if tFunction is set to 1, this function is performed
            cu.speed(0)                             # draws each letter in a list with space in between, which will be used later                         
            cu.penup()
            cu.goto(int(xCor)+i*int(lSpace),yCor)   # the amount of spcae in between the letter can be specified with lSpace, and be made with help
            cu.pendown()                            # of the loop counter                     
            cu.pencolor(tColor)
            cu.write(str(teXt[i]),align = tAlign,font=(tFont,tSize,tType)) # the size, font, font type, alignment and colour of the font can be set
            
    if(int(tFunction)== 2):                         # if tFunction is set to 2, this function is performed                                    
        cu.ht()                                     # simply draws given text                                     
        cu.left(tAngle)                             # just as above, the atrributes of the text can be set                
        cu.speed(0)
        cu.penup()
        cu.goto(xCor,yCor)
        cu.pendown()
        cu.pencolor(tColor)
        cu.write(teXt,align = tAlign,font=(tFont,tSize,tType))  