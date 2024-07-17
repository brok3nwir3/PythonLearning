# Week 29 - Quiz Answer Key

# AVOID PEEKING AHEAD OF TIME!










# Scroll down.
# |
# |
# v




























# Q1
# The following solution is a more eloquent answer.
# The interviewee should begin by figuring out the length of the list and dividing by 2, i.e. the halfway point of the list.
# The problem is that in some cases this will result in a decimal number, such as 2.5.
# To address this problem, you can cast the decimal to an integer, which will round a number like 2.5 to 3.
# Lastly we use the final number to be the element number to print.
num_list = [1, 2, 3, 4, 5]
mid_element = int((len(num_list)/2))
print(num_list[mid_element])

# Q2
original_list = [10, 90, 9, 17, 23, 81, 27, 55, 46]
new_list = [x for x in original_list if x%9 == 0]
print(new_list)

# Q3
name = input("Please enter your first name: ")
first_char = False
fixed_name = ''
for char in name:
    if first_char == False:
        fixed_name += char.upper()
        first_char = True
    else:
        fixed_name += char.lower()
print(fixed_name)

# Q4
my_array = [105, 19, 2000, 777, 89, 17, 504, 32]
target = 17

index = 0
for num in my_array:
    if num == target:
        print(index)
    else:
        index += 1

# Q5
my_array2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target2 = 7

mid_element = int((len(my_array2)/2))
print("The middle element is:", mid_element)

if my_array2[mid_element] >= target2:
    # Search first half.
    start_element = 0
    print("The target is in the first half of the array.")
else:
    # Search second half.
    start_element = mid_element
    print("The target is in the second half of the array.")

search = True
while search == True:
    if my_array2[start_element] != target2:
        start_element += 1
    else:
        search = False
        print("Target found at index:", start_element)

# Q6
# Note: You can uncomment the x4 print statements below to watch the array change with the run of each loop.
bubble_array = [5, 3, 1, 4, 2]
temp = 0
index = 0
count = 0
#print(len(bubble_array))
# We use 
while count <= len(bubble_array):
    #print("RUN", count)
    index = 0
    for num in bubble_array:
        #print(bubble_array)
        #print("index", index)
        # This first IF condition prevents us from getting an index out of bounds error.
        if index < len(bubble_array)-1:
            # This IF statement compares two adjacent numbers, to see if the number on the left is smaller.
            if (bubble_array[index] > bubble_array[index+1]):
                # If the condition was true, we use our temp variable to store a number while we swap data around.
                temp = bubble_array[index+1]
                bubble_array[index+1] = bubble_array[index]
                bubble_array[index] = temp
        index += 1
    count += 1

print(bubble_array)

# Q7 - BONUS
   
# Scroll down.
# |
# |
# v
        









unsorted_array = [5, 3, 1, 4, 2]
sorted_array = []

# Determine the number of indicies of the unsorted array.
array_indices = len(unsorted_array)-1

# To create a new sorted_array[], we need to run this while loop X times where X is the index length of the unsorted_array[].
while array_indices >= 0:
    # Each run of this loop we reset the value for the largest number and its index.
    largest_num = unsorted_array[0]
    largest_index = 0
    # We then check the see if any number is larger than the default number. If so, update the number and index.
    for num in unsorted_array:
        if num > largest_num:
            largest_num = num
            largest_index = unsorted_array.index(largest_num)

    # Some print statements for troubleshooting...
    #print("current largest num", largest_num)
    #print("index of largest num", temp_index)
    #print(unsorted_array)
            
    # We then add our current largest number to the beginning of our sorted_array[].
    sorted_array.insert(0, largest_num)
    # We also remove the current largest number from the unsorted_array[].
    unsorted_array.remove(unsorted_array[largest_index])
    # Lastly, we have to reduce the current indices amount.
    array_indices -= 1

print(sorted_array)