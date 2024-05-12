# Project 4 (100 Points) - Encrypt/Decrypt

# This project will test your ability to do the following...
# 1. Manipulate data.
# 2. Read local files.
# 3. Write new local files.
# 4. Use encryption/decryption.
# 5. Encode/decode binary or hexadecimal.

# The goal of the project is to write two programs; one to encrypt a file and another to decrypt a file.
# Note: Alternatively, the programs can be combined into a single program.

# The first program will read a local text file containing normal ASCII.
# As the program reads the file, it will convert the string data on each line to either binary or hexadecimal (your choice).
# Then the program will then encrypt the hexadecimal text (free choice on which encryption library to use).
# Note: Some encryption modules include... Fernet, RSA, AES, etc. (most of these will be part of the Cryptography library).
# The encryption should save the key value (if one is used) to a file called "key.txt" or something similar.
# The encrypted text should then be written to a new file called "encrypted.txt"
# Bonus: Give the output file name "<original_name>_encrypted.txt" or "encrypted_<original_name>.txt"

# The second prgram will read the files contents and decrypt them, using a key.
# The program will then convert the file back to ASCII from binary or hex.
# The decrypted text will then be written to a new file called "decrypted.txt"
# Bonus: Give the output file name "<original_name>_decrypted.txt" or "decrypted_<original_name>.txt"

# The final program should be able to encrypt and decrypt two .txt test files.

# The first test file contains:
# hello

# The second test file contains:
# 3ncrypT n PyThoN... & d3Crypt n PyTh0n!

# Grading Rubric...
# 1) Does the program work? (60 Points)
#   a) The program reads a local text file.
#   b) Converts/unconverts strings to binary/hex.
#   c) Encrypts/decrypts the strings.
#   d) Writes a new local file with the encrypted/decrypted data.
# 2) Can you explain the code, and answer questions about the code? (40 Points)
#   a) Which encryption module did you use? Why?
#   b) How are files read/written?
#   c) In laymans terms, how was the original file encrypted?
#   d) How did you encode/decode the ASCII?
#   e) How did the program know which file to encrypt/decrypt?
# 3) Does your program have any bonus flavor? (10 Points)
#   a) Does the program include ASCII art?
#   b) File naming format (bonus points).
#   c) Was any other interesting terminal output included?