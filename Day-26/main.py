# new_nums = [new_item for item in list]
# You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain
# every number in the list numbers but each number should be squared.
#
# e.g. `4 * 4 = 16`
# 4 squared equals 16.
# DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.
#
# Example Output
# [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n**2 for n in numbers]
# print(squared_numbers)
# write a List Comprehension to create a new list called result. This new list should only contain the even numbers.
# Example Output
# [2, 8, 34]
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [n for n in numbers if n % 2 == 0]
# print(result)
# Create a list called result which contains the numbers that are common in both files.
# IMPORTANT: The result should be a list that contains Integers, not Strings.
with open("file1.txt") as file1:
    f1 = file1.readlines()
    # f1 = [s.rstrip() for s in f1]
with open("file2.txt") as file2:
    f2 = file2.readlines()
    # f2 = [s.rstrip() for s in f2]
result = [int(num) for num in f1 if num in f2]

# Example Output
# [3, 6, 5, 33, 12, 7, 42, 13]
print(result)