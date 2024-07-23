### Encryption Program ###
# Project 5
# Author: Phil van der Linden
# Date: 05/12/2024

# Note: The target file for encryption must have all new lines removed.

from cryptography.fernet import Fernet      # The encryption library we're using.
import os                                   # Used for some Linux OS commands.
import time                                 # Used for visual delays as the code runs.

print("Running encryption program...\n")

# Select a mode.
legal_selection = False
while legal_selection == False:
    mode = input("Choose mode:\n1: Encrypt\n2: Decrypt\n")
    if mode not in ('1', '2'):
        print("Only '1 or '2' can be selected.")
    elif mode == '1':
        print("\nEncryption mode selected.")
        legal_selection = True
    else:
        print("\nDecryption mode selected.")
        legal_selection = True

### ENCRYPTION MODE ###

if mode == '1':
    print("Saving a new Fernet key to current directory...\n")
    fernet_key = Fernet.generate_key() # Create a Fernet key.
    fernet = Fernet(fernet_key) # Set the new Fernet key.
    print("Fernet key saved.")
    time.sleep(1)

    fernet_key_file = open('fernet_key.txt', 'wb')
    fernet_key_file.write(fernet_key)
    fernet_key_file.close()

    path = os.getcwd()
    dir_list = os.listdir(path)
    
    print("\nFiles in current directory '" + path + "' :\n", dir_list)

    # Select a file.
    legal_selection = False
    while legal_selection == False:
        file_choice = input("\nWhich text file would you like to encrypt?\n")
        if file_choice[-4:] != ".txt": # Check for a .txt file extension.
            print("Only .txt files are allowed.")
        else:
            legal_selection = True

    file_selection = file_choice
    text_file = open(file_selection, "r")
    content = text_file.read()

    # Convert the original text to hexadecimal, one character at a time.
    hex_str = ""
    for char in content:
        hex_str += hex(ord(char))

    # Encrypt the hex string with Fernet, and specify the string as hex.
    enc_message = fernet.encrypt(hex_str.encode())

    time.sleep(1)
    print("\nOriginal string as hex: ", hex_str)
    time.sleep(1)
    print("\nEncrypted Fernet string: ", enc_message)

    enc_file = open('encrypted.txt', 'wb')
    enc_file.write(enc_message)
    enc_file.close()
    print("\nEncrypted file saved.")

### DECRYPTION CODE ###

else:
    print("\nUsing local key files and encrypted text file...")
    time.sleep(1)

    fernet_key_file = open('fernet_key.txt', 'rb')
    fernet_key_data = fernet_key_file.read()
    enc_file = open('encrypted.txt', 'rb')
    enc_file_data = enc_file.read()

    restore_key = Fernet(fernet_key_data) # Set the key with Fernet.
    dec_message = restore_key.decrypt(enc_file_data) # Decrypt the data with the Fernet key.
    print("\nHex string extracted.")
    time.sleep(1)

    # Decode hexadecimal characters and remove any hex identifiers.
    temp = dec_message.decode().replace('0x', '')
    ascii_str = ""
    for i in range(0, len(temp), 2):
        part = temp[i : i + 2]
        ch = chr(int(part, 16))
        ascii_str += ch # Build the ASCII string two characters at a time.
    print("\nDecrypted file saved.")

    dec_file = open('decrypted.txt', 'w')
    dec_file.write(ascii_str)
    dec_file.close()