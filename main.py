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

# TODO 1. Create a dictionary in this format:
df_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

dict_alphabet = {row.letter: row.code for (index, row) in df_alphabet.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_code():
    user_word = input("Enter a word: ")
    try:
        new_list = [dict_alphabet[letter.upper()] for letter in user_word]
    except KeyError:
        print("All characters must be letters.")
        generate_code()
    else:
        print(new_list)


generate_code()
