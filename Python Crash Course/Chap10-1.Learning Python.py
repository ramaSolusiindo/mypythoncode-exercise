"""
 exercise read files
"""
filenames = 'Chap10-FilesExecption-pi_digit.txt'
with open(filenames) as file_object:
    lines = file_object.readlines()

with open(filenames) as file_object:
    baca = file_object.read()

with open(filenames) as file_object:
    baca2 = file_object.readline()


print(f"This is readlines result : {lines}")
print(f"This is read result : \n{baca}")
print(f"This is readlines result : {baca2}")

pi_string = ''
for line in lines:
    # pi_string += line.rstrip()
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
pi_int = float(pi_string)
print(type(pi_string))
print(type(pi_int))


"""
with open('Chap10-FilesExecption-pi_digit.txt') as file_object:
    contents = file_object.read()

filepath = 'C:/Users/Lenovo T470s/Documents/seskoTNI.txt'
with open(filepath) as file_object2 :
    contents2 = file_object2.read()
# print(contents)
# remove the blanklines
# print(contents.rstrip())
print(contents2)
"""