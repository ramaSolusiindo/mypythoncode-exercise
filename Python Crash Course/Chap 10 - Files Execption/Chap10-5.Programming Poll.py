"""
 Exercise write a program that ask the user for their reason and write their name to a file
 called programming-poll.txt
"""
filename = 'programming-poll.txt'
responses = []
while True:
    response = input("\n Why do you like programming? ")
    responses.append(response)

    continue_respon = input ("Whould you like to continue to others ? (y/n) ")
    answer = continue_respon.lower()
    if answer != 'y':
        break

with open(filename, 'a') as file_object:
    for response in responses:
        file_object.write(f"{response}\n")













"""

filename = 'programming-poll.txt'
print("Type 'quit' if you want finished")
while True:
    respons = input('Tell me your reason why you like programming ? ')
    if respons == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{respons} \n")
            print(f"Thanks your responses has been recorded")
            
"""