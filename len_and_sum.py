#LOOPS
# student_heights = [180, 124, 165, 173, 189, 169, 146]
# total = 0
# for n in student_heights:
#   total = total + n
# print(total/len(student_heights))

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#   (student_heights[n]) += (student_heights[n])
#   average = (student_heights[n])/(n+1)
# print(round(average))

# Calculate max wo max()

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# highest = 0
# for score in student_scores:
#   if score > highest:
#     highest = score

# print(f"The highest score in the class is: {highest}")

#sum even bt 1-100 with range():
# total = 0
# for i in range(2, 101, 2):
#   total += i
# print(total)
# OR
# res = sum(x for x in range(1, 100) if x % 2 == 0)
# print(res)
# OR
total = 0
for i in range(1, 101):
  if i % 2 == 0:
    total += i
print(total)