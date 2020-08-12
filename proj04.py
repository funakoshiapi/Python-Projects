
##############################################################################
#                                                                            
#     Project 4                                                                       #
#       
#    A player rolls two dice. Each die has six faces. These faces contain  
#   1, 2, 3, 4, 5, and 6 spots.
#   After the dice have come to rest, the sum of the spots on 
#   the two upward faces is calculated. If the sum
#   is 7 or 11 on the first throw, the player wins 
#   (this is called a “Natural win”). If the sum is 2, 3, or 12 on
#   the first throw (called "craps"), the player loses
#    (i.e. the "house" wins). If the sum is 4, 5, 6, 8, 9, or 10
#   on the first throw, then the sum becomes the player's 
#   "point." To win, you must continue rolling the
#   dice until you "make your point." The player 
#   loses by rolling a 7 before making the point. 
#
##############################################################################









#from random import randint  # the real Python random
from cse231_random import randint  # the cse231 test random for Mimir testing
import sys 

def display_game_rules():
    print('''A player rolls two dice. Each die has six faces. 
          These faces contain 1, 2, 3, 4, 5, and 6 spots. 
          After the dice have come to rest, 
          the sum of the spots on the two upward faces is calculated. 
          If the sum is 7 or 11 on the first throw, the player wins. 
          If the sum is 2, 3, or 12 on the first throw (called "craps"), 
          the player loses (i.e. the "house" wins). 
          If the sum is 4, 5, 6, 8, 9, or 10 on the first throw, 
          then the sum becomes the player's "point." 
          To win, you must continue rolling the dice until you "make your point." 
          The player loses by rolling a 7 before making the point.''')

def get_bank_balance():
    
    '''Prompt the player for an initial bank balance (from which
        wagering will be added or subtracted). 
        The player-entered bank balance is returned as
        an int.'''
    
    user_balance_f = ''
    
    while user_balance_f == '':
       
       user_balance_f = input('Enter an initial bank balance (dollars): ')
       
       
           
    return int(user_balance_f)       
    


def add_to_bank_balance(balance): 
    
    '''Prompts the player for an amount to add to the
        balance. The balance is returned as an int.'''
    
    int_balance_c = 0
            
    user_balance_c= ''
    
    balance_control = 'yes'
    
    balance_question =''
    
    balance_total = 0
    
        
    while balance_question == '':
        
        balance_question = input("Do you want to add to your balance? ")
        
        
    while balance_control == 'yes':     
        
            if balance_question.lower() == 'no':
                
                balance_control = 'no'
                
                if balance < 1:
                    
                    print("You don't have sufficient balance to continue.")
                    print('Game is over.')
                    sys.exit()
                
                
                return balance
                
            
            if balance_question.lower()=='yes':
                
                while user_balance_c == '':
                
                    user_balance_c = input ('Enter how many dollars to add to your balance: ')
                    
                int_balance_c = int(user_balance_c)  
                    
                balance_total = int_balance_c + balance
                
                print('Balance:',balance_total)
                
                
                
                return balance_total
    

def get_wager_amount(): 
    
    ''' Prompts the player for a wager on a particular roll. The
        wager is returned as an int.'''
    
    wager =''
    
    while wager == '':
        
         wager = input ('Enter a wager (dollars): ')
         
         return int(wager)

def is_valid_wager_amount(wager, balance):
    '''Checks that the wager is less than
    or equal to the balance; returns  
    True if it is; False otherwise'''
    
    if wager <= balance:
        
        return True
    else:
        return False
    

def roll_die():
    
    '''Rolls one die. This function 
        should randomly 
        generate a value between 1 and 6
        inclusively and returns that value as an int'''
  
    random = randint(1,6)

    return random

    # atributr valu to die 1 and die 2 _> not implemented

def calculate_sum_dice(die1_value, die2_value):
    
    '''Sums the values of the two
        die and returns the sum as an int.'''
    
    # were is the value of the die coming from?
    
    sum_dice = die1_value + die2_value
    
    return sum_dice


def first_roll_result(sum_dice):
    
    '''The function determines the
        result on the first
        roll of the pair of dice.'''
    
    # check this
    # seems to not understand how i'm calling the calculate_sum function
    

    
    if sum_dice == 7 or sum_dice == 11:
        
        return 'win'
    
    if sum_dice == 2 or sum_dice==3 or sum_dice ==12 :
        return 'loss'
    
   
    if sum_dice == 4 or sum_dice == 5 or sum_dice == 6 or sum_dice == 8 or sum_dice ==9 or sum_dice == 10:
        
        point_value = sum_dice
        
        return 'point'
    
    
    
def subsequent_roll_result(sum_dice, point_value):
    
    '''The function determines
        the result on the subsequent rolls 
        of the pair of dice.'''
    
    if sum_dice == point_value:
      
      return 'point'
  
  
    if sum_dice == 7:
      
      return 'loss'
  
    if sum_dice != point_value and sum_dice != 7:
      
      return  'neither'


def continue_g():
    
    '''The function asks the player if the games continues'''
    
    continue_g = input('Do you want to continue? ')
    
    return continue_g
    



def main(): 
    
    ''' Takes no input. Returns nothing. 
        Call the functions from here.
        That, the game is
        played in this function'''
 
    
    display_game_rules()
    
    balance = get_bank_balance()
    
    add_balance=balance
    
    result_2=''
    
    # this variables are used as control to move through different
    # while loops in the source code
    
    continue_game = 'yes'
    
    first_roll = 'yes'
    
    control= True

   
    
    while continue_game == 'yes':
        
        while control==True:
            
            
            # this block of code is in charge of 
            # the first time the user plays the game
            # will rool the dices and check the results without
            # printing the result yet.
            # results display are handle on a different block of code
            # outside this while loop
            
            if first_roll == 'yes':
                
                wager = get_wager_amount()
                
                while wager > balance :
                    
                    print('Error: wager > balance. Try again.')
                    wager = get_wager_amount()
                    
            
                die1 = roll_die()
            
                die2 = roll_die()
        
                print('Die 1:',die1)
            
                print('Die 2:',die2)
            
                sum_dice = calculate_sum_dice(die1,die2)
            
            
                print('Dice sum:',sum_dice)
                
               # will check for the different resultes 
               # that regard the first roll of dices
               # output is printed outside the loop
               
               
                result = first_roll_result(sum_dice)
                
                if result == 'win':
                    
                    balance = add_balance + wager
                    
                    continue_game ='no'
                    break
                
                if result =='loss':
                    
                    balance = add_balance - wager
                    
                    continue_game ='no'
                    break
                
                if result =='point':
                    
                    point_value = sum_dice
                    break
        
                
            # will check for the different resultes 
            # that regard the subsequent roll of dices
            # had to use sys import to force program to stop
            # when player decides not to continue with the game
                
            while first_roll == 'no':
                
                    
                die1 = roll_die()
            
                die2 = roll_die()
            
                print('Die 1:',die1)
            
                print('Die 2:',die2)
            
                sum_dice = calculate_sum_dice(die1,die2)
                    
                print('Dice sum:',sum_dice)
                    
                result_2 = subsequent_roll_result(sum_dice, point_value)
                    
                    
                if result_2 == 'point':
            
                        balance = add_balance + wager
                        print('You matched your Point.')  
                        print('You WIN!')
                        print('Balance:',balance)
                        
                        first_roll ='yes'
                        
                        continue_game = continue_g() 
    
                        if continue_game == 'yes':
        
                            continue_game = 'yes'
                            
                            # this variable contains the initial balance
                            # and sums it the add balance
                            
                            add_balance = add_to_bank_balance(balance)
                            
                            
                        elif continue_game =='no':
                
                            print('Game is over.')
                            sys.exit()
            
                if result_2 == 'neither':
            
                        first_roll = 'no'
            
                        continue_game='yes'
            
                if result_2 == 'loss':
            
                        balance = add_balance - wager
                        print('You lose.')
                        print('Balance:',balance)
                        
                        first_roll ='yes'
                        
                        continue_game = continue_g() 
    
                        if continue_game == 'yes':
        
                            continue_game = 'yes'
                
                            add_balance = add_to_bank_balance(balance)
                            
                    
                        elif continue_game =='no':
                            
                            print('Game is over.')
                            sys.exit()
                          
                            
        # The  block of code below will handle the different 
        # out puts of rolling the dice
        # especially the first roll of dices, and the case 
        # in which we a point result
        
 

       
        # this if stament serves as  link to start the subsequent results  
        # that are checked in the while loop above.
        # It uses the control variables to go through the if statement
        # that regard the subsequent roll of dices
        
        if result == 'point':
            
            print('*** Point:',point_value)
            
            first_roll = 'no'
            
            continue_game='yes'
            
            
            
        if result == 'loss':
            
            print('Craps.')
            print('You lose.')
            print('Balance:',balance)
            
            continue_game = continue_g() 
    
            if continue_game == 'yes':
        
                continue_game = 'yes'
                
                add_balance = add_to_bank_balance(balance)
                
            elif continue_game =='no':
                
                print('Game is over.')
                continue_game=='no'
                sys.exit()
            
    
        if result == 'win':
        
            print('Natural winner.')
            print('You WIN!')
            print('Balance:',balance)
    
    
            continue_game = continue_g() 
    
            if continue_game == 'yes':
        
                continue_game = 'yes'
                
                add_balance = add_to_bank_balance(balance)
                
                
            elif continue_game =='no':
                
                print('Game is over.')
                continue_game=='no'
                sys.exit()

if __name__ == "__main__":
    main()
