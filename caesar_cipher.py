#
#   This program encrypts and decrypts messages with the caesar cipher 
#
#   You can specify how many shifts the cipher uses
#
#   (https://en.wikipedia.org/wiki/Caesar_cipher)
#

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] # Normal alphabet
shifted = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] # Shifted alphabet

message = input("Message: ").lower() # Get the message

shift = int(input("\nHow many characters should be shifted? ")) # Get the

while shift > 25: shift -= 26 # Every shift over 25 can be simplified

# Shift the shifted list
for i in range(shift): 
    char = shifted.pop(0)
    shifted.append(char)

method = input("\nEncrypt or Decrypt: ") # Encrypt or Decrypt the message

modified_message = '' # Create modified message variable

# Swap the characters
for i in range(0, len(message)):

    # Skip empty spaces
    if message[i] == ' ': 
        modified_message += ' '
        continue

    char = message[i] # Get the current character

    # Swap current character with the character in the shifted list
    if method.lower() == "encrypt":
        idx = alphabet.index(char)
        modified_message += shifted[idx]
    
    # Swap current character with the character in the alphabet list
    elif method.lower() == "decrypt":
        idx = shifted.index(char)
        modified_message += alphabet[idx]

print(f'\n{modified_message}') # Print out the encrypted/decrypted message



