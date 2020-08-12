# Project 7

# Opens a data file, and allows the user to observe TSA information data:
# table of data, and a data ploted graph.
# The data is mostly from 2002 to 2009


'''
    The programs starts by asking for a file
    name. If the file exists it is opened. 
    If not it prompts the user to try a different
    file name. Then it makes use of iterations, tuples, lists and functions
    to manipulate and display the data.
    
'''

import pylab   # needed for plotting

STATUS = ['Approved','Denied','Settled'] 


def open_file():    
    '''
        Asks for input file name, and opens the existing file
        value: processes type string
        Returns: returns a file object
    '''
    
    file_str = input("Please enter a file name: ")
    
    while True:
        try:
            file_obj = open(file_str, 'r')
            
            return file_obj
            break
        
        except IOError:
            
            print("File not found.",end="") 
           
            file_str = input(" Please enter a valid file name: ")
            
            
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



def read_file(fp):
    '''
    Will read a file object
    Value: The arguments processed is a file object
    Returns: a list of tuples  
    
    '''
    
    header = fp.readline()
    header_lst = header.split(',')
   
    # The find index fuctions is used to find the desired column 
    # in the execl file
    
    date_list=[]
    airport_list=[]
    amount_list=[]
    status_list=[]
    close_amount_list=[]
    
    
    
    # looking for data in each column
    for line in fp:
            
            line_lst = line.strip().split(',')
            
            years= find_index(header_lst,'Date Received')
            
            date = line_lst[years]
    
                
            airport= find_index(header_lst,'Airport Name')
                
            airport_name = line_lst[airport]
            
            
            amount= find_index(header_lst,'Claim Amount')
                
            claim_amount = line_lst[amount]
                
           
            
            s= find_index(header_lst,'Status')
                
            status = line_lst[s]
                
            
            
            c = find_index(header_lst,'Close Amount')
                
            c_amount = line_lst[c]
            
        
            # ignores empty strings, and only then appendes to its lists
            if date == '' or airport_name == '' or claim_amount=='' or status == '' or c_amount == '':
                continue
             
            date_list.append(date)
            airport_list.append(airport_name)
            amount_list.append(claim_amount)
            status_list.append(status)
            close_amount_list.append(c_amount)
            
    
    years=date_list
    airport=  airport_list
    amount = amount_list
    status = status_list
    c_amount = close_amount_list
    
    i= 0
    
    yr = []
    airport_f = []
    amount_f =[]
    status_f = []
    c_amount_f =[]
    
    # checking if the data is from the desired years
    while i < len(years):
        
       if '02' in years[i][-2:]: 
           yr.append(years[i])
           airport_f.append(airport[i])
           amount_f.append(amount[i])
           status_f.append(status[i])
           c_amount_f.append(c_amount[i])
             
       if '03' in years[i][-2:]: 
           yr.append(years[i])
           airport_f.append(airport[i])
           amount_f.append(amount[i])
           status_f.append(status[i])
           c_amount_f.append(c_amount[i])
           
       if '04' in years[i][-2:]: 
           yr.append(years[i])
           airport_f.append(airport[i])
           amount_f.append(amount[i])
           status_f.append(status[i])
           c_amount_f.append(c_amount[i])   
           
           
           
       if '05' in years[i][-2:]: 
           yr.append(years[i])
           airport_f.append(airport[i])
           amount_f.append(amount[i])
           status_f.append(status[i])
           c_amount_f.append(c_amount[i])    
           
       if '06' in years[i][-2:]: 
           yr.append(years[i])
           airport_f.append(airport[i])
           amount_f.append(amount[i])
           status_f.append(status[i])
           c_amount_f.append(c_amount[i])   
           
           
       if '07' in years[i][-2:]: 
           yr.append(years[i])
           airport_f.append(airport[i])
           amount_f.append(amount[i])
           status_f.append(status[i])
           c_amount_f.append(c_amount[i])  
             
       if '08' in years[i][-2:]: 
           yr.append(years[i])
           airport_f.append(airport[i])
           amount_f.append(amount[i])
           status_f.append(status[i])
           c_amount_f.append(c_amount[i])      
           
       if '09' in years[i][-2:]: 
           yr.append(years[i])
           airport_f.append(airport[i])
           amount_f.append(amount[i])
           status_f.append(status[i])
           c_amount_f.append(c_amount[i])  
           
           
       i +=1 
    
 
    # formating and converting the quantities to float
    c_amount_float=[]
    
    for line in c_amount_f:
        
        line= line.strip('$')
        
        line = line.strip().replace(';','')
        
        c_amount_float.append(float(line))
        
    amount_float=[]
    
    for line in amount_f:
        
        line= line.strip('$')
        
        line = line.strip().replace(';','')
        
        amount_float.append(float(line))
           
        
  # fixing it to mimir
  # above I organized the name of airports in only one list and, did
  #similar thing for the other data. This solution got me to get the final
  # output of this project, but it didn't fullfil the requirements on mimir.
  # Therefore I started to organize the data, on the lines below so that it passes
  # the mimir test for this function
  
  # Here
  
  
    lst=[]
    
    i=0
    
    while i < len(yr):
        # ceating a list of tuples to be returned
        m=(yr[i],airport_f[i],amount_float[i],status_f[i],c_amount_float[i])
      
        lst.append(m)
        i+=1
    
    return lst
             


def process(data):
    
    '''
    This will process the data before it is displayed
    Value: The arguments processed is a list
    Returns: a list
    
    '''

    
    # ORGANIZING THE DATA TO BE USED
    
    years=[]
    airport=[]
    amount=[]
    status=[]
    c_amount=[]
    
    
    i=0 
    
    y=data[0]
    
    while i < len(data):
        
            y=data[i]
            
            years.append(y[0])
            airport.append(y[1])
            amount.append(y[2])
            status.append(y[3])
            c_amount.append(y[4])
            
            i+=1  
        
        
    # status of each year in separte lists 
    
    status_02 = []
    status_03 = []
    status_04 = []
    status_05 = []
    status_06 = []
    status_07 = [] 
    status_08 = []
    status_09 = []
    
    i=0
    y=data[0]
    
    
    # creating a indeividual status list corresponding to its respective year
    while i < len(data):
        
            y=data[i]
            
            if '02' in y[0][-2:]:
                status_02.append(status[i])
                
            if '03' in y[0][-2:]:
                status_03.append(status[i])    
            
            if '04' == y[0][-2:]:
                status_04.append(status[i])
                
            if '05' in y[0][-2:]:
                status_05.append(status[i])  
                
            if '06' in y[0][-2:]:
                status_06.append(status[i])
                
            if '07' in y[0][-2:]:
                status_07.append(status[i])  
                
            if '08' in y[0][-2:]:
                status_08.append(status[i]) 
                
            if '09' in y[0][-2:]:
                status_09.append(status[i])   
                
            i+=1 
            
    
    
    # all the data reffering to its classification is put togther.
    
    data=[airport, amount, status, c_amount, status_02, status_03, status_04, status_05, status_06, status_07, status_08, status_09 ]
    STATUS = ['Approved','Denied','Settled'] 
    
    total_approved=0
    total_denied = 0
    total_settled= 0
    
    for line in data[2]:
        
        # approved
        if line == STATUS[0]:
            
            total_approved += 1
            
        else:
            pass
      
        if line == STATUS[1]:
            
            total_denied +=1
        else:
            pass
            
        if line == STATUS[2]:
            
            total_settled += 1
        else:
            pass
    
  
    total =  total_settled +  total_denied + total_approved 
          
    
    i=0
    my_tuple_a = data[3]
    t2 = data[2]
    sum_approved = 0
    sum_settled = 0
    c_app=0
    c_sett=0
    
    
    while i < len(my_tuple_a): 
        
        # getting the sum of approved
        if t2[i]== STATUS[0] and my_tuple_a[i] != 0.0:
            
            t= my_tuple_a[i]
            
            sum_approved += t
            c_app += 1
            
        else:
            pass
            
        if t2[i]== STATUS[2] and my_tuple_a[i] != 0.0:
            
            t1= my_tuple_a[i]  
            
            sum_settled += t1
            
            c_sett += 1
        else:
            pass
            
        
        i +=1
    # here us the average settlement
    
    average = (sum_approved + sum_settled) / (c_sett  + c_app)
    
    max_n = 0
    
    # Max claim amout here
    for line in data[1]:
        
        if line > max_n:
            
            # here
            max_n= line
            
            
    airports = data[0]
    amount=data[1]
    i=0
    
    # Name of max claim airport
    
    while i < len(amount): 
        
        if amount[i] == max_n :
            
            # Here
            airport_max = (airports[i])
            
        i +=1
        
    #################################################
    # TOTAL FOR EACH YEAR (approved + settled + denied)
    
    total_02 = tota_1(data[4])
    total_03 = tota_1(data[5])
    total_04 = tota_1(data[6])
    total_05 = tota_1(data[7])
    total_06 = tota_1(data[8])
    total_07 = tota_1(data[9])
    total_08 = tota_1(data[10])
    total_09 = tota_1(data[11])
   
       
    list1=[total_02, total_03,total_04,total_05,total_06,total_07,total_08,total_09]
    
    # TOTAL FOR EACH YEAR (approved + settled )
    total_02 = tota_2(data[4])
    total_03 = tota_2(data[5])
    total_04 = tota_2(data[6])
    total_05 = tota_2(data[7])
    total_06 = tota_2(data[8])
    total_07 = tota_2(data[9])
    total_08 = tota_2(data[10])
    total_09 = tota_2(data[11])
    
    list2=[total_02, total_03,total_04,total_05,total_06,total_07,total_08,total_09]
    
    # TOTAL FOR EACH YEAR ( denied)
    
    total_02 = tota_3(data[4])
    total_03 = tota_3(data[5])
    total_04 = tota_3(data[6])
    total_05 = tota_3(data[7])
    total_06 = tota_3(data[8])
    total_07 = tota_3(data[9])
    total_08 = tota_3(data[10])
    total_09 = tota_3(data[11])
    
    
    
    list3=[total_02, total_03,total_04,total_05,total_06,total_07,total_08,total_09]
    
    return (list1, list2, list3, total, average, max_n, airport_max)


def tota_1(m):
        '''
        This function will calculate the total for(approved + settled + denied)
        Value: The arguments processed are a list
        Returns: a float 
    
        '''
        STATUS = ['Approved','Denied','Settled'] 
        
        approved=0
        denied = 0
        settled= 0
        
        for line in m:
            
            # approved
            
            if line == STATUS[0]:
                
                approved += 1
            else:
                pass
             # Denied    
            if line == STATUS[1]:
                
                denied +=1
            else:
                pass
             # Settled    
            if line == STATUS[2]:
                
                settled += 1 
            else:
                pass
         
        total = approved + denied + settled  
            
        return total               
  
           
def tota_2(m):
    
        '''
        This function will calculate the total for(approved + settled )
        Value: The arguments processed are a list
        Returns: a float 
    
        '''
        
        STATUS = ['Approved','Denied','Settled'] 
        
        approved =0
        settled = 0
    
        
        for line in m:
            
            # approved
            
            if line == STATUS[0]:
                
                approved += 1
            else:
                pass
          
            if line == STATUS[2]:
                
                settled+= 1  
            else:
                pass
          
           
        total = approved + settled
            
        return total  

             

def tota_3(m):
    
        '''
        This function will calculate the total for(denied)
        Value: The arguments processed are a list
        Returns: a float 
    
        '''
        
        STATUS = ['Approved','Denied','Settled'] 
        
        
        denied = 0
          
        for line in m:
                
            if line == STATUS[1]:
                
                 denied += 1 
            else:
                pass
         
           
        total = denied
            
        return total 
    
    

def display_data(tup):
    
    '''
    Will display the formated data
    Value: The arguments processed is a tuple
    Returns: does no return anything 
    
    '''
    
    print("TSA Claims Data: 2002 - 2009")
    print()
    print('N = {:,d}'.format(tup[3]))
    print("{:<8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}".format(" ",'2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009'))
    
    l1 = tup[0]
    l2 = tup[1]
    l3 = tup[2]
    
    print("{:<8s}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}".format('Total',l1[0],l1[1],l1[2],l1[3],l1[4],l1[5],l1[6],l1[7]))
    print("{:<8s}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}".format('Settled',l2[0],l2[1],l2[2],l2[3],l2[4],l2[5],l2[6],l2[7]))
    print("{:<8s}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}".format('Denied',l3[0],l3[1],l3[2],l3[3],l3[4],l3[5],l3[6],l3[7]))
    print()
    
    print('Average settlement:','$'"%.2f    " % tup[4])
    
    n = "%.2f" % tup[5]
    n= float(n)
    
    print('The maximum claim was','${:,.2f}'.format(n) , 'at',tup[6],'Airport')


def plot_data(accepted_data, settled_data, denied_data):
    
    '''
    This function uses a selected previous extracted data to plot a graph
    Value: the arguments are lists
    Returns: Does not return anything, but will plot a graph
    '''
    
    question= input('Plot data (yes/no): ')
    if question.upper() == 'YES':
        X = pylab.arange(8)   # create 8 items to hold the data for graphing
        # assign each list's values to the 8 items to be graphed, include a color and a label
        pylab.bar(X, accepted_data, color = 'b', width = 0.25, label="total")
        pylab.bar(X + 0.25, settled_data, color = 'g', width = 0.25, label="settled")
        pylab.bar(X + 0.50, denied_data, color = 'r', width = 0.25,label="denied")
    
        # label the y axis
        pylab.ylabel('Number of cases')
        # label each bar of the x axis
        pylab.xticks(X + 0.25 / 2, ("2002","2003","2004","2005","2006","2007","2008","2009"))
        # create a legend
        pylab.legend(loc='best')
        # draw the plot
        pylab.show()
        # optionally save the plot to a file; file extension determines file type
        # pylab.savefig("plot.png")
   
def main():
    '''
    This function is where the other functions are called, and where
    the object file is closed.
    Value: has no argument
    Returns: Does not return anything
    '''
    
    data_open = open_file()
    
    reading = read_file(data_open)
    
    processing = process(reading)
    
    displaying = display_data(processing)
    
    ploting = plot_data(processing[0],processing[1],processing[2])
    
    data_open.close()
    
if __name__ == "__main__":
    main()