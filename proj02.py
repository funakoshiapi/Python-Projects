# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""





#Display the rules of the game
print("\nWelcome to the game of Nim! I'm probably going to win...")
print('''Nim is a simple two-player game based on removing stones.
         The game begins with two piles of stones, numbered 1 and 2. 
         Players alternate turns. Each turn, a player chooses to remove one, 
         two, or three stones from some single pile. The player who removes the
         last stone wins the game.''')


    ###########################################################
    #
    #  Computer Project #2
    #
    #  Two players take turns removing objects from distinct piles
    #  The last person reomving the object from the distinct pile wins.
    # This code will display the ammount of objects in the piles
    # and the  amount of removed objects from the pile.
    # It checks if the player follows the rule of the game
    # which include that the pile must be 1 or 2 and non-empty.
    #
    # At the end it displays the winner of the game and the score of the game 
    #
    ###########################################################
    


play_str=input("Would you like to play? (0=no, 1=yes) ")


# controls if the game will initiate or not
# Initiate piles with 5 stones

while int(play_str) != 0:
    
    
    pile_1 = 5
    pile_2 = 5
    
   

    #  Used to set what initial printing to give to the user
    # and to control when the game ends
    
    while(pile_1 > 0 or pile_2 > 0): 
        
        if(pile_1 == 5 or pile_2 ==5):
            
            print ("Start --> Pile 1:",pile_1,"   Pile 2:" ,pile_2)
            choose = input("Choose a pile (1 or 2): ")
            choose_int = int(choose)
            
        else:
            print ("Pile 1:",pile_1,"   Pile 2:",pile_2)
            choose = input("Choose a pile (1 or 2): ")
            choose_int = int(choose)
            
       
        
        # Game rules
        
        # Regulate the game allowing this conditions to be fullfild: 
        # pile must be 1 or 2 and non-empty
  
        while (choose_int != 1 and choose_int != 2):
            
            print("Pile must be 1 or 2 and non-empty. Please try again.")
            choose = input("Choose a pile (1 or 2): ")
            choose_int = int(choose)
            
        while ((choose_int ==1) and (pile_1 == 0)):
            
            print("Pile must be 1 or 2 and non-empty. Please try again.")
            choose = input("Choose a pile (1 or 2): ")
            choose_int = int(choose)
            
        while ((choose_int ==2) and (pile_2 == 0)):
            
            print("Pile must be 1 or 2 and non-empty. Please try again.")
            choose = input("Choose a pile (1 or 2): ")
            choose_int = int(choose)
            

        #GAME CONTROL
        # PILE 1 HUMAN COMMANDS 
       
     
        if (choose_int == 1): 
        
            taking_1 = input ("Choose stones to remove from pile: ")
            taking_int_1 = int(taking_1)
            
    
            while (taking_int_1 > 3):
                print("Invalid number of stones. Please try again.")
                taking_1 = input ("Choose stones to remove from pile: ")
                taking_int_1 = int(taking_1)
        
            else:
                
                pile_1 = pile_1 - taking_int_1
                
                
                print("Player -> ",end='')
                print("Remove",taking_int_1,"stones from pile 1")

                print ("Pile 1:",pile_1,"   Pile 2:",pile_2)
                
                # This block of code checks who removed the last stone
                #from the pile. Attributes a value of 1 to the variable 
                # x ,which will be used to define who won the game;
                # This check repeats along the code.
                # x = 1 will be attributed when human player is the person
                # removing the last stone.
                
                
                if(pile_2 == 0):
                    if(pile_1 == 0):
                        x= 1
                        
                        break
                  

            # PILE 1 COMPUTER COMMANDS
                
                taking_computer= 1
                
           # Defines where the computer remove the stones from
           # and regulates the amount of stones taken
           
            if(pile_2 == 0):
                pile_1 = pile_1 - taking_computer
                print("Computer -> ",end='')
                print("Remove",taking_computer,"stones from pile 1")
                
                
                # x = 0 will be attributed when the computer is the last
                # removing the last stone
                
                if(pile_2 == 0):
                    if(pile_1 == 0):
                        
                        x= 0
                        print ("Pile 1:",pile_1,"   Pile 2:",pile_2)
                        break
              
                
            else:
                pile_2 = pile_2 - taking_computer
                print("Computer -> ",end='')
                print("Remove",taking_computer,"stones from pile 2")
                
                if(pile_2 == 0):
                    if(pile_1 == 0):
                        x= 0
                        print ("Pile 1:",pile_1,"   Pile 2:",pile_2)
                        break
               
 
        # PILE 2 HUMAN COMMANDS 
 
        if (choose_int == 2):
            taking_2 = input ("Choose stones to remove from pile: ")
            taking_int_2 = int(taking_2)
            
            
        
            while (taking_int_2 > 3):
                print("Invalid number of stones. Please try again.")
                taking_2 = input ("Choose stones to remove from pile: ")
                taking_int_2 = int(taking_2)
        
            else:
                
                pile_2 = pile_2 - taking_int_2
                
                print("Player -> ",end='')
                print("Remove",taking_int_2,"stones from pile 2")
                
                print ("Pile 1:",pile_1,"   Pile 2:",pile_2)
                
                    
                if(pile_1 == 0):
                    if(pile_2 == 0):
                        x= 1
                        
                        break
                  
         
            # PILE 2 COMPUTER COMANDS 
              
                taking_computer=1
            
            if(pile_1 == 0): 
                pile_2 = pile_2 - taking_computer
                print("Computer -> ",end='')
                print("Remove",taking_computer,"stones from pile 2")
                
                if(pile_2 == 0):
                    if(pile_1 == 0):
                        x= 0
                        print ("Pile 1:",pile_1,"   Pile 2:",pile_2)
                        break
               
            else:
                pile_1 = pile_1 - taking_computer
                print("Computer -> ",end='')
                print("Remove",taking_computer,"stones from pile 1")
                
                if(pile_2 == 0):
                    if(pile_1 == 0):
                        x= 0
                        print ("Pile 1:",pile_1,"   Pile 2:",pile_2)
                        break
                    
    # The folloging check what is the value of x
    # at the end of the loop to dictate who won the game
    # and displays the score at the end of the game
                
    points_hmn=0
    points_cp =0
                
    if (x == 1):
        print("\nPlayer wins!")
        points_hmn += 1 
        print("Score -> human:",points_hmn,"; computer:",points_cp,)
        
    if (x == 0):
        print("\nComputer wins!")
        
        points_cp += 1 
        print("Score -> human:",points_hmn,"; computer:",points_cp,)
         
# Will prompt to start a new game
    
    
    play_str = input("\nWould you like to play again? (0=no, 1=yes) ")

else:
   print("\nThanks for playing! See you again soon!")


