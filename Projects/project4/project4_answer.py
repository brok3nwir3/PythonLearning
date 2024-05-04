# Custom Encryption Program
# (Project4)
# Author: Phil van der Linden
# Date: 05/01/2024

import os
import rsa
import time
from ast import literal_eval

print("Running custom encryption program...\n")

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
    print("Saving a new private key and public key to current directory...\n")
    publicKey, privateKey = rsa.newkeys(512)
    print("Public key: ", publicKey)
    print("Privat key: ", privateKey)
    time.sleep(1)

    pub_key_file = open('public_key.txt', 'w')
    pub_key_file.write(str(publicKey))
    pub_key_file.close()
    priv_key_file = open('private_key.txt', 'w')
    priv_key_file.write(str(privateKey))
    priv_key_file.close()

    path = os.getcwd()
    dir_list = os.listdir(path)
    
    print("\nFiles in current directory '" + path + "' :\n", dir_list)

    # Select a file.
    legal_selection = False
    while legal_selection == False:
        file_choice = input("\nWhich text file would you like to encrypt?\n")
        if file_choice[-4:] != ".txt":
            print("Only .txt files are allowed.")
        else:
            legal_selection = True

    file_selection = file_choice
    text_file = open(file_selection, "r")
    content = text_file.read()

    hex_str = ""
    for char in content:
        hex_str += hex(ord(char))

    enc_message = rsa.encrypt(hex_str.encode(), publicKey)
    time.sleep(1)
    print("original string: ", hex_str)
    time.sleep(1)
    print("encrypted string: ", enc_message)

    enc_file = open('encrypted.txt', 'wb')
    enc_file.write(enc_message)
    enc_file.close()

### DECRYPTION CODE ###

else:
    print("Using local key files and encrypted text file...\n")
    time.sleep(1)

    pub_key_file = open('public_key.txt', 'r')
    pub_key_data = pub_key_file.read()
    priv_key_file = open('private_key.txt', 'r')
    priv_key_data = priv_key_file.read()
    enc_file = open('encrypted.txt', 'rb')
    enc_file_data = enc_file.read()

    #keyPriv = rsa.ImportKey(priv_key_data)
    #keyPriv = rsa.PrivateKey.load_pkcs1(priv_key_data)

    dec_message = rsa.decrypt(enc_file_data, priv_key_data).decode()
    #dec_message = rsa.decrypt(ast.literal_eval(str(priv_key_data)))
    print("decrypted string: ", dec_message)