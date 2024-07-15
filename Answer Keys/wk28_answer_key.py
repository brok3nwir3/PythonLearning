# Week 28 - Quiz Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
interview_list = [345, 22, 89, 9, 705, 11, 64, 703]

largest = 0
for num in interview_list:
    if num > largest:
        largest = num
print(largest)

# Q2
join_list = ['Ice', 'cream', ' is ', 'Bobs ', 'favorite ', "dessert."]

sentence = ''.join(join_list)
print(sentence)

# Q3
# A) What is the extension of the file that's created?
# .pickle
# B) What function is used to serialize the data?
# .dump()
# C) What function is used to deserialize the data?
# .load()
# D) What is the point of serializing data?
# To convert an object into a format that can be stored or transmitted.
# E) Why is there a warning if you try to view the file created by the code?
# Opening untrusted binary files (or deserializing) binary files can result in the execution of arbitrary system commands.

# Q4
import pickle
import os
my_object = {'A': 123, 'B': [1, 2, 3], 'C': {'X': 0, 'Y': 9}}
with open('my_object.pickle', 'wb') as f:
    pickle.dump(my_object, f)
with open('my_object.pickle', 'rb') as f:
    loaded_object = pickle.load(f)
print(loaded_object)
os.system('sha1sum my_object.pickle')

# Q5
import ipaddress
net = ipaddress.ip_network('123.45.67.64/27')
count = 0
ip_array = []
for a in net:
    print(a)
    count += 1
    ip_array.append(a)
print(count, 'total IP addresses in the provided network range.')
print(ip_array)

# Q6
import ipaddress
test_address = ipaddress.ip_interface('1.1.1.1/13')
print(test_address.netmask)
print(test_address.netmask.is_private)

# Q7
import os
my_ip = os.system("ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'")

# Q8
import os
my_ip = os.system("ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'")
print(my_ip) # This returns 0, which simply means the command ran successfully.
my_ip2 = os.popen("ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'").read()
print(my_ip2) # This returns the desired output.
# Note: The .popen() function allows programmers to access the subprocess pipe output.

# Q9
import os 
test_ping = os.popen("ping -c 1 8.8.8.8 ").read()

# Version without the BONUS code.
temp = ''
for data in test_ping:
    if data != ' ':
        temp += data
    else:
        print(temp)
        temp = ''

# Version w/ BONUS code.

# Scroll down.
# |
# |
# v
        






        
trigger = False
received = False
temp = ''
for data in test_ping:
    if trigger == True:
        if data == '1':
            received = True
    if data != ' ':
        temp += data
        if temp == 'received,':
            trigger = True
    else:
        print(temp)
        temp = ''

if received == True:
    print('\nPacket Received!')
else:
    print('\nPing Failed.')