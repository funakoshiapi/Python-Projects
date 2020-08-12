#!/usr/bin/env python3
# -*- coding: utf-8 -*-


 ###########################################################

    #  Computer Project #1

    #

    #  Prompt user to input distance in rods.
    #  Display user's input

    # Convert the distance in rods to meter, foot, miles and furlongs.

    # Calculate the minutes to walk the distance designated by the user at
    # speed of 3.1 miles per hour
    
    # Display the conversions of the distance, and the minutes to walk to
    # the user 

    #    
    ###########################################################


num_rod_str = input( "Input rods: " ) # input in rods. Type of variable is string
num_rod_float = float( num_rod_str ) # convert input to float type

print("You input" ,num_rod_float, "rods." "\n")

#CONVERTION CALCULATION

num_meter = num_rod_float * 5.0292
num_foot = num_meter / (0.3048)
num_miles = num_meter / (1609.34) 
num_furlongs = num_rod_float/ (40)

# average speed of  3.1 miles per hour 

AVG_SPEED = 3.1

# time based on distance and speed. d = t*s

t_hours = num_miles / (AVG_SPEED ) 

# THE FOLOWING IS CONVERTING THE TIME FROM SEC TO MINUTES

t_min = t_hours * 60.0


print("Conversions")
print("Meters:",round(num_meter,3))
print("Feet:",round(num_foot,3))
print("Miles:",round(num_miles,3))
print("Furlongs:",round(num_furlongs,3))
print("Minutes to walk" ,num_rod_float, "rods:" ,round(t_min,3),)


      
      
   
      
      
      
 