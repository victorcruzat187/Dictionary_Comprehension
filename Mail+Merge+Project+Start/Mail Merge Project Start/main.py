#TODO: Create a letter using starting_letter.txt
#letter = open("./input/letters/starting_letter.txt", "r")
#invited_ppl = open("./input/Names/invited_names.txt", "r")
#name = invited_ppl





 #   print(letter.readlines(1))

.
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#Replace the [name] placeholder with the actual name.
PLACEHOLDER = "[name]"
#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    # for name in letter:
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        # Save the letters in the folder "ReadyToSend"
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)