# Importing all the programs to this program
import quickgame
import customgame
import pastplayer
import gamemenu
import Quitgame

# Using game menu to select available options
gamemenu.Menu()
select= int(input("Enter your option: "))

# Using IF condition to select available options
if (select==1):
    quickgame.Quickgame()
else:
    if(select==2):
        customgame.Customgame()
    else:
        if(select==3):
            pastplayer.result()
        else:
            if(select==4):
                Quitgame.exit()
            
