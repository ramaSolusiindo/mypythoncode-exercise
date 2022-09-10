# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
"""
Important you are not allowed to use the max or min functions. 
The output words must match the example. i.e

The highest score in the class is: x
"""
# Write your code below this row 👇
max_number = 0
for score in student_scores:
    if score > max_number:
        max_number = score

print(max_number)
