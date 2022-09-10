# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
"""
Important You should not use the sum() or len() functions in your answer.
You should try to replicate their functionality using what you have learnt about for loops.
"""

# Write your code below this row 👇
jumlah = 0
hitung = 0
for student in student_heights:
    jumlah = jumlah + student
    hitung = hitung + 1

average = jumlah / hitung

print("Hasil rata-rata 'student-height' dalam pembulatan : ", round(average))
print("Hadil dari jumlah adalah : ", jumlah)


total_height = sum(student_heights)
num_of_student = len(student_heights)
average_student = round(total_height / num_of_student)


