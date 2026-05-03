#TODO: Create a letter using starting_letter.txt
with open("Input/Letters/starting_letter.txt","r") as starting_file:
    content = starting_file.read()
#for each name in invited_names.txt
with open("Input/Names/invited_names.txt","r") as invited_name:
    name_list = []
    for number in range(8):
        name = invited_name.readline()
        n2 = name.strip()
        name_list.append(n2)

with open("Input/Letters/starting_letter.txt","r") as actual_name:
    for item in name_list:
        c2 = content.replace("[name]", f"{item}")
        with open(f"Output/ReadyToSend/{item}.txt","w") as even:
            even.write(c2)









#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp