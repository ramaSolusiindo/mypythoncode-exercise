"""
Handling the FileNotFoundError Exception
"""
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as file_object:
        content = file_object.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    words = content.split()
    num_words = len(words)
    print(f"Tha file {filename} has about {num_words} words")
