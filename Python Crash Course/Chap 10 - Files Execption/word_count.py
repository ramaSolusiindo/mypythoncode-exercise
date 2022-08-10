"""
--- Working with multiple files
"""


def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        word = content.split()
        num_words = len(word)
        print(f"The file {filename} has about {num_words} words")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    count_words(filename)
