import random

print('''     
                    @@@@@@@               
                (@@@@@, &@@@@@         
             @@@    &@@@@@    @@@      
           &@@  @@@.       @@@  ,@@    
          @@  &@@             @@  @@   
         #@. &@                @@  @@  
        @ @  &@                 @@  @@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
       @@                            &@
       @@ @@@@@%                ,&@@ &@
       @@ %*         @@@@.      *&@@ &@
       @@           @    @           &@
       @@ @@@(.      @  @         .# &@
       @@ @@@&(.     @  @      @@@@@ &@
       @@             &@             &@
       @@ (.                         &@
       @@ @@@@@@@@@@@@@@@@@@@@@@@@@@ &@
 ''')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the on-demand random Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"And finally, how many numbers?\n"))



#Define functions which will return requested random item
def ret_random_letter():
  rand_counter = random.randint(0,25)
  for letter in letters:
    if rand_counter == 0:
      return(letter)
    if rand_counter == 0:break
    rand_counter -= 1

def ret_random_number():
  rand_counter = random.randint(0,9)
  for number in numbers:
    if rand_counter == 0:
      return(number)
    if rand_counter == 0:break
    rand_counter -= 1

def ret_random_symbol():
  rand_counter = random.randint(0,8)
  for symbol in symbols:
    if rand_counter == 0:
      return(symbol)
    if rand_counter == 0:break
    rand_counter -= 1



#Generate empty unshuffled password list
password = []


#Generate and add all requested characters to unshuffled password list
while nr_letters > 0:
  password.append(ret_random_letter())
  nr_letters -= 1
while nr_numbers > 0:
  password.append(ret_random_number())
  nr_numbers -= 1
while nr_symbols > 0:
  password.append(ret_random_symbol())
  nr_symbols -= 1

#Shuffle password list
random.shuffle(password)

#Creation of final password string and filling it up with random primitives
final_pass = ""
for passprimitive in password:
  final_pass += passprimitive

print(f"Your password is {final_pass}, keep it safe!")
