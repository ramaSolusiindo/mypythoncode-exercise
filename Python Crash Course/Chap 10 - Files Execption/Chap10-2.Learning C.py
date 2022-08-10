"""
 Exercise replace string with a different word
"""

filename = "../Chap 9 - Class/learning_python.txt"
with open(filename) as fileobject:
    content = fileobject.read()

new_content = content.replace('Python', 'C')
print(new_content)
