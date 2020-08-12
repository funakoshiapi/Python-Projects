x= 0

VOWELS = "aeiou"
modified_word = 'b' 

while(x==0):

    orig_str = input("Enter a word ('quit' to quit): ")

    my_str = orig_str.lower()

    if my_str == 'quit':
        break

    if not my_str:
        
        print("Can't convert empty string.  Try again.")
        orig_str = input("Enter a word ('quit' to quit): ")

        my_str = orig_str.lower()
      
        
                
    if my_str[0] in VOWELS:
        
        word_1 = my_str+"way"
        
        print(word_1)
        
        

    else:
        
        consonats=''
        stub=''
        
        for index, ch in enumerate(my_str):
            
            if my_str[index] not in VOWELS:
                consonants = consonats + ch
            
                
            else:
                stub = my_str[index:]
                consonants = my_str[:index]
            
                word = stub+consonants+"ay"
                
                print(word)
                break
                
        else:
          print(modified_word+"ay")
                
            
       