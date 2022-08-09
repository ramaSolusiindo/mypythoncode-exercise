"""
 Exercise write a program that prompt the user for their name and write their name to a file
 called guest.txt
"""
username = input('Please type your name : ')
filename = 'guest.txt'

with open(filename,'w') as file_object:
    file_object.write(username)

