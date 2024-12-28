import pandas as pd

# create data frame from csv using pandas
df = pd.read_csv("nato_phonetic_alphabet.csv")

# create a dictionary from the data frame
alphabet = {row.letter: row.code for (index, row) in df.iterrows()}

# get input from user
input_word = input("Enter a word: ").upper()

# create a list of the NATO phonetic alphabet for the input word
output_list = [alphabet[letter] for letter in input_word]

print(output_list)
