
"""
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
"""

import pandas
# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# with ("nato_phonetic_alphabet.csv")
phonetic_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(phonetic_data)
# print(phonetic_data.to_dict())  # this does not work in this case

for (index, alphabet) in phonetic_data.iterrows():
    # print(alphabet)
    pass
nato_phonetic_alphabet = {alphabet.letter: alphabet.code for (index, alphabet) in phonetic_data.iterrows()}
# print(nato_phonetic_alphabet)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
# print(nato_phonetic_alphabet.keys())
phonetic_words = [nato_phonetic_alphabet[letter] for letter in user_input]
print(phonetic_words)

# # phonetic = [nato_phonetic_alphabet.keys() for i in user_input if i == nato_phonetic_alphabet.keys()]
# # for i in user_input:
# #     # print(i)
# #     phonetic = [code for (letter, code) in nato_phonetic_alphabet.items() if letter == i]
# # # for (letter, code) in nato_phonetic_alphabet.items():
# # #     if letter == i:
# # #         print(code)
# print(phonetic_words)


# # Initial Code
# user_input = input("Enter a word: ").upper()
# phonetic_words = [nato_phonetic_alphabet[letter] for letter in user_input]
# print(phonetic_words)

# With Try Catch of KeyError
def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        phonetic_words = [nato_phonetic_alphabet[letter] for letter in user_input]
    except KeyError:
        print(f"Sorry, only letters in the alphabet please. You inputted: {user_input}.")
        generate_phonetic()
    else:
        print(phonetic_words)


generate_phonetic()

""" My trial with Error Handling
while True:
    user_input = input("Enter a word: ").upper()
    phonetic2 = []
    try:
        for i in user_input:
            # print(i)
            # print(nato_phonetic_alphabet[i])
            # phonetic2 += nato_phonetic_alphabet[i]  # Wrong - it adds each letter as a string.
            # phonetic2 = phonetic2.append(nato_phonetic_alphabet[i])  # this is wrong - \
            # AttributeError: 'NoneType' object has no attribute 'append'

            phonetic2.append(nato_phonetic_alphabet[i])  # correct one
    except KeyError:
        print(f"Sorry, only letters in the alphabet please. You inputted: {user_input}.")
        continue
    else:
        print(phonetic2)
    # print(phonetic2)

"""