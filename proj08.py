# Project 8

# Opens a data file, and allows the user to observe diabetes prevalence data.
# The data is diplayed on a table. And the user can also plot the data and display it

# =============================================================================
# Teacher Assistants help me complething some of the functios in this project
# =============================================================================


import pylab 

#from operator import itemgetter   # optional, if you use itemgetter when sorting

REGIONS = {'MENA':'Middle East and North Africa','EUR':'Europe',\
               'AFR':'Africa','NAC':'North America and Caribbean',\
               'SACA':'South and Central America',\
               'WP':'Western Pacific','SEA':'South East Asia'}

def open_file():    
    '''
        Asks for input file name, and opens the existing file
        value: processes type string
        Returns: returns a file object
    '''
    
    file_str = input("Please enter a file name: ")
    
    while True:
        try:
            file_obj = open(file_str, encoding ="windows-1252")
            
            return file_obj
            break
        
        except IOError:
            
            print("File not found.",end="") 
           
            file_str = input(" Please enter a valid file name: ")
    
def create_dictionary(file_obj):
    '''
        Will format the data and creat a dictionary
        value: processes a file object
        Returns: Dictionary
    '''
    
    D={}
    
    file_obj.readline()
    
    for line in file_obj:
         
         line_list = line.strip().split(',')
         
         country = line_list[1]
         region = line_list[2]
         age_group = line_list[3]
         gender = line_list[4]
         geographic_area = line_list[5]
         diabetes = int(float(line_list[6])*1000)
         population = int(float(line_list[7])*1000)
      
         tup = (gender, geographic_area, diabetes, population)
         
        # the following checks will guarantee that the dictionary
        # contains the correct elements of the list
        
         if region not in D:
             
            D[region] = {}
            
         if country not in D[region]:
             
            D[region][country]= {}
            
         if age_group not in D[region][country]:
             
            D[region][country][age_group]= [tup]
            
         else:
             
            D[region][country][age_group].append(tup)  
         
    return D
    
   
    
def get_country_total(data):
    
    '''
        Will format the data and create a dictionary
        containing total population, total people with diabites, 
        and it's respective countries.
        value: processes a dictionary
        Returns: Dictionary
    '''
    
    
   
    
    total_value_p= 0
    total_value_d =0
     
    countries_list = list(data.keys())
    
    my_dict = {}
    
    # The subsequent for loops
    # are very important because it allows us to
    # access the the keys of our dictionary
    
    for my_country in countries_list :
        
        age_group = data[my_country ]
        
        age_lst = list(age_group.keys())
        
        total_value_p= 0
        
        total_value_d= 0
        
        for age in age_lst:
            
            p = age_group[age]
            
            for values in p :
               
                # access the last valeu of the list tuple
                # wich referes to the population
                
               total_p = values[-1]
               
               total_p = int(total_p)
               
               total_value_p += total_p 
               
               # access the second last valeu of the list tuple
               # wich referes to the population with diabities
               
               diabites = values[-2]
               
               diabites = int(diabites)
               
               total_value_d += diabites
               
            
        my_dict[my_country] = (total_value_d, total_value_p )
    
    return my_dict    
        
    
def display_table (data, region):
    
     '''
        Will display a table of information
        value: processes a dictionary and a string.
        Returns: Does not return anything
     '''
   
     print("{:^61s}".format("Diabetes Prevalence in " + REGIONS[region] ))
     print("{:<25s}{:>20s}{:>16s}".format('Country Name ','Diabetes Prevalence','Population'))
    
     countries_list = list(data.keys())
     
     countries_list.sort()
     
     population=0
     
     p_diabities=0
     
     new_dict = {}
     
     for my_country in countries_list:
         
         new_dict[my_country] = data[my_country]
         
         value=new_dict[my_country]
         
         p_diabities += int(value[0])
                 
         population +=int(value[1])
         
         print("{:<25s}{:>20,d}{:>16,d}".format(my_country[:24], value[0], value[1]))
         
     print("{:<25s}{:>20,d}{:>16,d}".format('TOTAL', p_diabities, population))
    


def prepare_plot(data):
    
    '''
        Will format the data to be ploted
        value: processes a dictionary
        Returns: Dictionary
    '''
    # Teacher assistent help me to write this function
    
    countries_list = list(data.keys())
    
    my_dict = {}
    
    for my_country in countries_list:
        
        age_group = data[my_country]
       
        age_list = list(age_group.keys())
       
        for age in age_list:
            
            p = age_group[age]
            
            for values in p :
                
                if age not in my_dict:
                    
                    my_dict[age]={}
                    
                if values[0].upper() not in  my_dict[age]:
                    
                    my_dict[age][values[0].upper()]= 0
                    
                my_dict[age][values[0].upper()] += values[2]  
                
    return my_dict         
                    

def plot_data(plot_type,data,title):
    '''
        This function plots the data. 
            1) Bar plot: Plots the diabetes prevalence of various age groups in
                         a specific region.
            2) Pie chart: Plots the diabetes prevalence by gender. 
    
        Parameters:
            plot_type (string): Indicates what plotting function is used.
            data (dict): Contains the dibetes prevalence of all the contries 
                         within a specific region.
            title (string): Plot title
            
        Returns: 
            None
            
    '''
    
    plot_type = plot_type.upper()
    
    categories = data.keys() # Have the list of age groups
    gender = ['FEMALE','MALE'] # List of the genders used in this dataset
    
    if plot_type == 'BAR':
        
        # List of population with diabetes per age group and gender
        female = [data[x][gender[0]] for x in categories]
        male = [data[x][gender[1]] for x in categories] 
        
        # Make the bar plots
        width = 0.35
        p1 = pylab.bar([x for x in range(len(categories))], female, width = width)
        p2 = pylab.bar([x + width for x in range(len(categories))], male, width = width)
        pylab.legend((p1[0],p2[0]),gender)
    
        pylab.title(title)
        pylab.xlabel('Age Group')
        pylab.ylabel('Population with Diabetes')
        
        # Place the tick between both bar plots
        pylab.xticks([x + width/2 for x in range(len(categories))], categories, rotation='vertical')
        pylab.show()
        # optionally save the plot to a file; file extension determines file type
        #pylab.savefig("plot_bar.png")
        
        
    elif plot_type == 'PIE':
        
        # total population with diabetes per gender
        male = sum([data[x][gender[1]] for x in categories])
        female = sum([data[x][gender[0]] for x in categories])
        
        pylab.title(title)
        pylab.pie([female,male],labels=gender,autopct='%1.1f%%')
        pylab.show()
        # optionally save the plot to a file; file extension determines file type
        #pylab.savefig("plot_pie.png")

def main():
    
    '''
    This function is where the other functions are called, and where
    the object file is closed.
    Value: has no argument
    Returns: Does not return anything
    '''
    
    
    "\nDiabetes Prevalence Data in 2017"
    MENU = \
    '''
                Region Codes
    MENA: Middle East and North Africa
    EUR: Europe
    AFR: Africa
    NAC: North America and Caribbean
    SACA: South and Central America
    WP: Western Pacific
    SEA: South East Asia
    '''
    
    "Enter region code ('quit' to terminate): "
    "Do you want to visualize diabetes prevalence by age group and gender (yes/no)?: "
    "Error with the region key! Try another region"
    "Incorrect Input! Try Again!"
    
     # Teacher assistent help me to write this function
     
     
    op = open_file()
    
    data_creat = create_dictionary(op)
    
    r = list(REGIONS.keys())
    
    print(MENU)
    region = input("Enter region code ('quit' to terminate): " ).upper()
    
    while region != 'QUIT': 
        
       
        
        if region in data_creat:
    
             data = get_country_total(data_creat[region])
             
             display_table(data,region)
             
             q = input("Do you want to visualize diabetes prevalence by age group and gender (yes/no)?: ").lower()
             
             while q not in ['yes', 'no']:
                 
                 print("Incorrect Input! Try Again!")
                 
                 q = input("Do you want to visualize diabetes prevalence by age group and gender (yes/no)?: ").lower()
                 
             if q == 'yes':
                
                prep_p = prepare_plot(data_creat.get(region))
                
                title = ("Diabetes Prevalence in " + REGIONS[region] + ' by Age Group and Gender')
                
                plot_data("PIE",prep_p,title)
                plot_data("BAR",prep_p,title)
                 
                
             
        else:
            
           print("Error with the region key! Try another region" )
        
        print(MENU)
        region = input("Enter region code ('quit' to terminate): " ).upper()
        
        
        
        
    
    op.close()
###### Main Code ######
if __name__ == "__main__":
    main()
