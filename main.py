import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter: row.code for (index, row) in df.iterrows()}

input_word = input("Enter a word: ")

output_list = [alphabet[letter.upper()] for letter in input_word]

print(output_list)
