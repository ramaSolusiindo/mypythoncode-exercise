import random
# Step 1

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess.
#  Make guess lowercase.
guess = input("Please guess a letter ? ").lower()
#print(guess)


# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# for i in range(0, len(chosen_word)):
#     if guess == chosen_word[i]:
#         print("Correct")
#     else:
#         print("False")

for letter in chosen_word:
    if guess == letter:
        print("Correct")
    else:
        print("False")