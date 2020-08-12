# Project 6

# Opens a data file, and allows the user to observe census information:
# table of data, and a data ploted graph


'''
    The programs starts by asking for a file
    name. If the file exists it is opened. 
    If not it prompts the user to try a different
    file name. Then it makes use of iterations, tuples, lists and functions
    to manipulate and display the data.
    
'''


import pylab   # for plotting
from operator import itemgetter  # useful for sorting

def open_file():
    '''
        Asks for input file name, and opens the existing file
        value: processes type string
        Returns: returns a file object
    '''
    
    file_str = input("Enter a file name: ")
    
    
    while True:
        try:
            file_obj = open(file_str, 'r')
            
            return file_obj
            break
        
        except IOError:
            
            print("Error. Please try again.") 
           
            file_str = input("Enter a file name: ")
            
            
def find_index(header_lst,s):
    '''
    This function finds the index refereing to its repective
    column in the data file.
    Value: The arguments processed are a list and a string
    Returns: a index value  
    
    '''
    
    for index, el in enumerate(header_lst):
    
        if el == s:
            value=index
            return value
            break       
    else:
        print( None)
        

def read_2016_file(fp):
    '''
     This function goes through the file object and appends
     and sorts census informations refering to 2016 data file.
    Value: The arguments processed is a file pointer
    Returns: a list
    '''
    
    # This stpet is crutial for theis program, because 
    # here starts the initial manipulations of the file object data
    
    
    header = fp.readline()
    header_lst = header.split(',')
    my_list=[]
    
    # The find index fuctions is used to find the desired column 
    # in the execl file
    
    for line in fp:
        
        line_lst = line.strip().split(',')
        
        state = line_lst[2].strip()
        
        val_1=state
        
        native_index= find_index(header_lst,'EST_VC197')
     
        val_2 = line_lst[native_index]
      
        
        natu_cit = find_index(header_lst,'EST_VC201')
        
        val_3=line_lst[natu_cit]
        
        non_cit = find_index(header_lst,'EST_VC211')
    
        val_4=line_lst[non_cit]
        
        # This statment allows to 
        # only calculate the desire data in the object file
        # This is non numerical strings
        # will not be added to the  calculation
        
        if val_2.isdigit()== True and val_3.isdigit()== True and val_4.isdigit()== True:
           
            val_2 = int(val_2)
            val_3 = int(val_3)
            val_4 = int(val_4)
            
            sum_cit = val_2 + val_3 + val_4
                
            ratio_natu = (val_3/sum_cit)
        
            ratio_non = (val_4/sum_cit) 
            
            t = val_1,val_2,val_3,ratio_natu,val_4,ratio_non
            
            my_list.append(t)
            
            
        
    my_list = sorted(my_list, key=itemgetter(5))     
    return my_list    
   
    
    
    
def read_2000_file(fp2):
    '''
     This function goes through the file object and creates a tuple
     containing census informations refering to 2000 data file.
    Value: The arguments processed is a file pointer
    Returns: a tuple
    '''
    
    header = fp2.readline()
    header_lst = header.split(',')

    
    for line in fp2:
        
        line_lst = line.strip().split(',')
        
        total_p = find_index(header_lst,'HC01_VC02')
     
        total_p = line_lst [total_p]
      
        
        nati_re = find_index(header_lst,'HC01_VC03')
        
        nati_re =line_lst[nati_re]
        
        natu_cit = find_index(header_lst,'HC01_VC05')
        
        natu_cit=line_lst[natu_cit]
        
        non_cit = find_index(header_lst,'HC01_VC06')
        
        non_cit = line_lst[non_cit]
        
        
        if total_p.isdigit()== True and nati_re.isdigit()== True and natu_cit.isdigit()== True \
        and non_cit.isdigit()==True:
            
            t = int(total_p),int(nati_re),int(natu_cit),int(non_cit)
            
            
            
    return t
            

def calc_totals(data_sorted):
    '''
    This function calculates the total count of 2016: native-born residents,
    naturalized citizens,non-citizens and a total of of the three (residents)
    Value: The arguments processed is list
    Returns: a tuple
    '''
    
    value_1=0
    value_2=0
    value_3=0
    
    
    a=0
    
    my_tuple=()
    
    # this iteration is used to navigate through
    # the sorted data(list)
    # as the value of 'a' is incremented
    # we navigate to a diferent element of our list
    # wich will allow to collect the desired cencus information
    
    while a <= len(data_sorted)-1:
        
      
        my_list = data_sorted[a]
        
        n_resi= int(my_list[1])
        
        naturalized=int(my_list[2])
        
        non_citizens=int(my_list[4])
    
        value_1 += n_resi
        
        value_2 += naturalized
        
        value_3 +=non_citizens
        
        sum_total= value_1 + value_2  + value_3
        
        my_tuple= value_1, value_2, value_3, sum_total
        
        a += 1
        
    return my_tuple

def make_lists_for_plot(native_2000,naturalized_2000,non_citizen_2000,native_2016,naturalized_2016,non_citizen_2016):
    '''
    This function organizes a selected previous extracted data in three different lists.
    Value: The arguments are integers
    Returns: a tuple containing three lists
    '''
    list1 = [native_2000,native_2016]
    list2 = [naturalized_2000, naturalized_2016]
    list3 = [non_citizen_2000, non_citizen_2016]
    
    t = list1, list2,list3
    return t
    
def plot_data(native_list, naturalized_list, non_citizen_list):
    '''
    This function uses a selected previous extracted data to plot a graph
    Value: the arguments are lists
    Returns: Does not return anything, but will plot a graph
    '''
    question= input('Do you want to plot? ')
    if question.upper() == 'YES':
        X = pylab.arange(2)   # create 2 containers to hold the data for graphing
        # assign each list's values to the 3 items to be graphed, include a color and a label
        pylab.bar(X, native_list, color = 'b', width = 0.25, label="native")
        pylab.bar(X + 0.25, naturalized_list, color = 'g', width = 0.25, label="naturalized")
        pylab.bar(X + 0.50, non_citizen_list, color = 'r', width = 0.25,label="non-citizen")
    
        pylab.title("US Population")
        # label the y axis
        pylab.ylabel('Population (hundred millions)')
        # label each bar of the x axis
        pylab.xticks(X + 0.25 / 2, ("2000","2016"))
        # create a legend
        pylab.legend(loc='best')
        # draw the plot
        pylab.show()
        # optionally save the plot to a file; file extension determines file type
        #pylab.savefig("plot.png")
    else:
        pass
def main():    
    '''
    This function is where the other functions are called, and where
    the object file is closed.
    Value: has no argument
    Returns: Does not return anything
    '''
    
    data1 = open_file()
    data_2016 =read_2016_file(data1)
    
    
    
    data2 = open_file()
    data_2000 = read_2000_file(data2)
    space= ' '
    print("{:<31s}{:>5s}{:<32s}".format(space,'2016 Population: Native, Naturalized, Non-Citizen',space,))
    
    print("{:<20s}{:>15s}{:>17s}{:>22s}{:>16s}{:>22s}".format("State","Native","Naturalized","Percent Naturalized", "Non-Citizen","Percent Non-Citizen"))
    
    a=0
    
    total1 = calc_totals(data_2016)
    

    # Calculation of the precentages displayed in the table of data
    # This iteration is used to print different elelemnts in our list
    #refering to the 2016 data file
    
    while a<= len(data_2016)-1:
        
        my_list = data_2016[a]
        
        percentage2 = my_list[5]*100
        percentage2 = "%.1f" %  percentage2
        
        percentage1 = my_list[3]*100
        percentage1 = "%.1f" %  percentage1
        
        print("{:<20s}{:>15,d}{:>17,d}{:>22s}%{:>16,d}{:>22s}%" \
        .format(my_list[0],my_list[1],my_list[2], percentage1,my_list[4], percentage2))
        
        a +=1
        
    # 2016 total percentage    
    p_naturalized=(total1[1]/total1[3])*100
    p_naturalized = "%.1f" %  p_naturalized
    p_non_cit=(total1[2]/total1[3])*100
    p_non_cit = "%.1f" %  p_non_cit
    
    #2000 total percentage
    naturalized_p= (data_2000[2]/data_2000[0])*100
    naturalized_p = "%.1f" %  naturalized_p
    
    non_cit_p= (data_2000[3]/data_2000[0])*100
    non_cit_p = "%.1f" %  non_cit_p
    
    print('-'*112)
    
    print("{:<20s}{:>15,d}{:>17,d}{:>22s}%{:>16,d}{:>22s}%"\
        .format('Total 2016',total1[0],total1[1],p_naturalized,total1[2], p_non_cit))
    
    # Print refering to the 2000 data file    
    print("{:<20s}{:>15,d}{:>17,d}{:>22s}%{:>16,d}{:>22s}%"\
        .format('Total 2000',data_2000[1],data_2000[2],naturalized_p,data_2000[3],non_cit_p))
    
    
    ploting_lists = make_lists_for_plot(data_2000[1],data_2000[2],data_2000[3],total1[0],total1[1],total1[2])
    
    list1=ploting_lists[0]
    list2=ploting_lists[1]
    list3=ploting_lists[2]
    
    my_plot = plot_data(list1,list2,list3)
    
    data1.close()
    data2.close()
    
if __name__ == "__main__":
    main()