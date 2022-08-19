"""
--- Working with multiple files part 2
"""

file_names = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for file_name in file_names:
    try:
        with open(file_name, encoding='utf-8') as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        pass
    # except Exception as e:
        # print(e, type(e))
        # pass
    else:
        num_lines = len(lines)
        msg = f"{file_name} has {num_lines} lines"
        # msg += " lines"
        print(msg)

