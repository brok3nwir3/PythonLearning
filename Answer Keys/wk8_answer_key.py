# Week 8 - Assignment Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v

























# Q1:
sentence = 'dogs are super cool and dogs are the best animal.'

print(sentence.replace('dog', 'seagull'))

# Q2:
'''
My name is Alice. I wrote this program in the year 2023,
while I worked at Seagull Inc. My program checks a long
list of awesome animals and gives them a score,
based on how awesome they are.
'''

# Q3:
crazyString = 'e-R-Ror.oU-tp-Ut.i-s.O-F-T-en.diF-Fi-cult.T-O.rea-D.Wi-tHouT.ReFo-rMA-ttIn-G'

lowerized = crazyString.lower()
replacies = lowerized.replace('-','')
splitz = replacies.rsplit('.')

final_string = splitz
print(final_string)

# Bonus...
for word in range(len(final_string)):
    print(final_string[word])
    
# Q4:
import os
print('The current user is: ', end="")
print(os.getlogin())
print('The working directory is: ', end="")
print(os.getcwd())

# Q5:
item1 = 'He finished playing without a single mistake.'
item2 = 'For the sake of Jake we started clapping.'
item3 = 'She was waiting on the god forsaken island.'
bobs_list = [item1, item2, item3]

for word in range(len(bobs_list)):
    ake = bobs_list[word].replace('ake','') #Note capitals are skipped.
    w_remove = ake.replace('w', '')
    f_remove = w_remove.replace('t', '')
    final_string = f_remove
    print(final_string)
    
#Q6:
testString = 'Zebras ZOOM in zig-zag patterns to escape lions with zeal.'

lowerize = testString.lower()
print(lowerize.count('z'))

# Q7:
import os
iterations = 50
while iterations > 1:
    os.system('clear')
    print("\n*----")
    os.system('clear')
    print("\n**---")
    os.system('clear')
    print("\n***--")
    os.system('clear')
    print("\n****-")
    os.system('clear')
    print("\n*****")
    iterations = iterations - 1