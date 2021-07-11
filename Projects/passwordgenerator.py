import random
import array
  
#max length of the password
MAX_LEN = 48
  

DIGITS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
LOCASE_CHARACTERS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z')
  
UPCASE_CHARACTERS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z')
  
SYMBOLS = ('@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
           '*', '(', ')', '<')
  
#creates a combined list
COMBINED_LIST = (DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS)



# randomly select at least one character from each character set above
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)
  
#ensures that there is a character from each tuple
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
  
  
#fill the rest and randomise
for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
    #the u stands for unicode
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
  
#takes the letter in temp password and places it inside the password
password = ""
for x in temp_pass_list:
        password = password + x
          
print(password)