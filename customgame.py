# Importing random in order to mix the numbers given to the user
import Sub.mode

# Defining the Customgame to import to main program
def Customgame():
    print("                      CUSTOMGAME                         ")


    # Creating variables
    mode=int(input("\n1]Easy\n2]Medium\n3]Hard\nEnter the mode: "))
    

    # Using IF conditon to select the levels
    if(mode==1):
        Sub.mode.easy()
    else:
        if(mode==2):
            Sub.mode.medium()
        else:
            if(mode==3):
                Sub.mode.hard()
        
    
