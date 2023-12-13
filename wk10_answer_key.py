# Week 10 - Assignment Answer Key

# Q1
# import re as reggie

# Q2
# x = dir(reggie)
# print(x)

# Q3
# .search checks the whole string.
# .match checks from the beginning of the string.

# Q4
# mytest = reggie.search(r'lazer', bob_test)
# print(mytest)

# Q5
# my_var1 = 'tank'
# my_var2 = 'tail'

# test_1 = reggie.match(r'^t..k$', my_var1)
# if test_1:
#     print(test_1)

# test_2 = reggie.match(r'^t..k$', my_var2)
# if test_1:
#     print(test_2)

# Q6
# test1 = reggie.search(r'^[a-z]{5}[0-9]{2}$', var1)
# print(test1)

# test2 = reggie.search(r'^[a-z]{5}[0-9]{2}$', var2)
# print(test2)

# Q7
# alice_test1 = reggie.search(r'[\w.-]+@[\w.-]+', alice_var1)
# print(alice_test1)

# alice_test2 = reggie.search(r'[\w.-]+@[\w.-]+', alice_var2)
# print(alice_test2)