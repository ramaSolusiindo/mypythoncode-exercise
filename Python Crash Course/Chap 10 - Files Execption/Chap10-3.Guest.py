"""
 Exercise write a program that prompt the user for their name and write their name to a file
 called guest.txt
"""
username = input('Please type your name : ')
filename = '../Chap 9 - Class/guest.txt'

with open(filename,'w') as file_object:
    file_object.write(username)

