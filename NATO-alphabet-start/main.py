
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
student_data_frame = pandas.DataFrame(data)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

new_dict = {row.letter:row.code for (index,row) in student_data_frame.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

abbreviation = input("Whats your name?\n").upper()

name_list = [new_dict[letter] for letter in abbreviation]

print(name_list)