
# Project 5

# Opens a data file, and allows the user to observe the maximum population groth 
# on a range of years for each respective continent, displays the groth 
# percentage for each continent, and displays from among all the continents the 
# one  with the major population groth.

'''
    The programs starts by asking for a file
    name and if the file exists it is opened 
    if not it prompts the user to try a different
    file name. The a crutial action the
    program does is to break the data file 
    and save each line of the data file in a
    variable as a string. Then it calls the function
    calc_delta with the respestive string and
    column number argument , to calculate the the rate of
    change, which is stored in a variable.
    As we find the rate of change it loops its 
    values to calculate what is the bigest
    rate of change corresponding to each respective 
    country and the years that
    represent the major rate of change.
    Other loop is executed to identify the bigest
    population groth among the contines, 
    and the respective year. Lastly this values 
    are respecively formated for display  to the user. 
    
'''


def open_file():
    '''
        Asks for input file name, and opens the existing file
        value: processes type string
        Returns: returns a file object
    '''
    
    
   
    file_str = input("Enter a file name: \n")
   

    while True:
        
        
        try:
            
            file_obj = open(file_str, 'r')
            
            return file_obj
         
                           
            break
        
        except IOError:
            
            print("Error. Please try again.") 
           
            file_str = input("Enter a file name: ")
    
    
    
def print_headers():
    '''
    This function prints a header
    Value: Processes type string
    Returns: Header string 
    '''
    
    header =("     Maximum Population Change by Continent\n")
    
    return header
    

def calc_delta(line, col):
    '''
    This function calculates the rate of change in population
    Value: The arguments processed are string and int
    Returns: the rate of change  
    '''
    
    country = line[:15]
    
    number = line[15:]
    
    start = 0

    for i in range(6):
        
        if i == col-1:
            
            first = number[start:start+12]
            
            a = int(first[:6])
            b = int(first[6:])
                
            change = (b-a)/ a
            
            return change
        
        start +=6


def format_display_line(continent,year,delta):
    '''
    This function will format its arguments to be displayed
    Value: The arguments processed are string, int and float
    Returns: the formated argument 
    
    '''
    
    delta = delta * 100
    delta =  "%.f" % delta 
    
    return '{:<26s}{:>4d}-{:<9d}{:>4s}%'.format(continent,year-50,year,delta)



def extract_year(line, col):
    '''
    This function extract the year from a string
    Value: The arguments processed are string, and int
    Returns: a year in  type int
    '''
    
    number = line[15:]
    
    start = 0

    for i in range(6):
        
        if i == col-1:
            
            first = number[start:start+12]
    
            b = int(first[6:])
            
            
            return b
                
        
        start +=6 
          
    
def main():
    
    '''
    This function is where the other functions are called, and where
    the object file is closed.
    Value: The arguments processed are string and int
    Returns: Does not return anything
    
    '''
    
    line_continent=''
    line_afric=''
    line_asia= ''
    line_aust = ''
    line_eur = ''
    line_north = ''
    line_south = ''

    
    data = open_file()
    
    count = 0
    col = 0
    
    # The implementation of this for loop allowed to store each line of the data
    # file in diffent variables so that later data can be extracted from them
    # count is used as a switch to access each if statement to store the data
    
    for line in data:
      
        
        count += 1
        
        
        if count == 2:
            
           line_continent = line
           name = line[:15]
           
           
        if count == 3:
            
            line_afric = line
            name_afric = line[:15].strip(' ')
             
            
        if count == 4:
            
            line_asia = line
            name_asia = line[:15].strip(' ')
            
        if count == 5:
            
            line_aust = line
            name_aust = line[:15].strip(' ')
            
        if count == 6:
            
            line_eur = line
            name_eur = line[:15].strip(' ')
            
        if count == 7:
            
            line_north = line
            name_north = line[:15].strip(' ')
            
        if count == 8:
            
            line_south = line
            name_south = line[:15].strip(' ')
            
        col +=1  
     
    
    # The second most important step for obtaining the data to be formated 
    # hapens here, as we finally obtain the respective reate of changes
    # for each country and the respective year 
    
    max_change_a = 0
    for i in range(6):
        
        
       change_afric = calc_delta(line_afric,i+1)
       
       # This comperison keeps ocurring in this for loop so
       # that we can store the max rate of change and the year we find the max.
       
       # At the end of this loop we will have saved in variables the max rate,
       # and its respective year for all continents in our file
       
       if change_afric > max_change_a:
            
           max_change_a = change_afric
            
           year_a = extract_year(line_continent,i+1)
           
       
    max_change_asia=0   
    
    for i in range(6):
        
        change_asia = calc_delta(line_asia,i+1)
        
        if change_asia > max_change_asia:
            
               max_change_asia = change_asia
            
               year_asia = extract_year(line_continent, i+1)
     
    max_change_aust=0   
    
    for i in range(6):
        
        change_aust = calc_delta(line_aust,i+1)
        
        if change_aust > max_change_aust:
                   
                   max_change_aust = change_aust
                   
                   year_aust = extract_year(line_continent, i+1) 
    
    max_change_eur=0
    
    for i in range(6):
        
        change_eur = calc_delta(line_eur,i+1)
        
        if change_eur > max_change_eur:
                           
            max_change_eur = change_eur
                        
            year_eur = extract_year(line_continent, i+1)
       
    max_change_north = 0   
    
    for i in range(6):
         
         change_north = calc_delta(line_north,i+1)
         
         if change_north > max_change_north:
                           
             max_change_north = change_north
                           
             year_north = extract_year(line_continent, i+1)
               
    max_change_south = 0  
    
    for i in range(6):
        
        change_south = calc_delta(line_south,i+1)
        
        if change_south > max_change_south:
                               
            max_change_south = change_south
                                
            year_south = extract_year(line_continent, i+1)
              
       
    print(print_headers())
    print("{:26s}{:>9s}{:>10s}".format("Continent","Years","Delta"))       
    print(format_display_line(name_afric,year_a,max_change_a))
    print(format_display_line(name_asia,year_asia,max_change_asia))
    print(format_display_line(name_aust,year_aust,max_change_aust))
    print(format_display_line(name_eur,year_eur,max_change_eur))
    print(format_display_line(name_north,year_north,max_change_north))
    print(format_display_line(name_south,year_south, max_change_south))
    print("\nMaximum of all continents:")
    
    
    
    # The following loop was used to find the max population grouth, that gets
    # formated and stored in a variable called output
    
    max_grouth=0
    
    for i in range(5) :
        
        if  max_change_a > max_grouth:
         
            max_grouth = max_change_a
            
            output= format_display_line(name_afric,year_a,max_change_a)
        
        if max_change_asia > max_grouth:
            
                 
            max_grouth = max_change_asia
            output= format_display_line(name_asia,year_asia,max_change_asia)
                 
        if max_change_aust > max_grouth:
            
            max_grouth = max_change_aust
            output= format_display_line(name_aust,year_aust,max_change_aust)
                      
        if max_change_eur > max_grouth:
            
                 
            max_grouth = max_change_eur
            output= format_display_line(name_eur,year_eur,max_change_eur)
                           
        if max_change_north > max_grouth:
            
                               
            max_grouth = max_change_north
            output= format_display_line(name_north,year_north,max_change_north)
                               
        if max_change_south > max_grouth:
                                   
            max_grouth = max_change_south
            output = format_display_line(name_north,year_north,max_change_north)
            
    print(output)
    data.close()


if __name__ == "__main__":
    main()