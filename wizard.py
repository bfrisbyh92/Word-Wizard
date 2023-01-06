# Import the required modules
import os
import sys

# Get the file path of the password list from the user
file_path = input("Enter the path of the password list: ")

# Open the password list file
with open(file_path, "r") as f:
    # Read the contents of the file into a list of lines
    lines = f.readlines()

# Open a new file to write the modified password list to
with open("modified_list.txt", "w") as f:
    # Iterate over each line in the list
    for line in lines:
        # Split the line into words
        words = line.split()
        # Iterate over each word in the line
        for word in words:
            # Capitalize the first letter of the word and add "1!" to the end
            modified_word = word[0].upper() + word[1:] + "1!"
            # Write the modified word to the output file
            f.write(modified_word + " ")
        # Add a newline character after each line
        f.write("\n")

print("Modified password list written to modified_list.txt")
