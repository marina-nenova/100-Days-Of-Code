import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for index, row in nato_alphabet.iterrows()}

user_input = input("Which word would you like to convert? ")

code_words = [alphabet_dict[ch.upper()] for ch in user_input]
print(code_words)

