"""
 Exercise writing to a file, append to a file, writing multiple lines
"""
filename = "programming-test.txt"
with open(filename, 'w') as file_object :
    file_object.write("I love programming ")

with open(filename, 'a') as file_object :
    file_object.write(str(2022)+ '\n')

with open(filename,'a') as file_object:
    file_object.write("I love creating a game \n")

with open(filename,'a') as file_object:
    file_object.write('I also love finding meaning in large datasets.\n')
    file_object.write('I love creating apps that can run in a browser.\n')

with open(filename) as file_object:
    content = file_object.read()

print(content)

