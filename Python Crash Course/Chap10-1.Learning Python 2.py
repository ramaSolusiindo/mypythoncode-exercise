"""
 exercise read files
"""
filenames = 'learning_python.txt'

print("--- Reading in the entire file:")
with open(filenames) as fileobject:
    content = fileobject.read()

print(content)

print("\n--- Looping over the lines:")
with open(filenames) as fileobject:
    for content in fileobject:
        print(content.rstrip())

print("\n--- Storing the lines in a list:")
with open(filenames) as fileobject:
    content = fileobject.readlines()

for line in content:
    print(line.rstrip())

