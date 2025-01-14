# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary in this format:
phonetic_dict = {row.email_body: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# Create a list of the phonetic code words from a word that the user inputs.


def generate_word():
    word = input("Enter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters")
        generate_word()
    else:
        print(output_list)


generate_word()
