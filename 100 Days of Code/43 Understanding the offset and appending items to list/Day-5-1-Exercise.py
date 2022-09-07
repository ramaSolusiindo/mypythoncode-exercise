# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
jumlah = 0
hitung = 0
for student in student_heights:
    jumlah = jumlah + student
    hitung = hitung + 1

average = jumlah / hitung

print("Hasil rata-rata 'student-height' dalam pembulatan : ", round(average))
print("Hadil dari jumlah adalah : ", jumlah)

"""

"""

