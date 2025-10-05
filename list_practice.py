"""Write a Python script that concatenates two lists and prints the result"""
# # Define two lists
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# # Concatenate the lists
# concatenated_list = list1 + list2

# # Print the concatenated list
# print(concatenated_list)

"""Write a Python script that repeats a list three times and prints the result"""
# Define the list
# my_list = [1, 2, 3]

# # Repeat the list three times
# repeated_list = my_list * 3

# # Print the repeated list
# print(repeated_list)

"""Write a Python script that removes the elements at even indices from a list"""
# Define the original list
my_list = [10, 20, 30, 40, 50, 60]

# Use slicing to get elements at odd indices
filtered_list = my_list[1::2]

# Print the filtered list
print(filtered_list)


"Example2"
# Define the original list
# my_list = [10, 20, 30, 40, 50, 60]

# # Remove elements at even indices (0, 2, 4, ...)
# filtered_list = [my_list[i] for i in range(len(my_list)) if i % 2 != 0]

# # Print the filtered list
# print(filtered_list)

"""Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of
a list
"""
# # Define the original list
# my_list = [1, 2, 3, 4, 5]

# # Insert 10, 11, and 12 at the beginning of the list
# my_list = [10, 11, 12] + my_list

# Print the updated list
# print(my_list)

"""Square Numbers: Create a list of squares of numbers from 1 to 10"""
# squares = [x**2 for x in range(1, 11)]
# print(squares)

"""Even Numbers: Generate a list of even numbers from 1 to 20"""
# evens = [x for x in range(1, 21) if x % 2 == 0]
# print(evens)

"""Words Lengths: Given a list of words, create a list containing the lengths of each word"""
# words = ["apple", "banana", "cherry", "date"]
# lengths = [len(word) for word in words]
# print(lengths)

