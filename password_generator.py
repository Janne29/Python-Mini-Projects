#
#   This program generates a random password
#
#   You can specify the length and the symbols that will be used
#

import random
import string

# Create the variables for all the letters, numbers and symbols
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

length = int(input("How long should the password be? ")) # Get the length of the password

all = '' # Create the variable where all possible symbols will be stored in

if input("Use characters? y/n: ") in ('y', 'yes'): all += letters   # Add letters to the possible symbols

if input("Use numbers? y/n: ") in ('y', 'yes'): all += numbers  # Add numbers to the possible symbols

if input("Use symbols? y/n: ") in ('y', 'yes'): all += symbols  # Add the special symbols to the possible symbols

password = '' # Create the password variable

for i in range(length):
    password += all[random.randint(0, len(all)-1)] # Add a random symbol to the password

print(f'Here is your password: {password}') # Print out the generated password